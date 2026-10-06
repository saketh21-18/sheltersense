# ShelterSense AI

> **Data-Driven Shelter Design for Thermal Comfort in Extreme Environments**

ShelterSense AI is an intelligent shelter-design platform that analyzes **location, terrain, weather, and environmental conditions** to help identify shelter configurations suitable for extreme climates.

The system focuses on improving thermal comfort in challenging environments such as **high-altitude cold regions, extreme-heat zones, and humid regions** by combining environmental data with thermal comfort models and data-driven recommendations.

---

## Problem

Designing shelters for extreme environments is challenging because temperature, humidity, wind speed, solar conditions, and terrain can vary significantly between locations.

Traditional shelter design often requires extensive manual analysis.

**ShelterSense AI aims to simplify this process by providing a data-driven approach to evaluating thermal comfort and exploring suitable shelter designs.**

---

## Solution

ShelterSense AI follows a data-driven workflow:

```text
Location & Terrain
        ↓
Environmental Conditions
        ↓
Weather & Climate Data
        ↓
Thermal Comfort Analysis
        ↓
PMV / PPD Evaluation
        ↓
Shelter Design Recommendations
        ↓
Comfort Score & Insights
```

The platform helps users understand how different environmental conditions can influence shelter comfort and design decisions.

---

## Key Features

* 🌍 **Location-Based Analysis**

  * Analyze environmental conditions for different geographical locations.

* 🌡️ **Thermal Comfort Analysis**

  * Evaluate thermal comfort using PMV and PPD concepts.

* 🏔️ **Extreme Environment Support**

  * Designed around challenging environments such as cold, hot, and humid regions.

* 📊 **Data-Driven Insights**

  * Convert environmental parameters into meaningful shelter-design insights.

* 🏠 **Shelter Design Recommendations**

  * Explore design considerations based on environmental conditions.

* 📈 **Comfort Scoring**

  * Present thermal comfort results in an easy-to-understand format.

* 💻 **Interactive Web Interface**

  * Simple interface for entering conditions and exploring results.

---

## Example Use Cases

### 🏔️ High-Altitude Cold Regions

Example: **Ladakh**

Shelters need to minimize heat loss while maintaining acceptable indoor thermal conditions.

### 🏜️ Extreme-Heat Regions

Example: **Rajasthan**

Shelter design needs to reduce heat gain and improve thermal comfort during extremely high temperatures.

### 🌧️ High-Humidity Regions

Example: **Northeastern India**

Shelters need to account for high humidity, ventilation, rainfall, and moisture-related conditions.

---

## Technology & Concepts

### Core Concepts

* Thermal Comfort
* PMV — Predicted Mean Vote
* PPD — Predicted Percentage of Dissatisfied
* Environmental Data Analysis
* Data-Driven Shelter Design
* Climate-Aware Design

### Standards & References

* ISO 7730
* ASHRAE Thermal Comfort Guidelines
* Fanger Thermal Comfort Model
* NASA POWER Climate Data
* Central Building Research Institute (CBRI)

---

## Project Architecture

```text
                ┌─────────────────────┐
                │   User Input        │
                │ Location / Terrain  │
                └──────────┬──────────┘
                           ↓
                ┌─────────────────────┐
                │ Environmental Data  │
                │ Temperature         │
                │ Humidity            │
                │ Wind Speed          │
                │ Solar Conditions    │
                └──────────┬──────────┘
                           ↓
                ┌─────────────────────┐
                │ Thermal Comfort     │
                │ Analysis            │
                │ PMV / PPD           │
                └──────────┬──────────┘
                           ↓
                ┌─────────────────────┐
                │ Shelter Evaluation  │
                │ & Recommendations   │
                └──────────┬──────────┘
                           ↓
                ┌─────────────────────┐
                │ Comfort Score &     │
                │ Design Insights     │
                └─────────────────────┘
```

---

## Project Structure

```text
ShelterSense-AI/
│
├── assets/
├── src/
├── components/
├── public/
├── README.md
├── package.json
└── ...
```

> The exact structure may vary depending on the current implementation.

---

## Getting Started

### Clone the Repository

```bash
git clone https://github.com/YOUR-USERNAME/ShelterSense-AI.git
cd ShelterSense-AI
```

### Install Dependencies

```bash
npm install
```

### Run the Project

```bash
npm run dev
```

Open the local development URL shown in your terminal.

---

## Research & References

The project is inspired by established thermal-comfort standards and environmental data sources:

* [ISO 7730](https://www.iso.org/standard/39155.html?utm_source=chatgpt.com)
* [ASHRAE](https://www.ashrae.org/?utm_source=chatgpt.com)
* [NASA POWER](https://power.larc.nasa.gov/?utm_source=chatgpt.com)
* [Central Building Research Institute](https://cbri.res.in/?utm_source=chatgpt.com)

---

## Why ShelterSense AI?

Extreme environments require shelter designs that respond to their surroundings rather than relying on a one-size-fits-all approach.

ShelterSense AI explores how **environmental intelligence + thermal comfort modelling + data-driven design** can support better shelter planning for challenging terrains.

---

## Future Improvements

* Real-time weather data integration
* Advanced ML-based shelter optimization
* 3D shelter visualization
* Terrain-aware structural recommendations
* Material selection based on climate
* Solar radiation and energy analysis
* Regional language support
* Offline support for remote locations
* Integration with IoT environmental sensors

---

## Project Status

🚧 **Currently under development**

ShelterSense AI is being developed as a research-oriented prototype for intelligent and climate-aware shelter design.

---

## Developer

**Saketh** — Developer

BTech Student | Artificial Intelligence & Machine Learning

·

---

## License

This project is intended for **educational, research, and prototype development purposes**.
