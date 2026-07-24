# 🦠 COVID-19 Data Analysis Dashboard

A comprehensive COVID-19 Data Analysis project developed using **Python**, **Pandas**, **NumPy**, **Matplotlib**, **Seaborn**, **Plotly**, and **Streamlit**. The project analyzes global COVID-19 data, performs data preprocessing, exploratory data analysis (EDA), and presents insights through an interactive dashboard.

---

# 📌 Project Overview

The COVID-19 pandemic generated a large amount of publicly available data. This project analyzes the spread of COVID-19 across different countries by exploring confirmed, recovered, and death cases over time.

The project also provides an interactive Streamlit dashboard where users can visualize trends, compare countries, and explore important COVID-19 statistics.

---

# 🎯 Objectives

- Clean and preprocess COVID-19 data.
- Perform Exploratory Data Analysis (EDA).
- Analyze trends of confirmed, recovered, and death cases.
- Compare COVID-19 statistics across different countries.
- Create professional visualizations.
- Build an interactive dashboard using Streamlit.

---

# 📂 Project Structure

```
Cognetix_Covid_Analysis/
│
├── .vscode/
│
├── data/
│   └── Covid19_data.csv
│
├── Images/
│   ├── Daily_Deaths.png
│   ├── Daily_NewCases.png
│   ├── Daily_Recoveries.png
│   └── Worldwide_Cases.png
│
├── Notebook/
│   ├── Analysis.ipynb
│   └── Covid_19_Data.csv
│
├── Streamlit/
│   └── app.py
│
└── README.md
```

---

# 📊 Dataset Information

The dataset contains worldwide COVID-19 records including:

- Date
- Province/State
- Country/Region
- Latitude
- Longitude
- Confirmed Cases
- Death Cases
- Recovered Cases

---

# 🧹 Data Preprocessing

The following preprocessing steps were performed:

- Converted Date column to Datetime format
- Checked missing values
- Removed duplicate records
- Standardized country names
- Created new features:
  - Active Cases
  - Daily Cases
  - Daily Deaths
  - Daily Recoveries
  - Rolling Average
  - Weekly Trend
  - Monthly Trend
  - Recovery Rate
  - Mortality Rate
  - Growth Rate

---

# 📈 Exploratory Data Analysis

The project includes:

- Dataset Overview
- Statistical Summary
- Missing Value Analysis
- Country-wise Analysis
- Time Series Analysis
- Correlation Analysis

---

# 📊 Dashboard Features

The Streamlit dashboard includes the following interactive features:

## 📌 KPI Cards

- Total Confirmed Cases
- Active Cases
- Total Deaths
- Total Recoveries
- Recovery Rate
- Mortality Rate

---

## 🌍 Interactive World Map

A choropleth map displaying confirmed COVID-19 cases worldwide using Plotly.

---

## 📅 Filters

- Country Selection
- Date Range Selection

---

## 📈 Trend Analysis

- Daily New Cases
- Daily Deaths
- Daily Recoveries
- Weekly Trend
- Monthly Trend
- 7-Day Rolling Average

---

## 📊 Country Comparison

Compare multiple countries based on:

- Confirmed Cases
- Death Cases
- Recovery Cases

---

## 📉 Top Countries Analysis

- Top 10 Countries by Confirmed Cases
- Top 10 Countries by Death Cases
- Top 10 Countries by Recoveries
- Top 10 Countries by Active Cases

---

## 📊 Statistical Charts

- Line Charts
- Bar Charts
- Pie Chart
- Scatter Plot
- Histogram
- Box Plot
- Correlation Heatmap

---

## 📋 Data Table

Interactive table displaying country-wise COVID-19 statistics.

---

## 📥 Download Feature

Download the filtered dataset as a CSV file directly from the dashboard.

---

# 📷 Output Screenshots

### Daily New Cases

![Daily Cases](Images/<img width="2958" height="1316" alt="image" src="https://github.com/user-attachments/assets/95c4b379-3ac8-4603-b2be-3565e05e006f" />
)

---

### Daily Deaths

![Daily Deaths](Images/<img width="2888" height="1386" alt="image" src="https://github.com/user-attachments/assets/a349a957-288f-454c-a7af-665a2c7d7519" />
)

---

### Daily Recoveries

![Daily Recoveries](Images/<img width="2890" height="1346" alt="image" src="https://github.com/user-attachments/assets/50fcedb5-b642-47b7-8740-f739c4a3e2db" />
)

---

### Worldwide COVID Cases

![Worldwide Cases](Images/<img width="2954" height="948" alt="image" src="https://github.com/user-attachments/assets/c7616bed-feb5-4fbc-8cfa-22ca5b9eca9f" />
)

---

# 🛠 Technologies Used

| Technology | Purpose |
|------------|---------|
| Python | Programming Language |
| Pandas | Data Cleaning & Analysis |
| NumPy | Numerical Computation |
| Matplotlib | Data Visualization |
| Seaborn | Statistical Visualization |
| Plotly | Interactive Charts |
| Streamlit | Dashboard Development |

---

# 🚀 Installation

## Clone the Repository

```bash
git clone https://github.com/your-username/Covid19-Analysis.git
```

---

## Navigate to the Project

```bash
cd Covid19-Analysis
```

---

## Install Required Libraries

```bash
pip install pandas numpy matplotlib seaborn plotly streamlit
```

or

```bash
pip install -r requirements.txt
```

---

## Run the Dashboard

```bash
streamlit run Streamlit/app.py
```

---

# 📌 Key Insights

- COVID-19 cases increased rapidly during the early stages of the pandemic.
- Recovery rates improved significantly over time.
- Some countries experienced multiple waves of infections.
- Active cases varied considerably across regions.
- Recovery and mortality rates differed between countries.

---

# 🔮 Future Enhancements

- Vaccination Analysis
- Real-Time COVID Data Integration
- Machine Learning Prediction
- State-wise Analysis
- Dark Mode Dashboard
- Additional Interactive Filters

---

# 👨‍💻 Author

**Pranjal Rai**

Final Year MCA Student

- GitHub: https://github.com/pranjalr004
- LinkedIn: https://www.linkedin.com/in/pranjal-rai-998b6329b/

---

# ⭐ If you found this project useful, please consider giving it a Star on GitHub!
