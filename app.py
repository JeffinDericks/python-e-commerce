from flask import Flask,render_template,redirect,url_for,request
import sqlite3 as sql
import random
app = Flask(__name__)

list_1 = []

@app.route('/')
def flipkart():
    return render_template ("flipkart.html")

@app.route('/rice')
def rice():
    con = sql.connect("user.db")
    cur = con.cursor()
    cur.execute("select * from count")
    fet = cur.fetchone()
    count1 = fet[0]
    count2 = fet[1]
    count3 = fet[2]
    return render_template ("rice.html", count1 = count1, count2 = count2,count3 = count3)


@app.route('/operate/<counter>/<operation>', methods=["GET", "POST"])
def operate(counter, operation):
    if request.method == "POST":
        con = sql.connect("user.db")
        cur = con.cursor()
        cur.execute("select * from count")
        fet = cur.fetchone()
        count1 = fet[0]
        count2 = fet[1]
        count3 = fet[2]

        if counter == '1':
            if operation == 'increment' and count1 >= 0:
                count1 += 1
            elif operation == 'decrement' and count1 > 0:
                count1 -= 1
        elif counter == '2':
            if operation == 'increment' and count2 >= 0:
                count2 += 1
            elif operation == 'decrement' and count2 > 0:
                count2 -= 1
        elif counter == '3':
            if operation == 'increment' and count3 >= 0:
                count3 += 1
            elif operation == 'decrement' and count3 > 0:
                count3 -= 1    

        cur.execute("update count set count1=?, count2=?, count3=?", (count1, count2,count3))
        con.commit()
        return redirect (url_for('rice'))
    

# @app.route('/otp', methods = ["GET","POST"])
# def otp():
#         return render_template ("otp.html")
    
    


# @app.route('/login', methods=["GET", "POST"])
# def login():
#     code = None  # Initialize code outside the conditional
    
#     if request.method == "POST" and request.form.get("btn1")== "submit1":
#         code = random.randint(1000, 9999)
#         otp = request.form.get("otp")
#     if request.method == "POST" and request.form.get("btn2")== "submit2":
#         if str(code) == otp:  # Convert code to string for comparison
#             return redirect(url_for('rice'))
    
#     return render_template("login.html", code=code)



@app.route('/login', methods=["GET", "POST"])
def login():
    code = "0808"  # Initialize code outside of the conditional
    otp = None   # Initialize otp outside of the conditional
   
    if request.method == "POST" and request.form.get("btn1") == "submit1":

        # code = random.randint(1,10)
        
        print(code)
    if request.method == "POST" and request.form.get("btn2") == "submit2":
        otp = request.form.get("otp")
        print(otp)
        if otp == str(code):  # Convert code to string for comparison
            print("success")
            return redirect(url_for('rice'))
    
    return render_template("login.html", code=code, otp=otp)








# @app.route('/login', methods=["GET", "POST"])
# def login():
#     if request.method == "POST" and request.form.get("btn1") == "submit1":
#         # Generate a random four-digit code
#         code = str(random.randint(1000, 9999))
#     if request.method == "POST" and request.form.get("btn2") == "submit2":
#         otp = request.form.get("otp")
#         if otp == code:
#             return redirect(url_for('flipkart'))  # Redirect to success page or do whatever is required

#     return render_template("login.html", code = code)



@app.route('/oil')
def oil():
    return render_template ("oil.html")

@app.route('/iphone')
def iphone():
    return render_template ("iphone.html")


if __name__ == "__main__":
    app.run(debug=True)





