# Credit-Card-Offer-Acceptance

![Credit Cards](https://www.forbes.com/advisor/wp-content/uploads/2022/07/credit_cards.jpeg-1.jpg)

## Table of Contents 
1. [Problem Definition](#problem-defintion)
2. [Project Outline](#project-outline)
3. [How to Run the Project](#how-to-run-the-project)
4. [References](#References)
5. [Contact Me](#contact-me)

## Problem Definition
This project is carried out to explore customer acceptance trends of credit card offers from financial institutions. By exploring this data we hope to gain better understanding of the factors that influence offer acceptances, and also predict whether a customer is more liekly to accept or decline the offer,

More information on the problem and the data used for this project can be found [here](https://www.kaggle.com/datasets/thedevastator/unlocking-credit-card-offer-acceptance-trends-in)

## Project Outline 
- [Jupyter Notebook](https://github.com/Tobi-Ade/Credit-Card-Offer-Acceptance/blob/main/credit_card_acceptance.ipynb)<br>
  Here we clean the data, carry out exploratory data analysis, train and tune different machine learning models and see how well they perform on the data
 
- [Training the Model](https://github.com/Tobi-Ade/Credit-Card-Offer-Acceptance/blob/main/train.py)<br>
Here the final training occurs. We select the best model, and save it to a file so that it can be used on new data 

- [Creating a Flask App](https://github.com/Tobi-Ade/Credit-Card-Offer-Acceptance/blob/main/predict.py)<br>
This is where we write a script for serving the model. We use the saved model to predict a customer's decision when the data is sent to the flask app.

- [Testing the service ](https://github.com/Tobi-Ade/Credit-Card-Offer-Acceptance/blob/main/request.py)<br>
Here we write a script for testing our predcition service. We send a request to the flask app and it returns the estimated answer based on customer data.

- [Creating a Dockerfile](https://github.com/Tobi-Ade/Credit-Card-Offer-Acceptance/blob/main/Dockerfile)<br>
- We create a virtual environment using docker and run our service here.

## How to Run The Project
Please note that these steps are to be carried out in a terminal window like command prompt or git bash<br>
  - Clone the repository to your computer using:  <br>
  ```bash
  git clone https://github.com/Tobi-Ade/Credit-Card-Offer-Acceptance.git
  ```
  <br>
  
  - Navigate to the directory where you cloned the repo and cd into the cloned repo by running: <br>
  ```bash
  cd Credit-Card-Offer-Acceptance
  ```
  <br>
  You should now be in the project folder
  
  - The libraries used in this project can be found in the [requirements.txt](https://github.com/Tobi-Ade/Credit-Card-Offer-Acceptance/blob/main/requirements.txt) file. It is advisable to run this project in a virtual environment to avoid issues with your system configuration. To create a virtual environment with venv <br>
  ```bash
  python -m venv credit-env
  ```
  
   Activate credit-env with: <br>
   ```bash
   credit-env\Scripts\activate.bat
   ```
   <br>
   
   Now install the libraries from the requirements.txt file by running:<br>
   
   ```bash
   pip install -r requirements.txt
   ```
   
   As we saw earlier, the model was already trained and saved in the train.py file. However, you may want to retrain the model for some reason. You do this by executing the file. In terminal, run:<br>
   ```bash 
   python train.py
   ```
   
  Now deploy the flask app locally by running the predict.py file. It is recommended to do this with a production server like waitress(windows OS) or gunicorn(UNIX).<br>
  You can still run it directly, with:   <br>
  ```bash
  python predict.py
  ```
  
  with waitress: <br>
 
  ```bash
  waitress-serve --listen=0.0.0.0:9090 predict:app
  ```
  
   with gunicorn: <br>
 
  ```bash
  gunicorn --bind 0.0.0.0:9090 predict:app
  ```
  
  Now the prediction service should be running locally on "http://0.0.0.0:9090"
  
  Finally, you send a POST request to the service. You can do this by running the request.py file or use the file to understand the format in which the request will be sent, and then create your own request. This is how you run it:<br>
  ```bash
  python request.py
  ```
  
  You can also decide to build and run the Dockerfile for the project. To build this locally:
  ```bash
  docker build -t credit_card_project .
  ```
  
  Then to run it:<br>
  ```bash
  docker run -it --rm -p 9090:9090 credit_card_project:latest
  ```
  
