import flask
import pickle
import pandas as pd
import numpy as np


from sklearn.preprocessing import StandardScaler


with open('models/loan_application_model_lr.pickle', 'rb') as f:
    clf_lr = pickle.load(f)

ss = StandardScaler()
genders_to_int = {'MALE':1,
                  'FEMALE':0}

married_to_int = {'YES':1,
                  'NO':0}

education_to_int = {'GRADUATED':1,
                  'NOT GRADUATED':0}

dependents_to_int = {'0':0,
                      '1':1,
                      '2':2,
                      '3+':3}

self_employment_to_int = {'YES':1,
                          'NO':0}                      

property_area_to_int = {'RURAL':0,
                        'SEMIRURAL':1, 
                        'URBAN':2}




app = flask.Flask(__name__, template_folder='templates')
@app.route('/')
def main():
    return (flask.render_template('Loan_Application.html'))

@app.route("/Loan_Application", methods=['GET', 'POST'])
def Loan_Application():
    
    if flask.request.method == 'GET':
        return (flask.render_template('Loan_Application.html'))
    
    if flask.request.method =='POST':
        
        genders_type = flask.request.form['genders_type']
        marital_status = flask.request.form['marital_status']
        dependents = flask.request.form['dependents']        
        education_status = flask.request.form['education_status']
        self_employment = flask.request.form['self_employment']
        applicantIncome = float(flask.request.form['applicantIncome'])
        coapplicantIncome = float(flask.request.form['coapplicantIncome'])
        loan_amnt = float(flask.request.form['loan_amnt'])
        term_d = int(flask.request.form['term_d'])
        credit_history = int(flask.request.form['credit_history'])
        property_area = flask.request.form['property_area']

        output_dict= dict()
        output_dict['Applicant Income'] = applicantIncome
        output_dict['Co-Applicant Income'] = coapplicantIncome
        output_dict['Loan Amount'] = loan_amnt
        output_dict['Loan Amount Term']=term_d
        output_dict['Credit History'] = credit_history
        output_dict['Gender'] = genders_type
        output_dict['Marital Status'] = marital_status
        output_dict['Education Level'] = education_status
        output_dict['No of Dependents'] = dependents
        output_dict['Self Employment'] = self_employment
        output_dict['Property Area'] = property_area
        


        x = np.zeros(21)
    
        x[0] = applicantIncome
        x[1] = coapplicantIncome
        x[2] = loan_amnt
        x[3] = term_d
        x[4] = credit_history

        print('------this is array data to predict-------')
        print('X = '+str(x))
        print('------------------------------------------')

        pred = clf_lr.predict([x])[0]
        
        if pred==1:
            res = '🎊🎊Congratulations! your Loan Application has been Approved!🎊🎊'
        else:
                res = '😔😔Unfortunatly your Loan Application has been Denied😔😔'
        

 
        return flask.render_template('Loan_Application.html', 
                                     original_input=output_dict,
                                     result=res,)
   
if __name__ == '__main__':
    app.run(debug=True)