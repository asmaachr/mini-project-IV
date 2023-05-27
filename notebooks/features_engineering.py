import pandas as pd
import numpy as np

def features_eng(df):

    
    ## family size:
    

    df['Married'] = df['Married'].apply(lambda x: 1 if x == 'Yes' else 0)
    df['family_size']= 1+df['Dependents'].replace('3+', 3).astype(int)+df['Married']
    df['family_size']= df['family_size'].astype(str)
    df['family_size']= df['family_size'].replace(['4', '5'], '+4')
   
    # ## total income
    df['total_income']=df['ApplicantIncome']+df['CoapplicantIncome']
    df['total_income']=np.log(df['total_income'])
    ## Loanamount
    df['LoanAmount']=np.log(df['LoanAmount'])
    ## Loan_Amount_Term
    df['Loan_Amount_Term']= df['Loan_Amount_Term'].astype(int)
    # ## Credit_History
    df['Credit_History']= df['Credit_History'].astype(str)
    df_eng=df.drop(['Loan_ID','Gender','Married','Dependents','ApplicantIncome','CoapplicantIncome'], axis=1)
    return df_eng