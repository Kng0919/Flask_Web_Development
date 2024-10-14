from flask import Flask, render_template

app = Flask(__name__)

#Initial Page
@app.route('/')
def first_page():
    return render_template("home.html")



#Render template will search the target file within the folder names "templates"
@app.route("/template")
def show_temp():
    return render_template("index.html")

@app.route("/users")
def get_user():
    return render_template("users.html")

@app.route("/prompt")
def form_example():
    return render_template("forms.html")

if __name__ == "__main__":
    app.run()

