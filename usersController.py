from flask import jsonify
from userdb import customers
from userdb import db
class users:
    def read():
        return customers.query.all()
    def add(data):
        c = customers(first_name=data.get('fname'),last_name=data.get('lname'),email=data.get('email'),book_name=data.get('book_name'),book_isbn=data.get('book_isbn'),date_of_creation=data.get('date_of_creation'),no_of_stock=data.get('no_of_stock'))
        db.session.add(c)
        db.session.commit()
        return "True"
    def update(data,id):
        c = customers.query.filter_by(id=id).first()
        c.first_name=data.get('fname')
        c.last_name=data.get('lname')
        c.email=data.get('email')
        c.book_name=data.get('book_name')
        c.book_isbn=data.get('book_isbn')
        c.date_of_creation=data.get('date_of_creation')
        c.no_of_stock=data.get('no_of_stock')
        db.session.commit()
        return "True"
    def delete(id):
        customers.query.filter_by(id=id).delete()
        db.session.commit()
        return "True"
