# Fish Weight Prediction Web App

This is a web application that predicts the weight of a fish based on its species, length measurements, height, and width. The application utilizes a machine learning model trained on the Fish Market dataset.

## Features

- Allows users to input fish attributes such as species, length measurements, height, and width.
- Predicts the weight of the fish based on the provided attributes.
- Displays the predicted weight on the web interface.
- Retains the selected species and input values after the form submission.

## Installation

1. Clone this repository to your local machine:

    ```bash
    git clone https://github.com/Charan-Anugula-Ramesh-DC/Lab-4-AI-in-Enterprise-Systems.git
    ```

2. Navigate to the project directory:

    ```bash
    cd Lab-4-AI-in-Enterprise-Systems
    ```

3. Install the required Python packages:

    ```bash
    pip install -r requirements.txt
    ```

4. Run the Flask web server:

    ```bash
    python app.py
    ```

5. Open your web browser and go to `http://127.0.0.1:5000` to access the application.

## Usage

1. Enter the species of the fish from the dropdown menu.
2. Input the length measurements, height, and width of the fish.
3. Click the "Predict" button.
4. The predicted weight of the fish will be displayed on the web interface.

## Technologies Used

- Python
- Flask
- HTML/CSS
- scikit-learn

## Dataset

The Fish Market dataset used for training the machine learning model can be found on [Kaggle](https://www.kaggle.com/aungpyaeap/fish-market).

## Credits

This project was developed by Charan Anugula Ramesh. Feel free to contribute by submitting bug reports, feature requests, or pull requests.
