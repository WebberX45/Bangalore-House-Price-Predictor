import pandas as pd
from flask import Flask, render_template, request
import pickle

app = Flask(__name__)
df = pd.read_csv('House_Price_Clean_Data.csv')
pipe = pickle.load(open('RidgeModel.pkl', 'rb'))

@app.route('/')
def index():

    locations = sorted(df['location'].unique())
    return render_template('index.html', locations=locations)

@app.route('/predict', methods=['POST'])
def predict():

    location = request.form.get('location')
    bhk = float(request.form.get('bhk'))
    bath = float(request.form.get('bathroom'))
    sqft = float(request.form.get('square_feet'))

    input_df = pd.DataFrame([[location, bhk, bath, sqft]], columns=['location', 'bhk', 'bath', 'total_sqft'])

    prediction = pipe.predict(input_df)[0]

    return str(round(prediction, 2))

if __name__ == '__main__':
    app.run(debug=True, port=5000)