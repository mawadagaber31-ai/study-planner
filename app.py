from flask import Flask, redirect, render_template, request, session
from flask_session import Session
from cs50 import SQL
from werkzeug.security import check_password_hash, generate_password_hash

app = Flask(__name__)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

db = SQL("sqlite:///planner.db")


@app.route("/")
def index():
    if "user_id" not in session:
        return redirect("/login")

    tasks = db.execute(
        """
        SELECT * FROM tasks
        WHERE user_id = ?
        ORDER BY completed, deadline
        """,
        session["user_id"]
    )

    return render_template("index.html", tasks=tasks)

@app.route("/complete/<int:task_id>", methods=["POST"])
def complete_task(task_id):
    if "user_id" not in session:
        return redirect("/login")

    db.execute(
        """
        UPDATE tasks
        SET completed = 1
        WHERE id = ? AND user_id = ?
        """,
        task_id,
        session["user_id"]
    )

    return redirect("/")
@app.route("/delete/<int:task_id>", methods=["POST"])
def delete_task(task_id):
    if "user_id" not in session:
        return redirect("/login")

    db.execute(
        "DELETE FROM tasks WHERE id = ? AND user_id = ?",
        task_id,
        session["user_id"]
    )

    return redirect("/")
@app.route("/edit/<int:task_id>", methods=["GET", "POST"])
def edit_task(task_id):
    if "user_id" not in session:
        return redirect("/login")

    tasks = db.execute(
        "SELECT * FROM tasks WHERE id = ? AND user_id = ?",
        task_id,
        session["user_id"]
    )

    if not tasks:
        return redirect("/")

    task = tasks[0]

    if request.method == "POST":
        title = request.form.get("title")
        subject = request.form.get("subject")
        deadline = request.form.get("deadline")
        priority = request.form.get("priority")

        if not title:
            return "Please enter a task title"

        db.execute(
            """
            UPDATE tasks
            SET title = ?, subject = ?, deadline = ?, priority = ?
            WHERE id = ? AND user_id = ?
            """,
            title,
            subject,
            deadline,
            priority,
            task_id,
            session["user_id"]
        )

        return redirect("/")

    return render_template("edit.html", task=task)

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")

        if not username or not password or not confirmation:
            return "Please fill in all fields"

        if password != confirmation:
            return "Passwords do not match"

        existing_user = db.execute(
            "SELECT * FROM users WHERE username = ?",
            username
        )

        if existing_user:
            return "Username already exists"

        password_hash = generate_password_hash(password)

        db.execute(
            "INSERT INTO users (username, hash) VALUES (?, ?)",
            username,
            password_hash
        )

        return redirect("/login")

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    session.clear()

    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if not username or not password:
            return "Please enter username and password"

        users = db.execute(
            "SELECT * FROM users WHERE username = ?",
            username
        )

        if len(users) != 1 or not check_password_hash(users[0]["hash"], password):
            return "Invalid username or password"

        session["user_id"] = users[0]["id"]

        return redirect("/")

    return render_template("login.html")
@app.route("/logout")
def logout():
    session.clear()
    return redirect("/login")
@app.route("/add", methods=["GET", "POST"])
def add_task():
    if "user_id" not in session:
        return redirect("/login")

    if request.method == "POST":
        title = request.form.get("title")
        subject = request.form.get("subject")
        deadline = request.form.get("deadline")
        priority = request.form.get("priority")

        if not title:
            return "Please enter a task title"

        db.execute(
            """
            INSERT INTO tasks (user_id, title, subject, deadline, priority)
            VALUES (?, ?, ?, ?, ?)
            """,
            session["user_id"],
            title,
            subject,
            deadline,
            priority
        )

        return redirect("/")

    return render_template("add.html")
