# Project: Crop Yield Prediction under Climate Change - Group 4

### FTL Syria – AI for Climate: Machine Learning Challenge

## 📖 Overview

This repository contains the work for our group project, **Problem 1: Crop Yield Prediction**, as part of the Frontier Tech Leaders (FTL) Syria Programme's AI for Climate Machine Learning Challenge.

The goal is to develop and compare machine learning models that can predict agricultural crop yield based on historical climate and agricultural data. This project aims to explore how climate variables like temperature, rainfall, and solar radiation impact crop production, which is crucial for developing climate-resilient agriculture strategies.

## 🎯 Problem Statement & Research Question

- **Problem Statement:** Develop a machine learning model that predicts agricultural crop yield based on historical climate and agricultural data.
- **Research Question:** Can historical weather conditions help us predict crop yields, and which machine learning model produces more accurate predictions?

## 👥 Team Members (Group 4)

| Name | Email Address | Field | WhatsApp |
| :--- | :--- | :--- | :--- |
| **Nimra Afzaal** | nimraafzaal1998@gmail.com | Electrical and Power Engineering | +03094713313 |
| **Sular Albalkhi** | sularalbalkhi@gmail.com | Electronics and Communications Engineering | +936943700523 |
| **Zaid Aldeen Mohammad Kiki** | kikizaid2@gmail.com | Electrical and Power Engineering | +963997527701 |
| **Ahmad Deeb** | ahmaddeebdev@gmail.com | Electronics and Communications Engineering | +963984074032 |

## 🗃️ Data Sources

Our analysis will rely on two primary open data sources:

1.  **FAOSTAT:**
    - **URL:** [FAOSTAT Database](https://www.fao.org/faostat/en/#data/QCL)
    - **Purpose:** To obtain historical crop production, harvested area, and yield data by country and year.
    - **Target Variable:** Crop yield (hg/ha).

2.  **NASA POWER:**
    - **URL:** [NASA POWER Daily API](https://power.larc.nasa.gov/data-access-viewer/)
    - **Purpose:** To collect historical daily temperature, precipitation, and solar radiation data for the same countries and years.

## ⚙️ Project Plan & Methodology

The project will follow a standard machine learning workflow:

1.  **Data Collection & Cleaning:** Download, merge, and clean datasets from FAOSTAT and NASA POWER. We will align data by country and year, and handle any missing values.
2.  **Exploratory Data Analysis (EDA):** Analyze the relationships between climate variables (temperature, rainfall, solar radiation) and crop yield. Visualize trends and correlations.
3.  **Feature Engineering:** Create meaningful features from the raw data. This includes:
    - Average/maximum temperature for the growing season.
    - Annual/seasonal rainfall totals.
    - Average solar radiation.
    - Country, year, and crop type as categorical features.
4.  **Model Development:** We will implement and train two different regression models to compare their performance:
    - **Model A:** Decision Tree Regressor
    - **Model B:** XGBoost Regressor
5.  **Model Evaluation:** The models will be evaluated using a validation set and compared based on the following metrics:
    - **Mean Absolute Error (MAE)**
    - **Root Mean Squared Error (RMSE)**
    - **R² (Coefficient of Determination)**

    We will use cross-validation to ensure the models are robust and not overfitting.

## 📈 Expected Outcome

- **Model Comparison:** A clear comparison of the Decision Tree and XGBoost models, identifying which performs better for this specific task.
- **Feature Importance:** An analysis of which climate variables contribute most to crop yield prediction.
- **Insights & Discussion:** A discussion on how these findings can support and inform climate-resilient agriculture policies and practices, helping farmers and policymakers make better decisions.

## 📋 Important Considerations

- **Avoiding Data Leakage:** A critical requirement is to **not use production volume or harvested area as predictors** when predicting yield, as they are components of the yield calculation itself. We will focus on climate and other external features.
- **Temporal Data:** We will be careful not to introduce future climate information into our historical predictions. The model must only use data that would be available at the time of prediction.

## 📂 Project Status

| Task | Status |
| :--- | :---: |
| Data Collection & Cleaning | ⏳ Not Started |
| Exploratory Data Analysis (EDA) | ⏳ Not Started |
| Feature Engineering | ⏳ Not Started |
| Model Training & Tuning | ⏳ Not Started |
| Evaluation & Comparison | ⏳ Not Started |
| Final Report & Presentation | ⏳ Not Started |

## 🛠️ Tools and Technologies

- **Programming Language:** Python
- **Libraries:** Pandas, NumPy, Scikit-learn, XGBoost, Matplotlib, Seaborn
- **Environment:** Jupyter Notebook / Google Colab