# 2 DESENVOLVER UMA APLICACAO FLASK USANDO COOKIES

from flask import Flask, make_response, request

app = Flask(__name__)
cursos = ['Aeronautica', 'Aeroespacial', 'Civil', 'Computacao', 'Eletronica', 'Mecanica']
meus_cursos = ['', '', '', '', '', '']

@app.route('/set')
def setcookie():
    resposta = make_response('Ajustando um cookie para o exemplo')
    for i in range(6):
        resposta.set_cookie(str(i), cursos[i])
    return resposta

@app.route('/get')
def getcookie():
    for i in range(6):
        meus_cursos[i] = request.cookies.get(str(i))
    return 'O cursos do ITA sao: ' + str(meus_cursos)

if __name__ == '__main__':
    app.run(debug=True)