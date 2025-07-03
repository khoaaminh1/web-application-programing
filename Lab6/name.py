from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        user = request.form['name']
        return redirect(url_for('success', name=user))
    return render_template('name.html')

@app.route('/success/<name>')
def success(name):
    return f"welcome {name}"

if __name__ == '__main__':
    app.run(debug=True)
