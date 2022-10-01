from aplicacion import app
from flask import Flask, render_template, render_template, request, redirect, session
import random # import the random module



@app.route('/')
def inicio():
    if 'numerorandom' in session:
        pass
    else:
        session['numerorandom']=random.randint(1, 100)
        session['estado']=[]
        session['color']=[]
        session['contador']=1
        session['ganador']=[]
    return render_template('index.html')

@app.route('/ad', methods=['POST'])
def adiviando():
    if session['contador'] == 5:
        return render_template ('perdiste.html')
    elif session['contador'] < 5:    
        intento= int(request.form["adivina"])
        if intento == session['numerorandom']:
            session['estado']='Adivinaste'
            # session['contador'] +=1
            return render_template ('ganaste.html')
        elif intento > session['numerorandom']:
            session['estado']='Muy alto'
            session['color']='bg-danger'
            session['contador'] +=1
        else:
            session['estado']='Muy bajo'
            session['color']='bg-danger'
            session['contador'] +=1
        return redirect('/')
    else:
        return render_template ('perdiste.html')

@app.route('/jugardenuevo', methods=['POST'])
def jugardenuevo():
    session.clear()
    return redirect('/')

@app.route('/ganadores', methods=['POST'])
def registrarGanador():
    session['ganador'].append(request.form['nombre'])
    session['ganador'].append(session['contador'])
    print(session['ganador'])
    return render_template('ganadores.html')
