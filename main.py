from flask import Flask, render_template, request
import pymongo
import flask
import functions as fun
import random

app = flask.Flask(__name__)

@app.route("/",methods = ['GET'])
def home():
    return render_template("home.html")

@app.route("/get_register",methods = ['GET'])
def get_register():
    return render_template("register.html")

@app.route("/register", methods = ['POST'])
def register():
    data = {"Name":request.form["name"],"Gmail":request.form["gmail"],"Phone no":request.form["phone"]}
    result = fun.bankuser(data)
    return render_template('register.html', display = str(result))


@app.route("/withdraw", methods = ["GET"])
def withdraw():
    return render_template("withdraw.html")

@app.route("/toWithdraw",methods = ["POST"])
def toWithdraw():
    data ={"accNo": request.form["accNo"],"withdraw_bal":request.form["withdraw_bal"]}
    resp = fun.withdrawl(data)
    return render_template("withdraw.html", display = str(resp))


@app.route("/deposit",methods = ["GET"])
def deposit():
    return render_template("deposit.html")

@app.route("/to_deposit",methods = ["POST"])
def to_deposit():
    data ={"accNo": request.form["accNo"],"deposit_amt":request.form["deposit_amt"]}
    resp = fun.deposit(data)
    return render_template("deposit.html",display = str(resp))


@app.route("/check_bal", methods = ["GET"])
def check_bal():
    return render_template("check_bal.html")

@app.route("/balance",methods = ["POST"])
def balance():
    data ={"accNo": request.form["accNo"]}
    resp = fun.bank_balance(data)
    return render_template("check_bal.html", display = str(resp))

if __name__ == "__main__":
    app.run(debug = True)


# @app.route("/send_otp",methods = ['GET'])
# def sendotp():
#     return render_template("send_otp.html")
#
# @app.route("/otpgen",methods = ['GET'])
# def gen_otp():
#     num = {"Phone no": request.form["phone"]}
#     otp = random.randint(123456, 999999)
#     msg = "Your otp is " + str(otp)
#     URL = f'https://www.fast2sms.com/dev/bulkV2?authorization=ncU8ARFdqzC06alm47fWMkNJYDKe5ZV9g3sxt2oHPvBEOywXLQyXrsgaY4tACJkMPOZKEuI9o2nxDB57&variables_values={otp}"&route=otp&numbers={num}'
#
#     r = requests.get(url=URL)
#
#     get_otp = {"otp":request.form["otp"]}



# @app.route("/ver_otp",methods = ['GET'])
# def verotp():
#     if otp == :
#         resp = "Account Register Successfully"
#         return resp
#     else:
#         resp ="Please Enter valid otp"
#         return resp
#     return render_template("send_otp.html",message =str(resp))
#     return render_template("ver_otp.html")

