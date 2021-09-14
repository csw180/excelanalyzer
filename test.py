from datetime import date


tmpstr0 = '20080818'
tmpstr1 = '20080926'
print(tmpstr0[:4])
print(tmpstr0[4:6])
print(tmpstr0[6:])
# d0 = date(2008, 8, 18) #date 객체1
# d1 = date(2008, 9, 26) #date 객체2

d0 = date( int(tmpstr0[:4]), int(tmpstr0[4:6]), int(tmpstr0[6:])) 
d1 = date( int(tmpstr1[:4]), int(tmpstr1[4:6]), int(tmpstr1[6:])) 
delta = d0 - d1 #빼기
print (delta.days) #날짜로 계산
