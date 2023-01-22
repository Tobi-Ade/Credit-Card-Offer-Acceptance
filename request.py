import requests

url = "http://localhost:9090/"

customer = {
            'reward': 'Points',
            'mailer_type': 'Postcard',
            'income_level': 'Medium',
            'bank_accounts_open': 1,
            'overdraft_protection': 'Yes',
            'credit_rating': 'High',
            'credit_cards_held': 3,
            'homes_owned': 2,
            'household_size': 3,
            'own_your_home': 'No',
            'average_balance': 1054.5,
            'q1_balance': 830.0,
            'q2_balance': 716.0,
            'q3_balance': 1260.0,
            'q4_balance': 1412.0
}

response = requests.post(url, json=customer).json()

verdict = response['accept_offer']

if verdict == True:
    print("Accpetance Decision: Yes")
else:
    print("Accpetance Decision: No")
