class Account:
    def __init__(self, account_holder, balance = 0):
        self.balance = balance
        self.holder = account_holder

    def deposit(self, amount):
        self.balance = self.balance + amount
        return self.balance

    def withdraw(self, amount):
        if amount > self.balance:
            return 'Insufficient funds'
        self.balance = self.balance - amount
        return self.balance

    def __str__(self):
        return f"Acountholder: {self.holder} \f Balance: {self.balance}"

if __name__ == '__main__':
    tom_account = Account('tom',100)
    tom_account.deposit(170)
    print(tom_account)


class Student:
    def __init__(self, name, student_id,):
        self.name = name
        self.student_id = student_id
        self.grades = {"语文":0, "math":0, "English":0}

    def set_grade(self,course,grade):
        if course in self.grades:
            self.grades[course] = grade

    def print_grade(self):
        print(f'学生 {self.name} 学号 {self.student_id} 的成绩为：')
        for course in self.grades:
            print(f'{course}:{self.grades[course]} 分数')

if __name__ == '__main__':
    stu1 = Student("陈",856207)
    stu1.set_grade("语文",92)
    stu1.set_grade("math", 94)
    stu1.set_grade("English",100)
    print(stu1.print_grade())


class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def print_info(self):
        print(f'员工名字 {self.name} \n 员工id{self.id}')

class FullTime(Employee):
    def __init__(self, name, id ,montly_salary):
        super().__init__(name,id)
        self.montly_salary = montly_salary

    def calculate_montly_pay(self):
        return self.montly_salary

class PartTime(Employee):
    def __init__(self, name, id , daily_salary, work_days):
        super().__init__(name,id)
        self.daily_salary = daily_salary
        self.work_days = work_days

    def calculate_daily_pay(self):
        ##不能写成 def calculate_daily_pay(self,daily_salary, work_days)，因为方法中的参数不需要再被传入，因为已经在init中被定义了
        return self.daily_salary * self.work_days


if __name__ == '__main__':
    emp1 = PartTime("jojo", "10085", 300, 15)
    emp2 = FullTime("LEslie","10086",7000)
    print(emp1.calculate_daily_pay())
    print(emp2.calculate_montly_pay())
    emp2.print_info()

import datetime


class Library:
    def __init__(self):
        self.students = {}
        self.books = {}

    def add_student(self, student_id, student_name):
        if student_id not in self.students:
            self.students[student_id] = {
                'name': student_name,
                'borrowed_books': {},
                'balance': 0  # 添加学生账户余额
            }

    def add_book(self, book_title):
        if book_title not in self.books:
            self.books[book_title] = {
                'available': 1,
            }

    def borrow_book(self, student_id, book_title, days):
        if student_id in self.students and book_title in self.books:
            student = self.students[student_id]
            book = self.books[book_title]
            if book['available'] > 0 and len(student['borrowed_books']) < 5:
                due_date = datetime.date.today() + datetime.timedelta(days=days)
                student['borrowed_books'][book_title] = due_date
                book['available'] -= 1
                print(f"{student['name']}借阅了《{book_title}》，归还日期：{due_date}")
            else:
                print("无法借阅更多书籍或已借阅该书")

    def return_book(self, student_id, book_title):
        if student_id in self.students and book_title in self.books:
            student = self.students[student_id]
            if book_title in student['borrowed_books']:
                due_date = student['borrowed_books'][book_title]
                today = datetime.date.today()
                if today > due_date:
                    overdue_days = (today - due_date).days
                    overdue_fee = overdue_days // 30 * 3
                    student['balance'] += overdue_fee  # 更新学生账户余额
                    print(f"书籍《{book_title}》已逾期{overdue_days}天，扣费：{overdue_fee}元")
                student['borrowed_books'].pop(book_title)
                self.books[book_title]['available'] += 1
                print(f"{student['name']}归还了《{book_title}》")
            else:
                print("未借阅该书")
        else:
            print("无效的学生或书籍信息")


# 创建图书管理系统
library = Library()

# 添加学生和书籍
library.add_student("001", "学生1")
library.add_book("Python编程指南")
library.add_book("数据结构与算法")
library.add_book("计算机网络基础")

# 学生借书操作
library.borrow_book("001", "Python编程指南", 30)

# 模拟逾期
import datetime

today = datetime.date.today()
overdue_date = today - datetime.timedelta(days=45)  # 模拟45天的逾期
library.students["001"]["borrowed_books"]["Python编程指南"] = overdue_date

# 学生归还逾期的图书
library.return_book("001", "Python编程指南")

# 显示学生账户余额
print(f"{library.students['001']['name']}的账户余额：{library.students['001']['balance']}元")