import sqlite3
import xlsxwriter

workbook = xlsxwriter.Workbook('Y:\Manish_Choudhary\Assignment\Assignment-9\Problem-1\IMDB_Top_250_Movies.xlsx')
worksheet = workbook.add_worksheet("IMDB_Top_250_Movies")

con=sqlite3.connect('Y:\Manish_Choudhary\Assignment\Assignment-9\Problem-1\IMDB_Data.db')
cur=con.cursor()

header=['Rank','Title','Rating','Release_Date','Genre','Runtime','Director','Star','Country_Of_Origin','Language','Budget']
col=0
for item in header:
    worksheet.write(0,col,item)
    col+=1
row=1
for item in cur.execute('select * from IMDB_Table'):
    con.commit()
    col=0
    for ele in item:
        worksheet.write(row,col,ele)
        col+=1
    row+=1
con.close()
workbook.close()