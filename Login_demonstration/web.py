from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/user_info", methods=['GET', 'POST'])
def user_info():    
    if request.method == 'GET':
        print(request.args)
        user = request.args.get("user")
        pwd = request.args.get("pwd")
        gender = request.args.get("gender")
        hobbies = request.args.getlist("hobbies")
        occupation = request.args.get("occ")
        print(user,pwd ,gender ,hobbies ,occupation)
    else:
        print(request.form)
        user = request.form.get("user1")
        pwd = request.form.get("pwd1")
        occ = request.form.get("occ1")
        print(user,pwd,occ)

    return render_template("user.html")
@app.route("/register", methods=['GET'])
def register():
    return render_template("register.html")

@app.route("/login", methods=['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template("login.html")
    else:
        user = request.form.get("user")
        password = request.form.get('pwd')
        return "Welcome! User - " + user
    pass



if __name__ == "__main__":
    app.run()