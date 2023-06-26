import pandas as pd
import numpy as np
#Moving Average
def fnMA(m_Df, m_N1, m_N2, m_ColumnName='Close'):
    if m_ColumnName in m_Df.columns:
        #window는 몇개씩 연산할지이다.
        MA1= pd.Series.rolling(m_Df[m_ColumnName],window=20, center=False).mean()
        m_Df = m_Df.join(MA1)
        MA2= pd.Series.rolling(m_Df[m_ColumnName],window=20, center=False).mean()
        m_Df = m_Df.join(MA2)

        m_Df['SignalMA']  =m_Df['MA1'] - m_Df['MA2']
    else:
        raise("You didn't input a Column Name")
    return m_Df

def fnSortDateTime(m_Df):
    if 'Date' in m_Df.columns:
        if 'Time' in m_Df.columns:
            df=m_Df.sort(['Date', 'Time'], ascending=[True, True])
            #m_Df=m_Df.sort(['Date', 'Time'], ascending=[True, True])
        else:
            df=m_Df.sort(['Date'], ascending=[True])
            #m_Df=m_Df.sort(['Date'], ascending=[True])
        resultDf=df.reset_index(drop=True)
        #m_Df=m_Df.reset_index(drop=True)
    else:
        raise("You dodn't have the 'Date' column ")
    return resultDf
    #return m_Df

####################################################################################################
### file Name: fnTechnicalAnalysis.py
#####################################################################################################

#Relative Strength Index  
def fnRSI(m_Df, m_N):

    U = np.where(m_Df.diff(1) > 0, m_Df.diff(1), 0)
    D = np.where(m_Df.diff(1) < 0, m_Df.diff(1) *(-1), 0)

    AU = pd.DataFrame(U).rolling( window=m_N, min_periods=m_N).mean()
    AD = pd.DataFrame(D).rolling( window=m_N, min_periods=m_N).mean()
    RSI = AU.div(AD+AU) *100
    return RSI