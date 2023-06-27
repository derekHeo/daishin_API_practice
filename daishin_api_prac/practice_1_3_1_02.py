import pandas as pd
from pandas import DataFrame
from subDS import subMarketEye

if __name__ == "__main__":
    df_code = pd.read_csv('codeListSelection.csv')
    m_CodeList = df_code['종목코드']
    m_InfoList =[0,67, 70, 78]

    ### 자료가져오기
    data=subMarketEye(m_InfoList, m_CodeList)
    df = DataFrame(data, columns=['code', 'PER', 'EPS', '매출액증가율'])
    print(df)
    newDf = df.sort_values(by=['PER', 'EPS', 'code'], ascending=[True, False,  True])
    print(newDf)