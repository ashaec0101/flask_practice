from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)

students_data = [
    {"id": 1, "name": "Alice", "course": "Computer Science"},
    {"id": 2, "name": "Bob", "course": "Data Science"}
]

@app.get("/")
def home():
    return render_template("home.html")

@app.get("/students")
def students():
    return render_template("students.html", students=students_data)

@app.get("/students/new")
def new_student_form():
    return render_template("new_student.html")

@app.post("/students/new")
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

@app.post("/students/edit/<int:id>")
def update_student(id):
    for student in students_data:
        if student["id"] == id:
            student["name"] = request.form["name"]
            student["course"] = request.form["course"]

    return redirect(url_for("students"))

@app.post("/students/delete/<int:id>")
def delete_student(id):
    global students_data
    students_data = [s for s in students_data if s["id"] != id]
    return redirect(url_for("students"))

if __name__ == "__main__":
    app.run(debug=True)