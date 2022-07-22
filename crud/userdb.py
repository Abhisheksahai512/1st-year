from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
class customers(db.Model):
   id = db.Column('id', db.Integer, primary_key = True)
   first_name = db.Column(db.String(100))
   last_name = db.Column(db.String(50))  
   email = db.Column(db.String(50))  
   book_name = db.Column(db.String(200))
   book_isbn = db.Column(db.String(20))
   date_of_creation = db.Column(db.Date())
   no_of_stock = db.Column(db.BigInteger())

def __init__(self, first_name, last_name,email,book_name,book_isbn,date_of_creation,no_of_stock):
   self.first_name = first_name
   self.last_name = last_name
   self.email = email
   self.book_name = book_name
   self.book_isbn = book_isbn
   self.date_of_creation = date_of_creation
   self.no_of_stock = no_of_stock