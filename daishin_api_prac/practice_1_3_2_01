import urllib.request
from bs4 import BeautifulSoup
code =['005930']    
for c in code:    
    url="http://comp.fnguide.com/SVO2/ASP/SVD_FinanceRatio.asp?pGB=1&gicode=A005930&cID=&MenuYn=Y&ReportGB=&NewMenuID=104&stkGb=701"     
    f = urllib.request.urlopen(url).read()
    soup=BeautifulSoup(f, 'html.parser')        
    cells = soup.find('tr', {'id': "p_grid1_1"}).find_all('td')
    for cell in cells:
        print (cell.string)