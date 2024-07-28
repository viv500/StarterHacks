from flask import Flask, jsonify, request
from flask_cors import CORS

import random
from openai import OpenAI

client = OpenAI(
    api_key = "sk-None-tgdmWCo2Ge4XFK3dW8XPT3BlbkFJZrb594nsOoyvtdXqxqvY"
)

scam_phrases = {
    "Social security digits": 87, 
    "You've won a prize": 76,
    "Verify your account information": 32,
    "Urgent action required": 81,
    "This is not a scam": 83,
    "Call this number immediately": 80,
    "Your account has been compromised": 99,
    "Exclusive deal just for you": 44,
    "Pre-approved loan": 95,
    "Click this link to claim your reward": 83,
    "Lower your interest rates": 70,
    "You owe back taxes": 97,
    "Free trial, just pay shipping": 91,
    "Suspicious activity detected": 48,
    "Your computer has a virus": 92,
    "We need your personal information": 95,
    "Special promotion, act now": 60,
    "Urgent message from the IRS": 100,
    "You have unpaid fines": 76,
    "Confirm your password": 100,
    "Your bank account is at risk": 90,
    "Immediate action required: update your payment information": 90,
    "This is your final notice. Your car warranty is about to expire": 68,
    "You have an unclaimed inheritance. Contact us to claim it": 100,
    "Your subscription is about to expire. Renew now": 33,
    "Complete this survey to win a gift card": 20,
    "Immediate response required": 76,
    "You have a package waiting for you": 51,
    "We have a job offer for you": 100,
    "Verify your email to continue": 36,
}

app = Flask(__name__)
cors = CORS(app, origins='*')

@app.route('/', methods=['GET'])
def home(): 
    return jsonify(
        {
            "users": ['vivek', 'harishan', 'manit']
        }
    )

@app.route('/', methods=['POST'])
def receive_data(): 
    data = request.json
    print(data)
    return jsonify({'status': 'success', 'received': data})

if __name__ == '__main__': 
    app.run(debug=True)