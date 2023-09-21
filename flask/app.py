from flask import Flask, request, send_from_directory
import os

app = Flask(__name__)

# Set the upload folder and allowed extensions for images
UPLOAD_FOLDER = '../images'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Check if the file extension is allowed
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    return "Welcome to the Image Upload and Download Service!"

@app.route('/upload', methods=['POST'])
def upload_file():
    # Check if any files were uploaded
    # breakpoint()
    if len(request.files) == 0:
        return "No files uploaded"

    # Iterate over the files in the request
    for key, file in request.files.items():
        # Check if the file has an allowed extension
        if file and allowed_file(file.filename):
            
            # Save the file with the unique filename
            filename = os.path.join(app.config['UPLOAD_FOLDER'], key)
            file.save(filename)

    return "Files uploaded successfully"

@app.route('/download/<filename>', methods=['GET'])
def download_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

@app.route('/download', methods=['GET'])
def download_file1():
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

@app.route('/test', methods=['GET'])
def test():
    return {'okay': 'okay'}

if __name__ == '__main__':
    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)
    app.run(debug=True)
