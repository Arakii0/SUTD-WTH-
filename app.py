import datetime
from flask import Flask, render_template,send_file
from fsocket import socketio

app = Flask(__name__)   
socketio.init_app(app)  

@app.route('/')
def hello():
    return render_template('first.html')

@app.route('/second.html')
def yes():
    return render_template('second.html')

@app.route('/third.html')
def dead():
    return render_template('third.html')

@app.route('/second copy.html')
def maybe():
    return render_template('second copy.html')

@app.route('/sign-to-txt.html')
def why():
    return render_template('sign-to-txt.html')

@app.route('/sign-to-txt2.html')
def nah():
    return render_template('sign-to-txt2.html')

@app.route('/speech-to-txt.html')
def can():
    return render_template('speech-to-txt.html')

@app.route('/speech-to-txt2.html')
def alive():
    return render_template('speech-to-txt2.html')

@app.route('/camera.html')
def banana():
    return render_template('camera.html')

@app.route('/speech-to-txt-final.html')
def goat():
    return render_template('speech-to-txt-final.html')

@app.route('/sign-to-txt-final.html')
def lime():
    return render_template('sign-to-txt-final.html')

@app.route("/microphone")
def micro():
    return render_template("microphone.html")

@app.route('/a')
def returnAudioFile():
    path_to_audio_file = "C:\\Users\\proje\\OneDrive\\Desktop\\Hackathon\\Translated.mp3" #audio from project dir
    return send_file(
       path_to_audio_file, 
        mimetype="audio/mp3", 
       as_attachment=True, 
       download_name="test.mp3")

app.run(debug=False)