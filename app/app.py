# app.py
from flask import Flask, render_template, request, send_file, send_from_directory
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
        with open(log_file, 'w') as file:
            # Run 'ls -a' and store both stdout and stderr to the log file
            #subprocess.call(['ls', '-a', directory], stdout=file, stderr=file)
            #subprocess.call(['resemble-enhance', wav_path, denoised_path, '--denoise_only', '--device', 'cpu'], stdout=file, stderr=file, shell=True)
            subprocess.call(['resemble-enhance /app/uploads /app/downloads --denoise_only --device cpu'], stdout=file, stderr=file, shell=True)
        
        # Use 'cat' to print the contents of the log file
        #subprocess.call(['cat', log_file], shell=True)
        #bash_command = f'resemble-enhance {wav_path} {denoised_path} --denoise_only --device cpu'
        #subprocess.call(['touch',output_wav])
        #subprocess.call(['ls /app/*'], shell=True)

        # Serve the converted file as a response
        return send_file(output_wav, as_attachment=True, mimetype="audio/wav", download_name="cleanAudio.wav")

@app.route('/download-log', methods=['GET'])
def download_log():
    # Serve the log.txt file for download
    log_file = '/app/log.txt'
    return send_from_directory(os.path.dirname(log_file), 
                               os.path.basename(log_file), 
                               as_attachment=True)


if __name__ == '__main__':
    app.run(debug=True)
