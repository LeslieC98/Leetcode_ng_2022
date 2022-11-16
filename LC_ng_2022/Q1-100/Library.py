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
                'balance': 0
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
                    overdue_fee = overdue_days * 0.05  # 每逾期1天扣费0.05元
                    student['balance'] -= overdue_fee  # 从学生账户扣除逾期费用
                    print(f"书籍《{book_title}》已逾期{overdue_days}天，扣费：{overdue_fee:.2f}元")
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
print(f"{library.students['001']['name']}的账户余额：{library.students['001']['balance']:.2f}元")