# app.py
from flask import Flask, render_template, request, send_file
import subprocess
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = '/app/uploads'
app.config['DOWNLOAD_FOLDER'] = '/app/downloads'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    # Check if the POST request has the file part
    if 'wav_file' not in request.files:
        return "No file part"
    
    file = request.files['wav_file']
    
    # If the user does not select a file, browser also submits an empty part without filename
    if file.filename == '':
        return 'No selected file'
    
    # Save the uploaded file
    if file:
        filename = file.filename
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        wav_path = app.config['UPLOAD_FOLDER']
        denoised_path = app.config['DOWNLOAD_FOLDER'] #"/tmp" # os.path.join(app.config['UPLOAD_FOLDER'], output)
        output_wav = os.path.join(denoised_path, filename)
        log_file = '/app/log.txt'
        #bash_command = f'resemble-enhance {wav_path} {denoised_path} --denoise_only --device cpu'
        subprocess.call(['resemble-enhance', wav_path, denoised_path, '--denoise_only', '--device', 'cpu'], stdout=open(log_file, 'w'))
        #subprocess.call(['touch',output_wav])
        print(subprocess.call(['ls /app/*/'], shell=True))
        subprocess.call(['cat', log_file])

        # Serve the converted file as a response
        return send_file(output_wav, as_attachment=True, mimetype="audio/wav", download_name="cleanAudio.wav")

if __name__ == '__main__':
    app.run(debug=True)
