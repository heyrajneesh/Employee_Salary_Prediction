# Salary Prediction App (Random Forest + Streamlit)

This project predicts whether an individual earns **more than 50K** per year using demographic and work-related features.  
It uses a **Random Forest model** with a pre-processing pipeline (encoding & scaling) and provides a **Streamlit web interface** for predictions.

---

## **Features**
- **Random Forest Classifier** trained on the Adult Income dataset  
- **Streamlit frontend** for interactive prediction  
- Preprocessing with **OneHotEncoder** & **StandardScaler**  
- Handles class imbalance using **class weights**

---

## **Project Structure**
- `app.py` – Streamlit frontend  
- `rf_salary_model.pkl` – Trained Random Forest model  
- `preprocessor.pkl` – Preprocessing pipeline  
- `requirements.txt` – Dependencies  

---
Dataset
The model is trained on the Adult Income Dataset(Kaggle)
Screenshot
## **Screenshot**
![App Screenshot]([screenshot.png](https://github.com/heyrajneesh/Employee_Salary_Prediction/blob/c72ae6f8931d301b5b433266c67cec4a656bb4a8/Screenshot%20(21).png))
