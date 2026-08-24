"""
Fanger PMV/PPD & IMAC (India Model for Adaptive Comfort) Engine
Compliant with ISO 7730, ASHRAE Standard 55-2023, and National Building Code (NBC) 2016 India.
"""

import math
from typing import Dict, Any, Tuple


def calculate_pmv_ppd(
    ta: float,          # Air temperature (°C)
    tr: float,          # Mean radiant temperature (°C)
    vel: float,         # Air speed relative to body (m/s)
    rh: float,          # Relative humidity (%)
    met: float = 1.1,   # Metabolic rate (met), default 1.1 (sedentary / light domestic activity)
    clo: float = 0.5    # Clothing insulation (clo), default 0.5 (typical Indian summer attire)
) -> Tuple[float, float, str]:
    """
    Computes Predicted Mean Vote (PMV) and Predicted Percentage Dissatisfied (PPD)
    based on Fanger's 1970 thermal comfort balance equations (ISO 7730 / ASHRAE 55).
    """
    # Safe bounds on physical inputs
    ta = max(-30.0, min(60.0, float(ta)))
    tr = max(-30.0, min(70.0, float(tr)))
    vel = max(0.05, min(10.0, float(vel)))
    rh = max(5.0, min(100.0, float(rh)))
    met = max(0.8, min(4.0, float(met)))
    clo = max(0.1, min(3.0, float(clo)))

    m = met * 58.15  # Metabolic rate in W/m²
    w = 0.0          # External work in W/m²
    
    # Thermal resistance of clothing in m²K/W
    icl = 0.155 * clo
    if icl <= 0.078:
        fcl = 1.0 + 1.29 * icl
    else:
        fcl = 1.05 + 0.645 * icl
        
    # Water vapor pressure (Pa)
    pa = rh * 10.0 * math.exp(16.6536 - 4030.183 / (ta + 235.0))
    
    taa = ta + 273.15
    tra = tr + 273.15
    tcla = taa + (35.5 - ta) / (3.5 * (6.45 * icl + 0.1))
    
    p1 = icl * fcl
    p2 = p1 * 3.96
    p3 = p1 * 100.0
    p4 = p1 * taa
    p5 = 308.7 - 0.028 * (m - w) + p2 * math.pow(tra / 100.0, 4.0)
    
    xn = tcla / 100.0
    xf = xn
    eps = 0.00015
    
    hcf = 12.1 * math.sqrt(vel)
    
    for _ in range(150):
        xf = (xf + xn) / 2.0
        xf = max(2.5, min(3.8, xf))  # Safety clamp on (Tcl/100)
        hcn = 2.38 * math.pow(abs(100.0 * xf - taa), 0.25)
        hc = max(hcf, hcn)
        
        # Next approximation
        denom = 100.0 + p3 * hc
        if denom == 0:
            denom = 0.001
        xn = (p5 + p4 * hc - p2 * math.pow(xf, 4.0)) / denom
        if abs(xn - xf) <= eps:
            break
            
    tcl = 100.0 * xn - 273.15
    
    # Heat loss components (W/m²)
    hl1 = 3.05 * 0.001 * (5733.0 - 6.99 * (m - w) - pa)
    hl2 = max(0.0, 0.42 * ((m - w) - 58.15))
    hl3 = 1.7 * 0.00001 * m * (5867.0 - pa)
    hl4 = 0.0014 * m * (34.0 - ta)
    hl5 = 3.96 * fcl * (math.pow(xn, 4.0) - math.pow(tra / 100.0, 4.0))
    hl6 = fcl * hc * (tcl - ta)
    
    # Thermal load on body
    thermal_load = (m - w) - (hl1 + hl2 + hl3 + hl4 + hl5 + hl6)
    
    # Predicted Mean Vote (PMV)
    pmv = (0.303 * math.exp(-0.036 * m) + 0.028) * thermal_load
    pmv = max(-3.0, min(3.0, round(pmv, 2)))
    
    # Predicted Percentage of Dissatisfied (PPD)
    ppd = 100.0 - 95.0 * math.exp(-0.03353 * math.pow(pmv, 4.0) - 0.2179 * math.pow(pmv, 2.0))
    ppd = max(5.0, min(100.0, round(ppd, 1)))
    
    # Categorization based on ASHRAE 55 & ISO 7730
    if abs(pmv) <= 0.5:
        category = "Comfortable (Neutral)"
    elif 0.5 < pmv <= 1.0:
        category = "Slightly Warm"
    elif 1.0 < pmv <= 2.0:
        category = "Warm (Discomfort)"
    elif pmv > 2.0:
        category = "Hot (Severe Overheating)"
    elif -1.0 <= pmv < -0.5:
        category = "Slightly Cool"
    elif -2.0 <= pmv < -1.0:
        category = "Cool"
    else:
        category = "Cold (Underheating)"
        
    return pmv, ppd, category


def calculate_imac_adaptive_comfort(
    tout_running_mean: float,
    tin: float
) -> Dict[str, Any]:
    """
    Indian Model for Adaptive Comfort (IMAC) for naturally ventilated buildings (NBC 2016).
    """
    t_neutral = 0.54 * tout_running_mean + 12.83
    
    lower_90 = t_neutral - 2.38
    upper_90 = t_neutral + 2.38
    lower_80 = t_neutral - 3.46
    upper_80 = t_neutral + 3.46
    
    is_90_compliant = lower_90 <= tin <= upper_90
    is_80_compliant = lower_80 <= tin <= upper_80
    
    return {
        "t_neutral": round(t_neutral, 1),
        "band_90": (round(lower_90, 1), round(upper_90, 1)),
        "band_80": (round(lower_80, 1), round(upper_80, 1)),
        "indoor_temp": round(tin, 1),
        "is_90_compliant": is_90_compliant,
        "is_80_compliant": is_80_compliant,
        "status": "Optimal (90% Acceptable)" if is_90_compliant else ("Acceptable (80%)" if is_80_compliant else "Outside Comfort Envelope")
    }
