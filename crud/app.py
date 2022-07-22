from flask import Flask,render_template,redirect,request,make_response,jsonify
from usersController import users
from userdb import db
from userdb import customers
app = Flask(__name__)

app.config ['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/crud'
app.config ['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
with app.app_context():
    db.create_all()

@app.route('/')
def hello_world():
    data = users.read()
    return render_template("index.html",data=data)
@app.route('/user',methods=['GET','POST'])
def customer():
    if request.method=='POST':
        users.add(request.form)
        return redirect('/')
    else:
        return make_response("Method Not Allowed" ,405)
@app.route('/user/update/<int:id>',methods=['GET','POST'])
def customer_update(id):
    if request.method=='POST':
        users.update(request.form,id)
        return redirect('/')
    else:
        data=customers.query.filter_by(id=id).first()
        return render_template('update_form.html',data=data)
@app.route('/user/delete/<string:id>',methods=['GET'])
def customer_delete(id):
    id=int(id)
    users.delete(id)
    return redirect('/')
@app.errorhandler(404)
def page_not_found(e):
    return make_response("Route Not Found",404)
if __name__=="__main__":
    app.run(debug=True,port=5000)