# ###################################################################################################
# ### file Name: practice_1_2_2_01.py
# ###################################################################################################
from pandas import DataFrame
from subDS import subStockChart # 위에 작성한 subStockChart 불러오기

if __name__ == "__main__":
    ### 자료가져오기
    code ='A005930' # 삼성전자 종목코드 
    numHist =100 # 과거 100일치 데이터 
    df=subStockChart(code, numHist)
    print(df)