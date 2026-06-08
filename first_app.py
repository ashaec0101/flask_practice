from flask import Flask,request
app=Flask(__name__)

@app.route("/")
def home():
    return "Hello Flask"

@app.route("/about")
def about():
    return "About Page"

@app.route("/contact")
def some_method():
    return "Contact Page"
#url parameter -- path parameter
#/user/<name>
@app.route("/user/<name>")
def user_name(name):
    return f"Hello {name} !"
#Query string
# /user?name="Jasdhir"
@app.route("/user1")
def user1_name():
    name=request.args.get("name")
    job=request.args.get("job")
    return f"Hello {name}, who is a {job} !!!"
if __name__ =="__main__":
    app.run(debug=True)
