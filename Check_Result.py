import mysql.connector as ms
mydb=ms.connect(host='localhost',user='root',password='Neeraj@123',database='employee')
mycur=mydb.cursor()
mycur.execute('Select stu_id from stu_result')
x=mycur.fetchall()
sid=int(input('Enter student id: '))
for k in x:
    if sid==k[0]:
        mycur.execute(f"select * from stu_result where stu_id={sid}")
        i=mycur.fetchone()
        print("-----------Mark's sheet-------------")
        print(f"| Student Name    :        {i[2]}.")
        print(f"| Student ID: {i[0]} &  Roll no : {i[1]}")
        print('----------Subject Marks-------------')
        print("| Mathematics     :           ",i[3]," |")
        print("| Physics         :           ",i[4]," |")
        print("| Chemistry       :           ",i[5]," |")
        print("| English         :           ",i[6]," |")
        print("| CPF             :           ",i[7]," |")
        print('-----------Your Result--------------')
        print("| Total           :           ",i[8],"|")
        print('--------------Grade-----------------')
        print(f"| {(i[8]/500)*100}%      ",i[10],"    ",i[9])
        print("------------------------------------")
        break
else:
    print("Id not Fond.")