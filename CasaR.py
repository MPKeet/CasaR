

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics

state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'District of Columbia': 'DC',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Northern Mariana Islands':'MP',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Palau': 'PW',
    'Pennsylvania': 'PA',
    'Puerto Rico': 'PR',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virgin Islands': 'VI',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}


def Ident():
    cit=input('Please enter city to analyze: ')
    state=input('Please enter the corresponding state: ')
    
    Rent(cit,state)

def Rent(cit,state):
    
    df=pd.read_csv('/Users/maxwellkeeter/Desktop/CompSci Resources/Python/Data/City_Zri_AllHomesPlusMultifamily.csv')
    
    Locate1(df,cit,state)
    
#Searches for appropriate city/state time data
def Locate1(df,cit,state):
    #converts long form state name to abbreviation to use df
    stabbrev=state_abbrev[state]
    
    for i, row in df.iterrows():
        if row['RegionName']== cit and row['State']==stabbrev:
            
            #2011 6 Month Average
            yr11m02=row['2011-02']
            yr11m04=row['2011-04']
            yr11m06=row['2011-06']
            yr11m08=row['2011-08']
            yr11m10=row['2011-10']
            yr11m12=row['2011-12']
            yr11avg=((yr11m02+yr11m04+yr11m06+
                      yr11m08+yr11m10+yr11m12)/6)
            
            #2012 6 Month Average
            yr12m02=row['2012-02']
            yr12m04=row['2012-04']
            yr12m06=row['2012-06']
            yr12m08=row['2012-08']
            yr12m10=row['2012-10']
            yr12m12=row['2012-12']
            yr12avg=((yr12m02+yr12m04+yr12m06+
                      yr12m08+yr12m10+yr12m12)/6)
            
            #2013 6 Month Average
            yr13m02=row['2013-02']
            yr13m04=row['2013-04']
            yr13m06=row['2013-06']
            yr13m08=row['2013-08']
            yr13m10=row['2013-10']
            yr13m12=row['2013-12']
            yr13avg=((yr13m02+yr13m04+yr13m06+
                      yr13m08+yr13m10+yr13m12)/6)
            
            #2014 6 Month Average
            yr14m02=row['2014-02']
            yr14m04=row['2014-04']
            yr14m06=row['2014-06']
            yr14m08=row['2014-08']
            yr14m10=row['2014-10']
            yr14m12=row['2014-12']
            yr14avg=((yr14m02+yr14m04+yr14m06+
                      yr14m08+yr14m10+yr14m12)/6)
            
            #2015 6 Month Average
            yr15m02=row['2015-02']
            yr15m04=row['2015-04']
            yr15m06=row['2015-06']
            yr15m08=row['2015-08']
            yr15m10=row['2015-10']
            yr15m12=row['2015-12']
            yr15avg=((yr15m02+yr15m04+yr15m06+
                      yr15m08+yr15m10+yr15m12)/6)
            
            #2016 6 Month Average
            yr16m02=row['2016-02']
            yr16m04=row['2016-04']
            yr16m06=row['2016-06']
            yr16m08=row['2016-08']
            yr16m10=row['2016-10']
            yr16m12=row['2016-12']
            yr16avg=((yr16m02+yr16m04+yr16m06+
                      yr16m08+yr16m10+yr16m12)/6)
            
            #2017 6 Month Average
            yr17m02=row['2017-02']
            yr17m04=row['2017-04']
            yr17m06=row['2017-06']
            yr17m08=row['2017-08']
            yr17m10=row['2017-10']
            yr17m12=row['2017-12']
            yr17avg=((yr17m02+yr17m04+yr17m06+
                      yr17m08+yr17m10+yr17m12)/6)
            
            #2018 6 Month Average
            yr18m02=row['2018-02']
            yr18m04=row['2018-04']
            yr18m06=row['2018-06']
            yr18m08=row['2018-08']
            yr18m10=row['2018-10']
            yr18m12=row['2018-12']
            yr18avg=((yr18m02+yr18m04+yr18m06+
                      yr18m08+yr18m10+yr18m12)/6)
            
            #2019 6 Month Average
            yr19m02=row['2019-02']
            yr19m04=row['2019-04']
            yr19m06=row['2019-06']
            yr19m08=row['2019-08']
            yr19m10=row['2019-10']
            yr19m12=row['2019-12']
            yr19avg=((yr19m02+yr19m04+yr19m06+
                      yr19m08+yr19m10+yr19m12)/6)
        
                  

            print('''\nCity: {}\nState: {}\n--------------------\nThe average rent price for the following years are:
                  \n2011: ${}\n2012: ${}\n2013: ${}\n2014: ${}\n2015: ${}\n2016: ${}\n2017: ${}\n2018: ${}\n2019: ${}'''.format(cit,
                  state,yr11avg,yr12avg,yr13avg,yr14avg,yr15avg,yr16avg,yr17avg,yr18avg,yr19avg))
            
            
            RENT=[yr11m02,yr11m04,yr11m06,yr11m08,yr11m10,yr11m12,yr12m02,yr12m04,yr12m06,yr12m08,yr12m10,yr12m12,yr13m02,yr13m04,yr13m06,yr13m08,yr13m10,yr13m12,
                  yr14m02,yr14m04,yr14m06,yr14m08,yr14m10,yr14m12,yr15m02,yr15m04,yr15m06,yr15m08,yr15m10,yr15m12,yr16m02,yr16m04,yr16m06,yr16m08,yr16m10,yr16m12,
                  yr17m02,yr17m04,yr17m06,yr17m08,yr17m10,yr17m12,yr18m02,yr18m04,yr18m06,yr18m08,yr18m10,yr18m12,yr19m02,yr19m04,yr19m06,yr19m08,yr19m10,yr19m12]
            
          
            
            
                  
            Prices(cit,state,RENT)
           
            
        else:
            pass
            



