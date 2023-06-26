from subDS import subCpStockCode
from pandas import DataFrame

if __name__ == "__main__":
    data = subCpStockCode()
    # print(data)     # A:시장전체 선택
    df=DataFrame(data,  columns=['종목코드', '종목명', 'fullCode'])
    print(df)
    df.to_csv('codeList.csv')