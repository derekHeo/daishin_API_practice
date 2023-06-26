################################################################################################
### Stochasctic: fnStoch / Updated Date: 2015.11.22
################################################################################################
import pandas as pd

def fnStoch(m_Df, n=14): # price: 종가(시간 오름차순), n: 기간
    sz = len(m_Df['Close'])
    if sz < n:
        # show error message
        raise SystemExit('입력값이 기간보다 작음')
    tempSto_K=[]
    for i in range( sz):
        if i >= n-1:
            tempUp =m_Df['Close'][i] - min(m_Df['Low'][i-n+1:i+1])
            tempDown = max(m_Df['High'][i-n+1:i+1]) -  min(m_Df['Low'][i-n+1:i+1])
            tempSto_K.append( tempUp / tempDown )
        else:
            tempSto_K.append(0) #n보다 작은 초기값은 0 설정
    m_Df['Sto_K'] = pd.Series(tempSto_K,  index=m_Df.index)

    m_Df['Sto_D'] = pd.Series.rolling(m_Df['Sto_K'] , window = 3, center = False).mean()
    m_Df['Sto_SlowD'] = pd.Series.rolling(m_Df['Sto_D'] , window = 3, center = False).mean()

    return m_Df