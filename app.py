import numpy as np
import pickle as pk
import streamlit as st
from sklearn.ensemble import RandomForestClassifier

# loading the saved model
load_md = pk.load(open('modelrf.sav', 'rb'))


# creating a function for Prediction
def HR_Employee_attrition_prediction(input_data):
      input_data_as_numpy_array = np.asarray(input_data)
      input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)
      prediction = load_md.predict(input_data_reshaped)
      print(prediction)
      if(prediction[0] == 0):
             print('The company has no Attrition')
      else:
          print('The company has Attrition')  
    
 

def main():
       
    # giving a title
    st.title('HR Employee Attrition Web App')
    
    
    # getting the input data from the user
    Age = st.text_input('Age of the Person')
    BusinessTravel = st.text_input('Travelling levels of employee')
    DailyRate = st.text_input('Amount of money spent by the employee')
    Department = st.text_input('The employee division of employee')
    DistanceFromHome = st.text_input('travelling distance of employee')
    Education = st.text_input('Highest Qualification of employee')
    EducationField	= st.text_input('domain of qualification')
    EmployeeCount	= st.text_input('total number of employees in an organization')
    EmployeeNumber	= st.text_input('unique identifier assigned to each individual employee')
    EnvironmentSatisfaction = st.text_input('fulfillment of their work environment.')
    Gender = st.text_input('Biological differences in human.')
    HourlyRate	= st.text_input('money paid for work performed within a specific hour')
    JobInvolvement = st.text_input('engaged and committed to their work.')
    JobLevel	= st.text_input('Ranking of employee.')
    JobRole	= st.text_input('specific set of responsibilities with particular position')
    JobSatisfaction = st.text_input('Satisfying the responsibilities')
    MaritalStatus = st.text_input('individuals legal relationship status')
    MonthlyIncome = st.text_input('total amount of money earned')
    MonthlyRate = st.text_input('the amount of money charged for services')
    NumCompaniesWorked = st.text_input('number of different companies employers has worked for over a specified period.')
    Over18 = st.text_input('Age limit')
    OverTime = st.text_input('extra working hours')
    PercentSalaryHike = st.text_input('increment of salary')
    PerformanceRating = st.text_input('measuring a perfromance of the employee')
    RelationshipSatisfaction = st.text_input(' evaluation of fulfillment they experience in their personal relationships')
    StandardHours = st.text_input('fixed hours')
    StockOptionLevel = st.text_input('compensation management within companies')
    TotalWorkingYears = st.text_input('actively working in their career up to a certain point in time')
    TrainingTimesLastYear = st.text_input('record of number of training sessions that an employee participated in during the last year or a specified period.')
    WorkLifeBalance = st.text_input('effectively managing the demands ')
    YearsAtCompany = st.text_input('record the total number of years that an individual has been employed')
    YearsInCurrentRole = st.text_input('record the total number of years that an individual has been in their current position')
    YearsSinceLastPromotion = st.text_input('record the total number of years that have passed since an individuals last promotion')
    YearsWithCurrManager = st.text_input('record the total number of years that an individual has been reporting to their current manager')
    
    # code for Prediction
    prediction = ''
    
    # creating a button for Prediction
    
    if st.button('Attrition Test Result'):
        prediction = Attrition_prediction([Age,BusinessTravel	,DailyRate	,Department,	DistanceFromHome	,Education	,EducationField	,EmployeeCount	,EmployeeNumber	,EnvironmentSatisfaction	,Gender	,HourlyRate	,JobInvolvement	,JobLevel	,JobRole	,JobSatisfaction	,MaritalStatus	,MonthlyIncome	,MonthlyRate	,NumCompaniesWorked	,Over18	,OverTime,	PercentSalaryHike,	PerformanceRating	,RelationshipSatisfaction,	StandardHours	,StockOptionLevel,	TotalWorkingYears	,TrainingTimesLastYear	,WorkLifeBalance	,YearsAtCompany	,YearsInCurrentRole,	YearsSinceLastPromotion	,YearsWithCurrManager])
        
        
    st.success(prediction)
    
    
if __name__ == '__main__':
    main()
    