from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return redirect(url_for('square'))

@app.route('/square')
def square():
    num = request.args.get('num')
    if num:
        try:
            number = int(num)
            result = number ** 2
            return render_template('result.html', number=number, result=result)
        except ValueError:
            return "<p>Please enter a valid number.</p>"
    return render_template('math.html')

if __name__ == '__main__':
    app.run(debug=True)
