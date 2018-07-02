# 3 DESENVOLVER UMA APLICACAO FLASK USANDO SESSOES

from flask import Flask, session, render_template

app = Flask(__name__)
app.secret_key = 'minha senha ultra secreta'

@app.route('/')
def index():
    session['user'] = 'Antonhy'
    return render_template('index03.html')

@app.run('/getsession')
def getsession():
    if 'user' in session:
        return session['user']
    return 'Not logged in'

@app.run('/dropsession')
def dropsession():
    session.pop('user', None)
    return 'Dropped!'

if __name__ == '__main__':
    app.run(debug=True)