from pandas import DataFrame
from subDS import subStockChart # 위에 작성한 subStockChart 불러오기
from fnStoch import fnStoch

if __name__ == "__main__":
    ### 자료가져오기
    code ='A005930' # 삼성전자 종목코드
    numHist =30 # 과거 100일치 데이터
    df=subStockChart(code, numHist)
    df_fnStoch = fnStoch(df)
    print(df_fnStoch)