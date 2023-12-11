file='students.txt'
import os

def main():
    while True:
        menu()
        choice=int(input('请选择'))
        if choice in [0,1,2,3,4,5,6,7]:
            if choice==0:
                answer=input('您确定要退出系统吗?y/n')
                if answer=='y'or answer=='Y':
                    print('谢谢您的使用！！！')
                    break
                else:
                    continue
            elif choice==1:
                insert()
            elif choice==2:
                search()
            elif choice==3:
                delete()
            elif choice==4:
                modify()
            elif choice==5:
                sort()
            elif choice==6:
                total()
            elif choice==7:
                show()

def menu():                 
    print('===================学生信息管理系统===================')
    print('-----------------------功能菜单----------------------')
    print('\t\t1.录入学生信息')
    print('\t\t2.查找学生信息')
    print('\t\t3.删除学生信息')
    print('\t\t4.修改学生信息')
    print('\t\t5.对学生程序排序')
    print('\t\t6.统计学生总人数')
    print('\t\t7.显示所有的学生信息')
    print('\t\t0.退出')
    print('----------------------------------------------------')

def insert():
    students_list=[]
    while True:
        id=input('请输出学生id:')
        if not id:
            break
        name=input('请输入姓名:')
        if not name:
            break
        
        try:
            english=int(input('请输入英语成绩:'))
            python=int(input('请输入python成绩'))
            java=int(input('请输入java成绩:'))
        except:
            print('输入无效,不是整数类型,请重新输入')
            continue
        student={'id':id,'name':name,'english':english,'python':python,'java':java}
        students_list.append(student)
        answer=input('是否继续添加y/n\n')
        if answer=='y':  
            continue
        else:
            break

    save(students_list)
    print('学生信息录入完毕')

def save(lst):
    try:
        stu_txt=open(file,'a',encoding='utf-8')
    except:
        stu_txt=open(file,'w',encoding='utf-8')
    for item in lst:
        stu_txt.write(str(item)+'\n')
    stu_txt.close()

def search():
    pass

def delete():
    while True:
        student_id=input('请输入要删除的学生ID:')
        if student_id!='':
            if os.path.exists(file):
                with open(file,'read',encoding='utf-8') as File:
                    student_old=File.readlines()
            else:
                student_old=[]
            flag=False
            if student_old:
                with open(file,'w',encoding='utf-8') as wfile:
                    d={}
                    for item in student_old:
                        d=dict(eval(item))
                        if d['id']!=student_id:
                            wfile.write(str(d)+'\n')
                        else:
                            flag=True
                    if flag:
                        print(f'id为{student_id}的学生信息已被删除')
                    else:
                        print(f'没有找到id为{student_id}的学生信息')
            else:
                print('无学生信息')
                break
            show()
            answer=input('是否继续删除?y/n\n')
            if answer=='y':
                continue
            else:
                break
                 
def modify():
    pass

def sort():
    pass

def total():
    pass

def show():
    pass

if __name__=='__main__':
    main()
