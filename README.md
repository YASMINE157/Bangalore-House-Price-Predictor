# 🏠 Bengaluru House Price Predictor

An end-to-end Machine Learning project that predicts real estate prices in Bengaluru, India. This project covers the entire data science lifecycle, from data cleaning and outlier removal to building a predictive model and deploying it as a web application.

## 🚀 Live Demo
Check out the live app here: [http://192.168.1.7:8501/]

## 📌 Project Overview
Buying a home is a major life decision, but pricing can be complex. This project uses a **Ridge Regression** model to provide estimated prices based on:
* **Location:** Supporting 242 unique locations in Bengaluru.
* **Total Square Feet:** The overall area of the property.
* **BHK:** Number of bedrooms/hall/kitchen.
* **Bathrooms:** Number of bathrooms available.

## 🛠️ Tech Stack
* **Language:** Python 3.x
* **Data Manipulation:** Pandas, NumPy
* **Machine Learning:** Scikit-Learn (Pipelines, Ridge Regression, OneHotEncoder, StandardScaler)
* **Web Framework:** Streamlit
* **Deployment:** Streamlit Community Cloud
* **Model Export:** Joblib / Pickle

## 📊 Data Science Workflow
1. **Data Cleaning:** Handled missing values and simplified the `size` and `total_sqft` columns.
2. **Feature Engineering:** Reduced the dimensionality of the 'Location' column by grouping infrequent locations into an 'Other' category.
3. **Outlier Removal:** Applied business logic and statistical methods (Mean & Standard Deviation) to remove anomalies (e.g., houses with 2 bedrooms but only 500 sqft).
4. **Pipeline Building:** Created a robust `scikit-learn Pipeline` to handle preprocessing and modeling in one step.
5. **Model Selection:** Compared Linear Regression, Lasso, and Ridge, selecting **Ridge** for its superior performance and generalization.



## 📂 Repository Structure
```text
├── app.py                           # Streamlit web application code
├── Bengaluru_House_price_model.pkl  # Trained Ridge Regression Pipeline
├── requirements.txt                 # List of dependencies for deployment
└── README.md                        # Project documentation
