<!-- templates/index.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Upload WAV File</title>
</head>
<body>
    <h2>Upload a WAV file</h2>
    <form method="POST" action="/upload" enctype="multipart/form-data">
        <input type="file" name="wav_file" accept=".wav" required>
        <button type="submit">Upload</button>
    </form>
</body>
</html>
