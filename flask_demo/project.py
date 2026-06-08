from flask import Flask, request, render_template, redirect, url_for #importing Flask module from flask package

app = Flask(__name__) #this is a flask file and store it as app and refer to app to access it-- Build me a new website application and call it app

students_data = [
    {"id": 1, 
     "name": "Alice", 
     "course": "Computer Science"},
    {"id": 2, 
     "name": "Bob", 
     "course": "Data Science"}
] #list of dictionaries for each student

@app.get("/") #at the home page, get this info and run it
def home():
    return render_template("home.html") #allows for html to create a basic front-end to manipulate data, this is the home page

@app.get("/students") #get each student's data under the students router
def students():
    return render_template("students.html", students=students_data) #this returns the template, students.html and each student's data

@app.get("/students/new") #
def new_student_form():
    return render_template("new_student.html")

@app.post("/students/new") #creates a new student and appends that new student
def add_student():
    name = request.form["name"]
    course = request.form["course"]

    new_id = len(students_data) + 1

    students_data.append({
        "id": new_id,
        "name": name,
        "course": course
    })

    return redirect(url_for("students"))

@app.get("/students/edit/<int:id>") 
def edit_form(id):
    student = next((s for s in students_data if s["id"] == id), None)
    return render_template("edit_student.html", student=student)

@app.post("/students/edit/<int:id>") #edits a student
def update_student(id):
    for student in students_data:
        if student["id"] == id:
            student["name"] = request.form["name"]
            student["course"] = request.form["course"]

    return redirect(url_for("students"))

@app.post("/students/delete/<int:id>") #deltes a student
def delete_student(id):
    global students_data
    students_data = [s for s in students_data if s["id"] != id]
    return redirect(url_for("students"))

if __name__ == "__main__": #if this file is the main program we can use this to run the app with the debugger
    app.run(debug=True)