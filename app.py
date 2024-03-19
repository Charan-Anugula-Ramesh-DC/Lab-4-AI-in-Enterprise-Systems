from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)

# Load the trained model
model = joblib.load('fish_weight_prediction_model.pkl')

# Define the species options
species_options = ['Bream', 'Parkki', 'Perch', 'Pike', 'Roach', 'Smelt', 'Whitefish']

@app.route('/')
def home():
    return render_template('index.html', prediction_result="", length1="", length2="", length3="", height="", width="", selected_species="", species_options=species_options)

@app.route('/predict', methods=['POST'])
def predict():
    # Get input values from the form and convert them to floats
    length1 = float(request.form['Length1'])
    length2 = float(request.form['Length2'])
    length3 = float(request.form['Length3'])
    height = float(request.form['Height'])
    width = float(request.form['Width'])
    selected_species = request.form['Species']
    
    # Encode the selected species
    encoded_species = [0] * len(species_options)
    species_index = species_options.index(selected_species)
    encoded_species[species_index] = 1

    # Combine input values and encoded species into a single array
    features = np.array(encoded_species + [length1, length2, length3, height, width]).reshape(1, -1)

    # Make prediction
    prediction = model.predict(features)

    # Pass input values back to the form for display
    return render_template('index.html', prediction_result=f'Predicted weight: {prediction[0]:.2f} grams', length1=length1, length2=length2, length3=length3, height=height, width=width, species=selected_species, species_options=species_options)

if __name__ == '__main__':
    app.run(debug=True)
