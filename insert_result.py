import mysql.connector as ms
import module_s
mydb=ms.connect(host='localhost',user='root',password='Neeraj@123',database='employee')
mycurs=mydb.cursor()

sid=int(input('Enter student id: '))
roll=int(input('Enter student Roll no: '))
name=input('Enter student name: ')
math=int(input('Enter marks of math: '))
phy=int(input('Enter marks of physics: '))
che=int(input('Enter marks of chemistry: '))
eng=int(input('Enter marks of english: '))
cpf=int(input('Enter marks of CPF: '))
total=math+phy+che+eng+cpf
x=module_s.result(total)
z=module_s.grade(total)
sql=f"insert into stu_result values ({sid},{roll},'{name}',{math},{phy},{che},{eng},{cpf},{total},'{x}','{z}')"
mycurs.execute(sql)
mydb.commit()
print(mycurs.rowcount,"record inserted")