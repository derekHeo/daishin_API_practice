from pandas import DataFrame
from subDS import subStockChart # 위에 작성한 subStockChart 불러오기

if __name__ == "__main__":
    # ### 자료가져오기
    code ='A005380' # 현대차 종목코드 
    numHist =100 # 과거 100일치 데이터 
    df=subStockChart(code, numHist)
    #df.to_csv('stockData.csv') # csv파일 형태로 저장하기 
    df.to_csv('codeList.csv', encoding="utf-8")
    #df.to_csv('stockData.txt') # text 파일 형태로 저장하기         
    #print(df)