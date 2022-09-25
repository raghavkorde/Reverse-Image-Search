import os
from flask import Flask, render_template, request, redirect
from werkzeug.utils import secure_filename
from helpers import get_result
from flask_dropzone import Dropzone
app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))

app.config.update(
    UPLOADED_PATH = os.path.join(basedir,'uploads'),
    # Flask-Dropzone config:
    DROPZONE_ALLOWED_FILE_TYPE='image',
    DROPZONE_MAX_FILE_SIZE = 8,
    DROPZONE_MAX_FILES=1,
    DROPZONE_TIMEOUT = 5*60*1000,
    DROPZONE_UPLOAD_MULTIPLE=False,
    DROPZONE_REDIRECT_VIEW='fetch'
)
dropzone = Dropzone(app)


@app.route('/', methods=['POST', 'GET'])
def upload():
    if request.method == 'POST':
        file = request.files.get('file')
        filename = secure_filename(file.filename)
        PATH = os.path.join(app.config['UPLOADED_PATH'], filename)
        file.save(PATH)
        global UPLOADED_FILE_PATH
        UPLOADED_FILE_PATH = PATH 
        redirect('/fetch')
    return render_template('index.html')
     
@app.route('/fetch')
def fetch():
    try:
        return get_result(UPLOADED_FILE_PATH)
    except NameError:
        return render_template('error.html', message="Invalid file Type")


@app.route('/get_url', methods=['POST','GET'])
def get_url():
    if request.method == 'POST':
        url = request.form.get("url")
        return redirect(f"https://www.google.com/searchbyimage?image_url={url}")
    return redirect('/')

@app.route('/inst')
def inst():
    return render_template('instructions.html')

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)
