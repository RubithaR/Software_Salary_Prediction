# Software_Salary_Prediction

## **Overview**
This project aims to predict salaries based on various features such as:
- Country
- Age
- Education Level
- Years of Experience
- Developer Type
- Employment Type

The application uses machine learning models to analyze survey data and estimate salaries, providing insights into how different factors influence compensation in the tech industry.

---

## **Technologies Used**
1. **Python Libraries**:
   - **Pandas**: Data manipulation and preprocessing.
   - **NumPy**: Numerical computations.
   - **Matplotlib**: Data visualization.
   - **Scikit-learn**: Machine learning algorithms and model evaluation.

2. **Tools**:
   - **Jupyter Notebook**: For exploratory data analysis and model development.
   - **Streamlit**: To create an interactive web application for predictions.

---

## **How It Works**
1. **Data Preprocessing**:
   - Missing values are handled using techniques like mean imputation and mode replacement.
   - Categorical features are encoded using Label Encoding.
   - Outliers are removed to ensure robust model performance.

2. **Modeling**:
   - Linear Regression, Decision Tree, and Random Forest models are trained and compared.
   - GridSearchCV is used for hyperparameter tuning to optimize the Decision Tree model.

3. **Web Application**:
   - A Streamlit-based interface allows users to input details and get salary predictions.
   - The app displays predictions for a given set of features, such as country, education level, and developer type.

---

## **Project Structure**
```
Salary-Prediction/
│
├── app.py                   # Main Streamlit application
├── predict_page.py          # Prediction logic for Streamlit
├── Salary_Prediction.ipynb  # Jupyter notebook for EDA and modeling
├── saved_steps.pkl          # Serialized model and encoders
├── requirements.txt         # Python dependencies
└── README.md                # Project description (this file)
```

---

## **Setup Instructions**
1. Clone the repository:
   ```bash
   git clone https://github.com/your_username/salary-prediction.git
   cd salary-prediction
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the web application:
   ```bash
   streamlit run app.py
   ```

4. Open the app in your browser:
   ```
   http://localhost:8501
   ```

---

## **Usage**
1. Enter the required details:
   - Country
   - Age
   - Education Level
   - Years of Professional Experience
   - Developer Role
   - Employment Type

2. Click on **Predict** to see the estimated salary.
