import pandas as pd
# pip install pandas
# pip install xlrd
from datetime import date

df = pd.read_excel('018290_20210701_104147.xls')

df = df[['일자','고가','종가','대상여부','목표가','손절가']]
df.columns = ['date','high','last','targetyn','targetp','cutp']
df = df.astype({'date':'string'}).sort_values(by=['date'],ascending=True)
df.dropna()

hitdate = []
for idx, row in df.iterrows() :
    if row[3] == 'Y' :
        hitdate.append(row[0])

founded = False
statslist = []

for idx, row in df.iterrows() :
    if  not founded and row[0] in hitdate :
        history = {}
        founded = True
        history['매수일'] = row[0]
        history['매수가'] = int(row[2]) 
        history['목표가'] = int(row[4]) 
        history['손절가'] = int(row[5]) 
        continue
    if founded :
       if  history['목표가'] <=  int(row[1]) :
            history['결과'] = '성공'
            history['청산일'] = row[0]
            tmpstr0 = str(history['매수일'])
            tmpstr1 = str(history['청산일'])
            d0 = date( int(tmpstr0[:4]), int(tmpstr0[4:6]), int(tmpstr0[6:])) 
            d1 = date( int(tmpstr1[:4]), int(tmpstr1[4:6]), int(tmpstr1[6:])) 
            delta = d1 - d0 #빼기
            history['보유기간'] = delta.days
            history['수익(%)'] = (history['목표가'] - history['매수가'])/history['매수가'] *100
            founded = False
            statslist.append(history)
       elif  history['손절가'] >   int(row[5]) :
            history['결과'] = '실패'
            history['청산일'] = row[0]
            history['손절가'] = int(row[5])
            tmpstr0 = str(history['매수일'])
            tmpstr1 = str(history['청산일'])
            d0 = date( int(tmpstr0[:4]), int(tmpstr0[4:6]), int(tmpstr0[6:])) 
            d1 = date( int(tmpstr1[:4]), int(tmpstr1[4:6]), int(tmpstr1[6:])) 
            delta = d1 - d0 #빼기
            history['보유기간'] = delta.days
            history['수익(%)'] = ( history['손절가'] - history['매수가'] )/history['매수가'] *100
            founded = False
            statslist.append(history)


totprofit =0.0
for history in statslist :
    print(f"{history['매수일']} 매수가:{history['매수가']:7,d} === 청산 => {history['청산일']}:{history['결과']} 보유기간: {history['보유기간']:2d} \
             수익 : {history['수익(%)']:5.2f}")
    totprofit += history['수익(%)']

print(f"==== 매매횟수:{len(statslist)} 총수익율(%) :{totprofit:5.2f}")
