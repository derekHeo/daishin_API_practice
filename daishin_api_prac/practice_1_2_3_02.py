from subDS import subCpSvrNew7224
from pandas import DataFrame

if __name__ == "__main__":

    m_Market ='B' # 'B':거래소, 'C':코스닥, 'D':선물, 'E':콜옵션, 'F':풋옵션
    numOrMoney ='1' # 1:수량 2:금액
    fromDate = '20230131' # 요청 시작 날짜
    toDate = '20230626'   # 요청 마지막 날짜

    # ### 자료가져오기
    data=subCpSvrNew7224(m_Market, numOrMoney, fromDate, toDate)
    df=DataFrame(data,  columns=['일자', '개인', '외국인', '기관계', '금융투자', '보험', '투신', '은행', '기타금융', '연기금', '기타법인',  '국가지자체', '사모펀드'])
    print(df)
    df.to_csv('subCpSvr7224.csv')