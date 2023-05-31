import mysql.connector as ms
import module_s
sid=int(input('Enter your id: '))
mydb=ms.connect(host='localhost',user='root',password='Neeraj@123',database='employee')
mycur=mydb.cursor()
mycur.execute(f'select stu_id from stu_result')
y=mycur.fetchall()
for i in y:
    if i[0]==sid:
        print("Would you like to change into stdent marks/name data.")
        x=input("Choose anyone:\n1. Marks 2. Name 3. Check result: ")
        if x=='1':
            ws=input('Choose anyone: 1. Math, 2.Physics, 3.Chemistry, 4.English, 5.CPF: ')
            if ws=='1':
                math=int(input('Enter marks of math: '))
                s1=f"select sub_math from stu_result where stu_id={sid}"
                z=module_s.fetch(s1,sid)
                sql1=f"update stu_result set sub_math={math} where stu_id={sid}"
                module_s.update_marks(sql1)
                um=math+z
                sql2=f"update stu_result set total_marks={um} where stu_id={sid}"
                module_s.update_marks(sql2)
                e1=module_s.grade(um)
                sql3=f"update stu_result set grade='{e1}' where stu_id={sid}"
                module_s.update_marks(sql3)
                e2=module_s.result(um)
                sql4=f"update stu_result set result='{e2}' where stu_id={sid}"
                module_s.update_marks(sql4)
            elif ws=='2':
                phy=int(input('Enter marks of Physics: '))
                s1=f"select sub_physics from stu_result where stu_id={sid}"
                z=module_s.fetch(s1,sid)
                sql1=f"update stu_result set sub_physics={phy} where stu_id={sid}"
                module_s.update_marks(sql1)
                um=phy+z
                sql2=f"update stu_result set total_marks={um} where stu_id={sid}"
                module_s.update_marks(sql2)
                e1=module_s.grade(um)
                sql3=f"update stu_result set grade='{e1}' where stu_id={sid}"
                module_s.update_marks(sql3)
                e2=module_s.result(um)
                sql4=f"update stu_result set result='{e2}' where stu_id={sid}"
                module_s.update_marks(sql4)

            elif ws=='3':
                che=int(input('Enter marks of Chemistry: '))
                s1=f"select sub_chemistry from stu_result where stu_id={sid}"
                z=module_s.fetch(s1,sid)
                sql1=f"update stu_result set sub_chemistry={che} where stu_id={sid}"
                module_s.update_marks(sql1)
                um=che+z
                sql2=f"update stu_result set total_marks={um} where stu_id={sid}"
                module_s.update_marks(sql2)
                e1=module_s.grade(um)
                sql3=f"update stu_result set grade='{e1}' where stu_id={sid}"
                module_s.update_marks(sql3)
                e2=module_s.result(um)
                sql4=f"update stu_result set result='{e2}' where stu_id={sid}"
                module_s.update_marks(sql4)
            elif ws=='4':
                eng=int(input('Enter marks of English: '))
                s1=f"select sub_english from stu_result where stu_id={sid}"
                z=module_s.fetch(s1,sid)
                sql1=f"update stu_result set sub_english={eng} where stu_id={sid}"
                module_s.update_marks(sql1)
                um=eng+z
                sql2=f"update stu_result set total_marks={um} where stu_id={sid}"
                module_s.update_marks(sql2)
                e1=module_s.grade(um)
                sql3=f"update stu_result set grade='{e1}' where stu_id={sid}"
                module_s.update_marks(sql3)
                e2=module_s.result(um)
                sql4=f"update stu_result set result='{e2}' where stu_id={sid}"
                module_s.update_marks(sql4)
            elif ws=='5':
                cpf=int(input('Enter marks of CPF: '))
                s1=f"select sub_cpf from stu_result where stu_id={sid}"
                z=module_s.fetch(s1,sid)
                sql1=f"update stu_result set sub_cpf={cpf} where stu_id={sid}"
                module_s.update_marks(sql1)
                um=cpf+z
                sql2=f"update stu_result set total_marks={um} where stu_id={sid}"
                module_s.update_marks(sql2)
                e1=module_s.grade(um)
                sql3=f"update stu_result set grade='{e1}' where stu_id={sid}"
                module_s.update_marks(sql3)
                e2=module_s.result(um)
                sql4=f"update stu_result set result='{e2}' where stu_id={sid}"
                module_s.update_marks(sql4)
            else:
                 print('Please choose any.')
        elif x=='2':
            new_name=input('Enter your new name: ')
            n=module_s.rename(sid,new_name)
            print(n)
        else:
            print('Invaild input')
        break
else:
    print('Worng id')