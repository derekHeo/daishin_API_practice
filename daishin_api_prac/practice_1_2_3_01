from subDS import subCpSvr7254
from pandas import DataFrame

if __name__ == "__main__":

    code='A005930'        # 삼성전자 코드 
    fromDate = '20230131' # 요청 시작 날짜
    toDate = '20230626'   # 요청 마지막 날짜

    # ### 자료가져오기
    data=subCpSvr7254(code, fromDate, toDate)
    print(data)
    df=DataFrame(data,  columns=['일자', '개인', '외국인', '기관계', '금융투자', '보험', '투신', '은행', '기타금융', '연기금', '기타법인', '기타외인', '사모펀드', '국가지자체'])
    df.to_csv('subCpSvr7254.csv')