def Prices(cit,state,RENT):

    df=pd.read_csv('/Users/maxwellkeeter/Desktop/CompSci Resources/Python/Data/Sale_Prices_City.csv')
    
    Locate2(df,cit,state,RENT)
    
def Locate2(df,cit,state,RENT):
    
    
    
    for i, row in df.iterrows():
        if row['RegionName']== cit and row['StateName']==state:
            
            #2011 6 Month Average
            yr11m02=row['2011-02']
            yr11m04=row['2011-04']
            yr11m06=row['2011-06']
            yr11m08=row['2011-08']
            yr11m10=row['2011-10']
            yr11m12=row['2011-12']
            yr11avg=((yr11m02+yr11m04+yr11m06+
                      yr11m08+yr11m10+yr11m12)/6)
            
            #2012 6 Month Average
            yr12m02=row['2012-02']
            yr12m04=row['2012-04']
            yr12m06=row['2012-06']
            yr12m08=row['2012-08']
            yr12m10=row['2012-10']
            yr12m12=row['2012-12']
            yr12avg=((yr12m02+yr12m04+yr12m06+
                      yr12m08+yr12m10+yr12m12)/6)
            
            #2013 6 Month Average
            yr13m02=row['2013-02']
            yr13m04=row['2013-04']
            yr13m06=row['2013-06']
            yr13m08=row['2013-08']
            yr13m10=row['2013-10']
            yr13m12=row['2013-12']
            yr13avg=((yr13m02+yr13m04+yr13m06+
                      yr13m08+yr13m10+yr13m12)/6)
            
            #2014 6 Month Average
            yr14m02=row['2014-02']
            yr14m04=row['2014-04']
            yr14m06=row['2014-06']
            yr14m08=row['2014-08']
            yr14m10=row['2014-10']
            yr14m12=row['2014-12']
            yr14avg=((yr14m02+yr14m04+yr14m06+
                      yr14m08+yr14m10+yr14m12)/6)
            
            #2015 6 Month Average
            yr15m02=row['2015-02']
            yr15m04=row['2015-04']
            yr15m06=row['2015-06']
            yr15m08=row['2015-08']
            yr15m10=row['2015-10']
            yr15m12=row['2015-12']
            yr15avg=((yr15m02+yr15m04+yr15m06+
                      yr15m08+yr15m10+yr15m12)/6)
            
            #2016 6 Month Average
            yr16m02=row['2016-02']
            yr16m04=row['2016-04']
            yr16m06=row['2016-06']
            yr16m08=row['2016-08']
            yr16m10=row['2016-10']
            yr16m12=row['2016-12']
            yr16avg=((yr16m02+yr16m04+yr16m06+
                      yr16m08+yr16m10+yr16m12)/6)
            
            #2017 6 Month Average
            yr17m02=row['2017-02']
            yr17m04=row['2017-04']
            yr17m06=row['2017-06']
            yr17m08=row['2017-08']
            yr17m10=row['2017-10']
            yr17m12=row['2017-12']
            yr17avg=((yr17m02+yr17m04+yr17m06+
                      yr17m08+yr17m10+yr17m12)/6)
            
            #2018 6 Month Average
            yr18m02=row['2018-02']
            yr18m04=row['2018-04']
            yr18m06=row['2018-06']
            yr18m08=row['2018-08']
            yr18m10=row['2018-10']
            yr18m12=row['2018-12']
            yr18avg=((yr18m02+yr18m04+yr18m06+
                      yr18m08+yr18m10+yr18m12)/6)
            
            #2019 6 Month Average
            yr19m02=row['2019-02']
            yr19m04=row['2019-04']
            yr19m06=row['2019-06']
            yr19m08=row['2019-08']
            yr19m10=row['2019-10']
            yr19m12=row['2019-12']
            yr19avg=((yr19m02+yr19m04+yr19m06+
                      yr19m08+yr19m10+yr19m12)/6)
        
                  

            print('''\nCity: {}\nState: {}\n--------------------\nThe average sales price for the following years are:
                  \n2011: ${}\n2012: ${}\n2013: ${}\n2014: ${}\n2015: ${}\n2016: ${}\n2017: ${}\n2018: ${}\n2019: ${}\n\n'''.format(cit,
                  state,yr11avg,yr12avg,yr13avg,yr14avg,yr15avg,yr16avg,yr17avg,yr18avg,yr19avg))
            
            
            PRICES=[yr11m02,yr11m04,yr11m06,yr11m08,yr11m10,yr11m12,yr12m02,yr12m04,yr12m06,yr12m08,yr12m10,yr12m12,yr13m02,yr13m04,yr13m06,yr13m08,yr13m10,yr13m12,
                  yr14m02,yr14m04,yr14m06,yr14m08,yr14m10,yr14m12,yr15m02,yr15m04,yr15m06,yr15m08,yr15m10,yr15m12,yr16m02,yr16m04,yr16m06,yr16m08,yr16m10,yr16m12,
                  yr17m02,yr17m04,yr17m06,yr17m08,yr17m10,yr17m12,yr18m02,yr18m04,yr18m06,yr18m08,yr18m10,yr18m12,yr19m02,yr19m04,yr19m06,yr19m08,yr19m10,yr19m12]
            
           
                  
            Corr(RENT,PRICES)
           
            
        else:
            pass
        
        

        

