from flask import Flask,request,jsonify

app=Flask(__name__)

#@app.route("/student",method=['GET','POST'])
@app.get("/student")
def student():
    data={
        "id":1,
        "name":"Alice",
        "course":"Python"
    }
    return jsonify(data)
if __name__ == "__main__":
    app.run(debug=True)