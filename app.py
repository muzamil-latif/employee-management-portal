from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():

    if request.method == "POST":

        name = request.form["name"]
        email = request.form["email"]
        department = request.form["department"]
        designation = request.form["designation"]

        conn = sqlite3.connect("employees.db")
        cursor = conn.cursor()

        cursor.execute(
            """
            INSERT INTO employees (name, email, department, designation)
            VALUES (?, ?, ?, ?)
            """,
            (name, email, department, designation)
        )

        conn.commit()
        conn.close()

    conn = sqlite3.connect("employees.db")
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM employees")
    total_employees = cursor.fetchone()[0]

    conn.close()

    return render_template(
        "index.html",
        total_employees=total_employees
    )


@app.route("/employees")
def employees():

    conn = sqlite3.connect("employees.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM employees")
    employees = cursor.fetchall()

    conn.close()

    return render_template(
        "employees.html",
        employees=employees
    )


@app.route("/delete/<int:id>")
def delete_employee(id):

    conn = sqlite3.connect("employees.db")
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM employees WHERE id = ?",
        (id,)
    )

    conn.commit()
    conn.close()

    return redirect("/employees")


@app.route("/about")
def about():

    return render_template("about.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)