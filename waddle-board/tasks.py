from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__, template_folder="templates")

todos = []

@app.route("/")
def index():
    return render_template("mainpage.html", todos=todos)

@app.route("/", methods=["POST"])
def add():
    todo = request.form['todo']
    priority = request.form['priority']

    todos.append({
        "task": todo, 
        "Inprogress":False, 
        "done":False,
        "priority": priority,
        })
    return redirect(url_for("mainpage"))

@app.route("/edit/<int:index>", methods=["GET", "POST"])
def edit(index):
    todo = todos[index]
    if request.method == "POST":
        todo['task'] = request.form['todo']
        todo['priority'] = request.form['proproty']
        return redirect(url_for("index"))
    else:
        return render_template("edit.html, todo=todo, index=index")
    
@app.route("/inprogress/<int:index>")
def inprogress(index):
    todos[index]["Inprogress"] = not todos[index]["Inprogress"]
    return redirect(url_for("index"))

@app.route("/check/<int:index>")
def done(index):
    todos[index]["done"] = not todos[index]["done"]
    return redirect(url_for("index"))

@app.route("/delete/<int:index>")
def delete(index):
    del todos[index]
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)
