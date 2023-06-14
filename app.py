# Download the helper library from https://www.twilio.com/docs/python/install
import os
from flask import Flask, request, jsonify, render_template, redirect, url_for
from twilio.rest import Client


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('home.html')


# Define Verify_otp() function
@app.route('/login' , methods=['POST'])
def verify_otp():
    username = request.form['username']
    password = request.form['password']
    mobile_number = request.form['number']

    if username == 'verify' and password == '12345':   
        account_sid = 'ACdf2eed5b4094a2bb1afd2b26ef41b270'
        auth_token = '674730a676727666d2d45976afb07cd5'
        client = Client(account_sid, auth_token)

        verification = client.verify.v2 \
            .services('VA26c1a1ec166166cc426e2703c0afcbbf') \
            .verifications \
            .create(to=mobile_number, channel='sms')

        print(verification.status)
        return render_template('otp_verify.html')
    else:
        return render_template('user_error.html')



@app.route('/otp', methods=['POST'])
def get_otp():
    print('processing')

    received_otp = request.form['received_otp']
    mobile_number = request.form['number']

    account_sid = 'ACdf2eed5b4094a2bb1afd2b26ef41b270'
    auth_token = '674730a676727666d2d45976afb07cd5'
    client = Client(account_sid, auth_token)                                                 
    verification_check = client.verify.v2 \
        .services('VA26c1a1ec166166cc426e2703c0afcbbf') \
        .verification_checks \
        .create(to=mobile_number, code=received_otp)
    print(verification_check.status)

    if verification_check.status == "pending":
        return render_template('otp_error.html')
    else:
        return redirect("https://project-c272.onrender.com/")


if __name__ == "__main__":
    app.run()

