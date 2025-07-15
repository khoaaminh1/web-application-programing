from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
from bson.objectid import ObjectId

app = Flask(__name__)

# Kết nối MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["students_db"]
collection = db["students"]

@app.route("/")
def index():
    # Nếu có query name, dùng kết quả tìm kiếm; ngược lại hiển thị tất cả
    name = request.args.get("name")
    if name:
        students = list(collection.find({"name": name}))
    else:
        students = list(collection.find())
    return render_template("index.html", students=students)

@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        collection.insert_one({
            "name": request.form["name"],
            "age": int(request.form["age"]),
            "major": request.form["major"]
        })
        return redirect(url_for("index"))
    return render_template("form.html", student=None)

@app.route("/edit/<id>", methods=["GET", "POST"])
def edit(id):
    student = collection.find_one({"_id": ObjectId(id)})
    if request.method == "POST":
        collection.update_one(
            {"_id": ObjectId(id)},
            {"$set": {
                "name": request.form["name"],
                "age": int(request.form["age"]),
                "major": request.form["major"]
            }}
        )
        return redirect(url_for("index"))
    return render_template("form.html", student=student)

@app.route("/delete/<id>")
def delete(id):
    collection.delete_one({"_id": ObjectId(id)})
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)
