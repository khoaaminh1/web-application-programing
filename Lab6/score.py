from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def student():
    return render_template('score_form.html')

@app.route('/result', methods=['POST'])
def result():
    if request.method == 'POST':
        result = request.form
        return render_template('score_result.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
