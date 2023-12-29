import time
import sys

def typewriter_effect(text, speed=0.01):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)

# 定義圖書館書籍類別
class Library:
    # 初始化函式，設定書籍的屬性
    def __init__(self, book_name, book_id, publisher, author, publish_date,
                 lend_status, lend_date, return_deadline, book_place,
                 lend_person_name, stu_id, email):
        # 將傳入的參數設定為物件的屬性
        self.book_name = book_name
        self.book_id = book_id
        self.publisher = publisher
        self.author = author
        self.publish_date = publish_date
        self.lend_status = lend_status
        self.lend_date = lend_date
        self.return_deadline = return_deadline
        self.book_place = book_place
        self.lend_person_name = lend_person_name
        self.stu_id = stu_id
        self.email = email

    # 定義字串表示法，用於印出物件的屬性
    def __str__(self):
        return f"Book name: {self.book_name}\nBook ID: {self.book_id}\nPublisher: {self.publisher}\nAuthor: {self.author}\nPubilsh date: {self.publish_date}\nLend Status: {self.lend_status}\nLend date: {self.lend_date}\nReturn deadline: {self.return_deadline}\nBook place: {self.book_place}\nLend_person_name: {self.lend_person_name}\nStudent ID: {self.stu_id}\nEmail: {self.email}\n"

# 創建一個書籍物件 Book1
Book1 = Library("Python", 12345678910, "Guido van Rossum", "Guido van Rossum", "1989-12",
                "Lent", "1889-12-1", "20XX-XX-XX", "Everywhere on the internet",
                "Everyone", "4B1G0095", "4B1G0095@stust.edu.tw")

# 接收使用者輸入的書籍名稱
choice = input("Please Enter the book you want to search:")

# 判斷使用者輸入是否為 Book1
if choice == "Book1":
    # 印出 Book1 的屬性
    print(Book1)
    
    # 載入圖片
    from PIL import Image   

    img = Image.open("C:\\Users\\owner\\Downloads\\Python-logo-notext.svg.png")

    # 顯示圖片
    img.show()

else:
    print("Sorry, book not found!")

# 註解掉的部分，如果需要使用 Book2，可以取消註解並印出其屬性
"""
Book2 = Library("Python", 12345678910, "Guido van Rossum", "Guido van Rossum", "1989-12",
                "Lent", "1889-12-1", "20XX-XX-XX", "Everywhere on the internet",
                "Everyone", "4B1G0095", "4B1G0095@stust.edu.tw")
print(Book2.__dict__)
"""
