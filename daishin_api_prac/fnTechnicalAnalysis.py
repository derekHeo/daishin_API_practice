import pandas as pd

#Moving Average
def fnMA(m_Df, m_N, m_ColumnName='Close'):
    if m_ColumnName in m_Df.columns:
        MA= pd.Series(pd.rolling_mean(m_Df[m_ColumnName], m_N), name = 'MA_' + str(m_N))
        resultDf = m_Df.join(MA)
    else:
        raise("You didn't input a Column Name")
    return resultDf