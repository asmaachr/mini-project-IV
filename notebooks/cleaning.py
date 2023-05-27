import pandas as pd
import numpy as np



def missing_value(df):

    # #missing values in gender we will consider the mode
    mode_gender = 'Male'
    # #Fill missing values in the gender with the mode values
    df['Gender'].fillna(mode_gender, inplace=True)

    #Fill missing values in Married: if coapplicantsincome>0 then 1 otherwise 0
    df['Married'].fillna(df['CoapplicantIncome'].apply(lambda x: 1 if x > 0 else 0), inplace=True)

    #Fill missing values for  dependents with 0
    df['Dependents'].fillna(0, inplace=True)

    #Fill missing values for  Self_Employed with No
    df['Self_Employed'].fillna('No', inplace=True)

    #Fill missing values for Loan Amount with median value
    median_value = 128
    # Fill missing values in the "Loan Amount" column with the median value
    df['LoanAmount'].fillna(median_value, inplace=True)

     #Fill missing values for Loan_Amount_Term with median value
    median_value2 = 360
    # Fill missing values in the "Loan Amount" column with the median value
    df['Loan_Amount_Term'].fillna(median_value2, inplace=True)

    #Fill missing values for  credit history with 0
    df['Credit_History'].fillna(0, inplace=True)

    return df