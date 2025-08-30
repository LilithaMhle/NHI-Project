# National Health Insurance (NHI) – Machine Learning Project

**Module:** Technical Programming 2  
**Due Date:** 30 August 2025  

**Group Members (Alphabetical Order):**  
- Mhle L. – 22322987  
- Mncwango A. S. – 22334567  
- Msane Z. N. – 22415488  
- Mthembu S. H. – 22337669  
- Ngwadla M. – 22310899  
- Shangase S. – 22315517  

---

## Project Overview

This project focuses on predicting healthcare service demand under South Africa's National Health Insurance (NHI) system using real-world clinical data from the **MIMIC-III Clinical Database (Demo Version 1.4)**.  

The goal is to build a machine learning model where we predict healthcare service demand under the NHI system, using patient demographics, admissions, diagnoses, and treatment data.

## Features

- **Machine Learning Life Cycle:** Includes problem definition, data collection, preparation, EDA, feature engineering, model building, and evaluation.  
- **Data Source:** MIMIC-III Demo dataset, multi-relational with tables including patients, admissions, diagnoses, procedures, prescriptions, lab events, and transfers.  
- **Predictive Modeling:** Random Forest classifier predicts healthcare service type (Emergency, Elective, Urgent) based on patient demographics and clinical features.  
- **Data Insights:** Exploratory data analysis visualizes patient demographics, length of stay, admission types, and common diagnoses.  
- **Feature Engineering:** Includes patient age, number of diagnoses, number of procedures, and admission type.  
- **Streamlit Dashboard:** Interactive dashboard for exploring data, model results, and application settings.  

---

## Streamlit Dashboard – User Interface

The **NHI Dashboard** provides an intuitive interface to explore healthcare data and model predictions. It has a **sidebar menu** and four main tabs:

- **Home** – Overview of the project, its goals (predicting healthcare demand, forecasting costs, evaluating access disparities), and team members.  
- **EDA** – Explore datasets with tables, charts for age distribution and admission types, and filtering options.  
- **Model** – Displays machine learning results, including model accuracy and classification report.  
- **Settings** – Configure theme (dark/light), notifications, and auto-refresh options.  

---

## Dataset

The dataset used is provided as a `.zip` archive:  

`mimic-iii-clinical-database-demo-1.4.zip`  

It contains CSV files such as:  

- `PATIENTS.csv` – Patient demographics  
- `ADMISSIONS.csv` – Hospital admissions  
- `ICUSTAYS.csv` – ICU stay details  
- `DIAGNOSES_ICD.csv` – Patient diagnoses  
- `PROCEDURES_ICD.csv` – Medical procedures  
- `PRESCRIPTIONS.csv` – Prescribed medications  
- `LABEVENTS.csv` – Lab test results  
- `CHARTEVENTS.csv` – Vital signs and observations  
- `TRANSFERS.csv` – Patient transfers  

Primary and foreign keys such as `subject_id`, `hadm_id`, and `icustay_id` allow merging tables into a single dataset.

---

## Project Steps

1. **Data Collection & Preparation:** Load CSV files into pandas DataFrames, clean missing values, and standardize columns.  
2. **Data Understanding:** Explore dataset structure, relationships, and key variables.  
3. **Exploratory Data Analysis (EDA):** Visualize age distribution, admission types, length of stay, and top diagnoses.  
4. **Feature Engineering:** Merge tables and create features like age, number of diagnoses, and procedures.  
5. **Model Building:** Train a Random Forest classifier to predict healthcare service type.  
6. **Evaluation & Interpretation:** Assess accuracy, precision, recall, and f1-score; interpret results in the context of NHI resource planning.  
7. **Streamlit Dashboard:** Interactive visualization and prediction tool for healthcare service demand.  

---

## Results

- **Model Accuracy:** 87.88%  
- **Insights:**  
  - Age, gender, number of diagnoses, and procedures are predictive of healthcare service type.  
  - Model can guide NHI policy for resource allocation, emergency services planning, and ICU distribution.  

---

## Future Improvements

- Incorporate additional features such as lab results, comorbidity indices, or medication patterns.  
- Explore advanced machine learning algorithms (e.g., XGBoost, Neural Networks).  
- Expand the Streamlit dashboard with more interactive visualizations and predictive scenarios.  

---

## References

- **PhysioNet – MIMIC-III Clinical Database (v1.4):** [https://physionet.org/content/mimiciii-demo/1.4/](https://physionet.org/content/mimiciii-demo/1.4/)  
