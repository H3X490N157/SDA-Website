from flask import Flask, render_template
from flask_mail import Mail, Message

app = Flask(__name__)

mail = Mail(app)


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/skills')
def skills():
    return render_template('skills.html')


@app.route('/education')
def education():
    return render_template('education.html')


@app.route('/experience')
def experience():
    return render_template('experience.html')






if __name__ == '__main__':
    app.run(debug=True)
