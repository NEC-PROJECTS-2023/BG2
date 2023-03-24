from flask import Flask, render_template, request
import json
import pickle
import numpy as np

app = Flask(__name__)
model = pickle.load(open('loan_application.pkl', 'rb'))
model1 = pickle.load(open('personalloan.pkl', 'rb'))

@app.route('/')
def Home():
    return render_template('index1.html')
@app.route('/business.html')
def business():
    return render_template('business.html')
@app.route('/personal.html')
def personalloan():
    return render_template('personal.html')
@app.route("/personal",methods=['POST','GET'])
def personal():
    if request.method=='POST':
        # id=float(request.form['id'])
        income = int(request.form['income'])
        age = int(request.form['age'])
        experiance=int(request.form['experiance'])
        marital= int(request.form['marital'])
        house = int(request.form['house'])
        car = int(request.form['car'])
        crjy = int(request.form['crjy'])
        crhy =int(request.form['crhy'])
        xx= np.zeros(8)
        xx[0]=income
        xx[1]=age
        xx[2]=experiance
        xx[3]=marital
        xx[4]=house
        xx[5]=car
        xx[6]=crjy
        xx[7]=crhy
        

    res=model1.predict([xx])[0]
    if res==1:
        return render_template('personal.html',res="Sorry, your loan application is Rejected.")
    else:
        return render_template('personal.html',res="Congratulations!!! your loan application is Approved!")


@app.route("/predict", methods=['POST','GET'])
def predict():
    

    if request.method == 'POST':
        gender = int(request.form['gender'])
        married = int(request.form['married'])
        dependents = int(request.form['dependents'])
        education = int(request.form['education'])
        selfemployed = int(request.form['selfemployed'])
        applicantincome = int(request.form['applicantincome'])
        coapplicantincome = int(request.form['coapplicantincome'])
        loanamount = int(request.form['loanamount'])
        loanamountterm = int(request.form['loanamountterm'])
        credithistory = int(request.form['credithistory'])
        propertyarea = int(request.form['propertyarea'])
        x= np.zeros(11)
        x[0]=gender
        x[1]=married
        x[2]=dependents
        x[3]=education
        x[4]=selfemployed
        x[5]=applicantincome
        x[6]=coapplicantincome
        x[7]=loanamount
        x[8]=loanamountterm
        x[9]=credithistory
        x[10]=propertyarea
    result=model.predict([x])[0]
    if result==0:
        return render_template('business.html',result="Sorry, your loan application is Rejected.")
    else:
        return render_template('business.html',result="Congratulations!!! your loan application is Approved!")

    
    
if __name__=="__main__":
    app.run(debug=True)