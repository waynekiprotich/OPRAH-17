from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', active_page='home')

@app.route('/message')
def message():
    return render_template('message.html', active_page='message')

if __name__ == '__main__':
    app.run(debug=True)