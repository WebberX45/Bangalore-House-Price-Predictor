# Bangalore House Price Predictor

Welcome to my **Bangalore House Price Prediction** project. In this project, I built a **machine learning model and deployed it using a Flask web application** to predict house prices in Bangalore based on key property features.

The system allows users to input **location, BHK, number of bathrooms, and total square feet**, and the model predicts the estimated house price.

---

## Dataset

The dataset used in this project is the **Bangalore House Price Dataset**, which contains real estate data for properties located in Bangalore.

Dataset features include:

- **Location** – Area where the property is located
- **BHK** – Number of bedrooms
- **Bathrooms** – Number of bathrooms in the house
- **Total Square Feet** – Total size of the property
- **Price** – House price in lakhs

This dataset enables the development of a **predictive model for estimating real estate prices**.

---

## Tools & Technologies

### Programming
- Python

### Libraries
- Pandas
- NumPy
- Scikit-learn
- Pickle

### Web Development
- Flask
- HTML
- Bootstrap
- JavaScript (AJAX)

---

## Project Workflow

### 1. Data Preprocessing
- Cleaned and formatted the Bangalore housing dataset
- Removed inconsistent and missing data
- Standardized location and numerical features

### 2. Feature Engineering
Selected key features affecting house prices:

- Location
- BHK
- Bathrooms
- Total Square Feet

### 3. Model Training
A **Ridge Regression model** was trained using Scikit-learn to predict house prices.

The trained model was then saved using **Pickle**.

### 4. Model Deployment
A **Flask web application** was created to serve the trained model.

The application:
- Accepts user inputs through a web form
- Sends inputs to the backend
- Uses the trained model to generate predictions

The prediction is returned and displayed on the webpage dynamically.

Example backend logic: :contentReference[oaicite:0]{index=0}

### 5. Frontend Interface
A simple and responsive interface was developed using **HTML and Bootstrap** where users can input property details and get predicted house prices.

Frontend interface code: :contentReference[oaicite:1]{index=1}

---

## Key Insights

- Property **location plays a major role in determining house prices**.
- Larger houses with more **square footage generally have higher prices**.
- **Number of bathrooms and BHK count** significantly influence pricing.
- Ridge Regression helps handle **multicollinearity between features** and improves prediction stability.

---

## Real-World Applications

This project demonstrates how machine learning can be applied in the **real estate industry**.

Possible applications include:

- **Real Estate Platforms**  
  Websites like 99acres, MagicBricks, and Housing.com can estimate property values automatically.

- **Property Valuation Tools**  
  Buyers and sellers can estimate fair property prices before transactions.

- **Real Estate Investment Analysis**  
  Investors can identify profitable property investments.

- **Smart Property Recommendation Systems**  
  Platforms can recommend houses based on predicted market values.

- **Urban Development Planning**  
  Government agencies can analyze housing trends and pricing patterns.

---

## Conclusion

This project demonstrates a complete **end-to-end machine learning pipeline**, including:

- Data preprocessing
- Model training
- Model serialization
- Web deployment using Flask
- Interactive frontend interface

By combining **machine learning and web development**, the system provides a simple tool to estimate house prices based on property characteristics.

---

## Contact

For questions, feedback, or collaboration:

LinkedIn:  
https://www.linkedin.com/in/pranav-kumar-553583394

Email:  
d.sci.pranav@gmail.com
