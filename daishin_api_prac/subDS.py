from pandas import DataFrame
import win32com.client
import win32com
import time

# ### stockChart ###
def subStockChart(m_Code, m_NumHist):                                   ### 1
# def subStockChart(m_Code, m_FromDate, m_ToDate):                           ### 2
    stockChart = win32com.client.Dispatch("CpSysDib.StockChart")
    stockChart.SetInputValue(0, m_Code)    # 종목 코드
    stockChart.SetInputValue(1, ord('2'))    # 요청 구분 (개수로 요청)  ### 1
    # stockChart.SetInputValue(1, ord('1'))    # 요청 구분 (날짜로 요청)      ### 2
    # stockChart.SetInputValue(2, m_ToDate)  # 시작일자                       ### 2
    # stockChart.SetInputValue(3, m_FromDate)    # 끝일자                     ### 2
    stockChart.SetInputValue(4, m_NumHist)     # 요청개수                ### 1
    stockChart.SetInputValue(5, [0,2,3,4,5]) # 날짜, 시가, 고가, 저가, 종가
    stockChart.SetInputValue(6, ord('D'))    # 차트 구분 (일)

    # ## 데이터 호출
    stockChart.BlockRequest()
    num = stockChart.GetHeaderValue(3)
    data=[]
    for i in range(num):
        tempData ={}
        tempData['Date']=(stockChart.GetDataValue(0,i))
        tempData['Open']=float(format(stockChart.GetDataValue(1,i), '.2f')) # 선물값이 오류수정 
        tempData['High']=float(format(stockChart.GetDataValue(2,i), '.2f'))
        tempData['Low']=float(format(stockChart.GetDataValue(3,i), '.2f'))
        tempData['Close']=float(format(stockChart.GetDataValue(4,i), '.2f'))
        data.append(tempData)

    # ## dataframe으로 전환    
    resultDf = DataFrame(data, columns=['Date', 'Open', 'High', 'Low', 'Close'])
    return resultDf

# ### CpSvr7254  투자주체별현황을 일별/기간별, 순매수/매매비중을 일자별로 확인할수 있습니다
def subCpSvr7254(m_code, m_FromDate, m_ToDate):
   # ## 대신 API 세팅
    cpSvr7254 = win32com.client.Dispatch("CpSysDib.CpSvr7254")
    cpSvr7254.SetInputValue(0, m_code)       # 종목코드
    cpSvr7254.SetInputValue(1, '0')          # 기간선택 0:기간선택, 1:1개월, ... , 4:6개월
    cpSvr7254.SetInputValue(2, m_FromDate)  # 시작일자
    cpSvr7254.SetInputValue(3, m_ToDate)    # 끝일자
    cpSvr7254.SetInputValue(4, '0')         # 0:순매수 1:비중
    cpSvr7254.SetInputValue(5, '0')         # 투자자
    cpSvr7254.BlockRequest()

    numData=cpSvr7254.GetHeaderValue(1)
    # print(numData)
    data=[]
    for ixRow in range(numData):
        tempData=[]
        for ixCol in range(14):
            tempData.append(cpSvr7254.GetDataValue(ixCol, ixRow))
        data.append(tempData)

    # 연속 수행
    while cpSvr7254.Continue:
        cpSvr7254.BlockRequest()
        numData = cpSvr7254.GetHeaderValue(1)
        # print(numData)
        for ixRow in range(numData):
            tempData=[]
            for ixCol in range(14):
                tempData.append(cpSvr7254.GetDataValue(ixCol, ixRow))
            data.append(tempData)
        time.sleep(0.1)

    return data

# ### CpSvrNew7224  투자자(기관,외국인,개인 등등) 들의 일일 매매 동향데이터(매수,매도,순매수)를 요청하고 수신합니다
def subCpSvrNew7224(m_Market, m_NumOrMoney, m_FromDate, m_ToDate):
   ## 대신 api 세팅
    obj = win32com.client.Dispatch("cpsysdib.CpSvrNew7224")
    obj.SetInputValue(0, ord('1'))          # 1:일반, 2: 챠트
    obj.SetInputValue(1, ord(m_Market))     # A:시장전체 선택
    obj.SetInputValue(2, '0')          # 0:투자자전체
    obj.SetInputValue(3,  ord('1'))          # 1:기간
    obj.SetInputValue(4,  ord(m_NumOrMoney)) # 1:계약 2:금액
    obj.SetInputValue(5,  '0')         # 1:기간선택
    obj.SetInputValue(6, m_FromDate)  # 시작일자
    obj.SetInputValue(7, m_ToDate)    # 최종일자
    obj.SetInputValue(8,  ord('1'))        # 1:순매수
    obj.BlockRequest()

    numData=obj.GetHeaderValue(5)
    data=[]
    for ixRow in range(numData):
        tempdata=[]
        for ixCol in range(13):
            tempdata.append(obj.GetDataValue(ixCol, ixRow))
        data.append(tempdata)

    while obj.Continue:
        obj.BlockRequest()
        numData = obj.GetHeaderValue(5)
        for ixRow in range(numData):
            tempdata=[]
            for ixCol in range(13):
                tempdata.append(obj.GetDataValue(ixCol, ixRow))
            data.append(tempdata)
        time.sleep(0.1)

    return data

# ### MarketEye 주식,지수,선물/옵션 등의 여러종목의 필요 항목들을 한번에 수신합니다.
def subMarketEye(m_InfoList, m_CodeList):
    # ## 대신 api 세팅
    obj = win32com.client.Dispatch("cpsysdib.MarketEye")
    obj.SetInputValue(0, m_InfoList)     # A:시장전체 선택
    obj.SetInputValue(1, m_CodeList)      # 종목
    obj.BlockRequest()

    numField=obj.GetHeaderValue(0)        # 필드수
    numData=obj.GetHeaderValue(2)         # 데이터수(종목수)
    # nameField=obj.GetHeaderValue(1)
    # print('필드명:', nameField)
    data=[]
    for ixRow in range(numData):
        tempdata=[]
        for ixCol in range(numField):
            tempdata.append(obj.GetDataValue(ixCol, ixRow))
        data.append(tempdata)
    return data

#CYBOS에서 사용되는 주식코드 조회 작업을 함.
def subCpStockCode():
   # ## 대신 api 세팅
    obj = win32com.client.Dispatch("CpUtil.CpStockCode")
    numData =   obj.GetCount()
    data=[]
    for ix in range(numData):
        tempData=[]
        tempData.append(obj.GetData(0,ix))
        tempData.append(obj.GetData(1,ix))
        tempData.append(obj.GetData(2,ix))
        data.append(tempData)
    return data