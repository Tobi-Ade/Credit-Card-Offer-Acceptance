"""
importing necessary libraries
"""
#Analysis packages
import numpy as np
import pandas as pd 

#Visualization packages
import matplotlib.pyplot as plt 
import seaborn as sns 

#Machine Learning Packages
from sklearn.model_selection import train_test_split
from sklearn.metrics import mutual_info_score
from sklearn.feature_extraction import DictVectorizer 
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier

import warnings 
import pickle 
warnings.filterwarnings("ignore")



"""
reading the data and checking the shape
"""
print("Loading data...")
try:
    df = pd.read_csv("./data/creditcardmarketing-bbm.csv")
    print("Loading successful")
except Exception as error:
    print(error)



"""
Creating a copy of the dataset to be used for analysis 
"""
data = df.copy()


data.columns = data.columns.str.lower().str.replace(" ", '_')

data.rename(columns={'#_bank_accounts_open':'bank_accounts_open', "#_homes_owned":"homes_owned", 
                     '#_credit_cards_held':'credit_cards_held'}, inplace=True)

data['accepted_offer'] = (data['offer_accepted']=="Yes").astype(int)
    
del data['offer_accepted']


"""
dropping redundant columns
"""
data = data.drop(['index', 'customer_number'], axis=1)

"""
checking for missing values
"""
data.isnull().sum()


"""
dropping columns with missing values
"""

data.dropna(inplace=True)

numerical_cols = ['q1_balance', 'credit_cards_held',
                  'q2_balance', 'q3_balance', 'q4_balance', 'average_balance', 
                  'household_size', 'bank_accounts_open', 'homes_owned']

categorical_cols = ['reward', 'mailer_type', 'income_level', 
                    'overdraft_protection', 'credit_rating', 'own_your_home' ]


"""
Splitting the data 
"""
df_full_train, df_test = train_test_split(data, test_size=0.2, random_state=1)
df_train, df_val = train_test_split(df_full_train, test_size=0.25, random_state=1)

y_full_train = df_full_train.accepted_offer.values
y_train = df_train.accepted_offer.values
y_val = df_val.accepted_offer.values
y_test = df_test.accepted_offer.values

del df_full_train['accepted_offer']
del df_train['accepted_offer']
del df_val['accepted_offer']
del df_test['accepted_offer']

def train(df, y):
    """
    This function takes in a set of features and targets, 
    and fits them on a logistic regression model
    params: features, target
    returns: dict vectorizer, model objects
    rtype: object
    """
    train_dict = df.to_dict(orient='records')
    dv = DictVectorizer()
    X = dv.fit_transform(train_dict)

    model = LogisticRegression(random_state=1)
    model.fit(X, y)
    
    return dv, model

def predict(df, dv, model):
    """
    This function predicts a target class for a set of features
    params: features, standard scaler and model objects
    returns: target class
    rtype: integer
    """
    test_dict = df.to_dict(orient="records")    
    X = dv.transform(test_dict)
    y_pred = model.predict(X)

    return y_pred


"""
Evaluating model on test data 
"""

dv, model = train(df_full_train, y_full_train)

y_pred = predict(df_test, dv, model)

round(accuracy_score(y_test, y_pred), 3)


#Saving the model
output_file = "model.bin"

with open(output_file, 'wb') as output_file:
    pickle.dump((dv, model), output_file) 

print(f"model successfully saved to {output_file}")