def Corr(RENT,PRICES):
    
    zipper=list(zip(RENT,PRICES))
    
    df=pd.DataFrame(zipper, columns=['Rent','Prices'])
    
 
    print('Correlation Matrix:')
    corr_matrix=df.corr()
    print(corr_matrix['Rent'].sort_values(ascending=False))
    
    MVAR(df)
    
def MVAR(df):
    
    X=df.Prices.values.reshape(-1,1)
    y=df.Rent.values.reshape(-1,1)
    
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
    
    regressor = LinearRegression()  
    regressor.fit(X_train, y_train)
    a=regressor.intercept_
    b=regressor.coef_
    
    
    print('\n\nKey Metrics:')
    print('Intercept={}'.format(a))
    print('Coefficient={}\n\n'.format(b))
    
    y_pred = regressor.predict(X_test)
    
    df3 = pd.DataFrame({'Actual': y_test.flatten(), 'Predicted': y_pred.flatten()})
    print('Actual Vs Predicted Values in Random Sample:')
    print(df3)
    
    df1 = df3.head(25)
    df1.plot(kind='bar',figsize=(10,6))
    plt.grid(which='major', linestyle='-', linewidth='0.5', color='green')
    plt.grid(which='minor', linestyle=':', linewidth='0.5', color='black')
    plt.show()
    
    print('Mean Absolute Error:', metrics.mean_absolute_error(y_test, y_pred))  
    print('Mean Squared Error:', metrics.mean_squared_error(y_test, y_pred))  
    print('Root Mean Squared Error:', np.sqrt(metrics.mean_squared_error(y_test, y_pred)))
    
    #calc average 3 month % increase for housing price
    chng=df.Prices.pct_change()
    avg_chng=((chng.mean())*0.05)
    
    lst_val=df.Prices.iloc[-1]
    futprice=int(lst_val*(1+avg_chng))
   
    

    #Predict cost of rent by the end of three months
    RP=int(a+(futprice*b))
    
    print('\n\nPredicted rent 3 months in the future will average: ${}'.format(RP))
    
    Rent_Rate(RP)
    
def Rent_Rate(RP):
    #Adding in misc costs of owning
    electric=RP*0.052
    water=RP*0.023
    wifi=RP*0.02
    cln=RP*0.2
    
    r_total=RP+electric+water+wifi+cln
    #assumes average of 15 booked nights per month as per "become a host" on airbnb
    pos_r=(r_total/15)
    
    print('\n\nSuggested Nightly Rate: ${}'.format(pos_r))

    
    

Ident()
