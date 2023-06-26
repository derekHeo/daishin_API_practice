####################################################################################################
### file Name: practice_1_4_0_01.py
####################################################################################################

from pandas import DataFrame
from subDS import subStockChart # 위에 작성한 subStockChart 불러오기

if __name__ == "__main__":
    ### 자료가져오기
    code ='A005930' # 삼성전자 종목코드
    numHist =100 # 과거 100일치 데이터
    df=subStockChart(code, numHist)
    #print(df['Close'].mean(axis=0))
    #print(df['Close'].std(axis=0))


    # 최근 날짜가 가장 위에 있음.(***주의*** 최근 날짜가 처음인지 마지막인지 체크)
    prices = df['Close']
    stockReturn =prices.pct_change(-1)
    #stockReturn = prices / prices.shift(-1) - 1 ### 동일한 결과
    #stockReturn = prices[:-1] / prices[1:].values - 1 ### 동일한 결과

    print(stockReturn.describe())
    print('skeness: ', stockReturn.skew(axis=0))
    print('kurtosis: ', stockReturn.kurtosis(axis=0))

    print('autocorrelation: ', stockReturn.autocorr())