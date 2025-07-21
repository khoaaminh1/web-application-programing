from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
from bson.objectid import ObjectId

app = Flask(__name__)

client = MongoClient("mongodb://localhost:27017/")
db = client["students_db"]
collection = db["students"]

# 3. HIỂN THỊ DANH SÁCH SINH VIÊN
@app.route('/')
def index():
    students = list(collection.find())
    return render_template('index.html', students=students)

# 2. THÊM SINH VIÊN
@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        student = {
            'name': request.form['name'],
            'age': int(request.form['age']),
            'gender': request.form['gender'],
            'major': request.form['major']
        }
        collection.insert_one(student)
        return redirect(url_for('index'))
    return render_template('form.html', student=None, action='Thêm')

# 4. SỬA SINH VIÊN
@app.route('/edit/<id>', methods=['GET', 'POST'])
def edit(id):
    student = collection.find_one({"_id": ObjectId(id)})
    if request.method == 'POST':
        collection.update_one({"_id": ObjectId(id)}, {"$set": {
            'name': request.form['name'],
            'age': int(request.form['age']),
            'gender': request.form['gender'],
            'major': request.form['major']
        }})
        return redirect(url_for('index'))
    return render_template('form.html', student=student, action='Sửa')

# 5. XÓA SINH VIÊN
@app.route('/delete/<id>')
def delete(id):
    collection.delete_one({"_id": ObjectId(id)})
    return redirect(url_for('index'))

# 6. TÌM KIẾM THEO TÊN CHÍNH XÁC
@app.route('/search', methods=['GET', 'POST'])
def search():
    students = []
    keyword = ""
    if request.method == 'POST':
        keyword = request.form['keyword']
        students = list(collection.find({'name': keyword}))
    return render_template('search.html', students=students, keyword=keyword)

# 7. TÌM KIẾM GẦN ĐÚNG THEO TÊN
@app.route('/search-fuzzy', methods=['GET', 'POST'])
def search_fuzzy():
    students = []
    keyword = ""
    if request.method == 'POST':
        keyword = request.form['keyword']
        students = list(collection.find({'name': {'$regex': keyword, '$options': 'i'}}))
    return render_template('search.html', students=students, keyword=keyword)

# 8. LỌC THEO NGÀNH
@app.route('/filter-major', methods=['GET'])
def filter_major():
    major = request.args.get('major')
    if major:
        students = list(collection.find({'major': major}))
    else:
        students = list(collection.find())
    majors = collection.distinct('major')
    return render_template('index.html', students=students, majors=majors, selected_major=major)

if __name__ == "__main__":
    app.run(debug=True)
