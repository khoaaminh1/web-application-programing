from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        
        username   = request.form.get('username')
        password   = request.form.get('password')
        gender     = request.form.get('gender')
        membership = request.form.get('membership')
        favcolor   = request.form.get('favcolor')
        correct    = 'correct' if request.form.get('correct') else 'not correct'

        
        return render_template('result.html',
                               username=username,
                               password=password,
                               gender=gender,
                               membership=membership,
                               favcolor=favcolor,
                               correct=correct)

   
    return render_template('exercise3.html')


if __name__ == '__main__':
    app.run(debug=True)
