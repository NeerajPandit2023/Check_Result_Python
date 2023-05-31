import mysql.connector as ms

# Update marks into database
def update_marks(sql):
    mydb=ms.connect(host='localhost',user='root',password='Neeraj@123',database='employee')
    mycur=mydb.cursor()
    mycur.execute(sql)
    mydb.commit()
    
# update
def fetch(sql,sid):
    mydb=ms.connect(host='localhost',user='root',password='Neeraj@123',database='employee')
    mycur=mydb.cursor()
    mycur.execute(sql)
    x=mycur.fetchone()
    x1=x[0]
    mycur.execute(f'select Total_marks from stu_result where stu_id={sid}')
    z=mycur.fetchone()
    z1=z[0]-x1
    return z1

def grade(per):
    p=(per/500)*100
    if p>=90:
        z='Outstanding'
    elif p>=80 and p<90:
        z='Excellent'
    elif p>=70 and p<80:
        z='Good'
    elif p>=60 and p<70:
        z='Average'
    else:
        z='Failed'
    return z

# check result
def result(p):
    per=(p/500)*100
    if per>=40:
        x='Passed'
    else:
        x='Failed'
    return x

def rename(sid,new_name):
    mydb=ms.connect(host='localhost',user='root',password='Neeraj@123',database='employee')
    mycur=mydb.cursor()
    mycur.execute(f"update stu_result set name='{new_name}' where stu_id={sid}")
    mydb.commit()
    return 'Sucessfully Updated'
    
    