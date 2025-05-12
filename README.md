# 🦠 COVID-19 Global Data Tracker

## 📌 Project Overview

This project is a data analysis and visualization tool that tracks global COVID-19 trends using real-world data. It analyzes confirmed cases, deaths, and vaccinations across time and countries, helping to uncover patterns and insights through clear visuals and reports.

---

## 🎯 Objectives

- Import and clean COVID-19 data
- Analyze trends in cases, deaths, and vaccinations
- Compare metrics across multiple countries
- Visualize trends using charts and maps
- Communicate findings through insights and narratives

---

## 🗂️ Project Structure

- `covid_tracker.py`: Main Python script for the entire project (data loading, analysis, and visualization)
-`owid-covid-data.csv`: COVID-19 dataset from Our World in Data (you must download it). The file is now in a zip format because it is very large.
- `README.md`: This project documentation

---

## 🛠️ Tools & Libraries Used

- `pandas` – Data manipulation
- `matplotlib` – Data visualization
- `seaborn` – Enhanced charts


---

## 📥 How to Use

1. **Clone this repository** or download the files.
2. **Download the dataset** from Our World in Data:  
   [https://covid.ourworldindata.org/data/owid-covid-data.csv](https://covid.ourworldindata.org/data/owid-covid-data.csv)
3. Save the file as `owid-covid-data.csv` in the project directory.
4. Run the script:
   ```bash
   python covid_tracker.py
