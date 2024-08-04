# app.py
from flask import Flask, render_template, request, send_file
import subprocess
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = './uploads'

@app.route('/')
def index():
    return render_template('index.html')
'''
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

        # Call the bash script to convert WAV to MP4
        wav_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        #mp4_filename = f"{os.path.splitext(filename)[0]}.mp4"
        #mp4_path = os.path.join(app.config['UPLOAD_FOLDER'], mp4_filename)
        denoised_path = "/tmp" # os.path.join(app.config['UPLOAD_FOLDER'], output)
        bash_command = f'resemble-enhance {wav_path} {denoised_path}'
        subprocess.call(bash_command, shell=True)

        # Serve the converted file as a response
        return send_file(denoised_path, as_attachment=True, attachment_filename=filename)
'''
if __name__ == '__main__':
    app.run(debug=True)
