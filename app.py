
from flask import Flask,render_template,request,redirect
from flask_sqlalchemy import SQLAlchemy
import mysql.connector

app = Flask(__name__)
@app.route('/')
def student():
    return render_template('index.html')


@app.route('/result', methods=['POST','GET'])
def result():
    mydb=mysql.connector.connect(
        host='remotemysql.com',
        user='x66FMd3zjZ',
        password='JcDGVFeCaV',
        database='x66FMd3zjZ'
    )
    mycursor=mydb.cursor()
    if request.method == 'POST':
        result= request.form.to_dict()
        firstname=result['firstname']
        lastname=result['lastname']
        email=result['email']
        password=result['password']
        phonenumber=result['phonenumber']
        mycursor.execute("insert into reg(firstname,lastname,email,password,phonenumber)values(%s,%s,%s,%s,%s)",(firstname,lastname,email,password,phonenumber))
        mydb.commit()
        mycursor.close()
        return render_template('success.html',result=result)        
if __name__=="__main__":        
   app.run(debug=True)        


