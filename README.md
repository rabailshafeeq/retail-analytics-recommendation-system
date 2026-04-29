# EDA on UCI Online Retail Dataset

## 📌 Project Overview
This project performs an **Exploratory Data Analysis (EDA)** on the [UCI Online Retail Dataset](https://archive.ics.uci.edu/dataset/352/online+retail) to uncover key insights related to customers, products, and temporal sales patterns.

### 🎯 Objectives
- **Data Quality Report:** Identify missing data, duplicates, and outliers.
- **Customer Insights:** Analyze purchasing behavior, frequency, and high-value customers.
- **Product Analysis:** Determine top-selling products, revenue drivers, and return-prone items.
- **Temporal Patterns:** Examine sales cycles, peak times, and seasonal trends.
- **Actionable Insights:** Provide recommendations for improving sales, reducing returns, and enhancing customer retention.
- **Product Recommendation System:** Recommending products to customers based on purchase patterns.

---

## 📂 Dataset Information
- **Source:** UCI Machine Learning Repository
- **Dataset Name:** Online Retail (11/5/2015)
- **Time Period:** 01/12/2010 - 09/12/2011
- **Description:** The dataset contains transactional data for a UK-based online retail store selling unique all-occasion gifts. Many customers are wholesalers.

🔗 **[Dataset Link](https://archive.ics.uci.edu/dataset/352/online+retail)**

---

## 🛠️ Setup & Installation
### 1️⃣ Clone the repository
```bash
git clone https://github.com/AzizbekAvazov/eda-uci-retail-dataset.git
cd eda-uci-retail-dataset
```
### 2️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```
### 3️⃣ Run the Jupyter Notebook
```bash
jupyter notebook notebooks/01_data_exploration.ipynb
```
Ensure the dataset file is present at:
```
data/uci_online_retail.xlsx
```

---

## 📊 Folder Structure
```bash
.
├── data/
│   └── uci_online_retail.xlsx         # Raw dataset
├── notebooks/
│   └── 01_data_exploration.ipynb      # EDA + Recommendation System
├── requirements.txt                   # Dependencies
└── README.md
```

---

## 🧠 Key Features
- 📉 Data cleaning, anomaly detection using Isolation Forest
- 🔄 Time-series and trend analysis
- 📊 Rich visualizations (Seaborn, Matplotlib)
- 🧑‍🤝‍🧑 Collaborative Filtering Recommendation System using KNN and Cosine Similarity

---

## ✅ License

This project is open source and free to use under the MIT License.

<!-- Keywords: Exploratory Data Analysis, EDA, Online Retail Dataset, UCI Machine Learning, Data Science, Data Visualization, Sales Analysis, Product Recommendation, Collaborative Filtering, Customer Behavior, Nearest Neighbors -->
