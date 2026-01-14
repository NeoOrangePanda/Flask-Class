from flask import Flask, render_template, request

app = Flask(__name__)

ALLOWED_EXTENSTIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

@app.route('/')
def index():
    return render_template('index.html')

def allowed_file(filename: str):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSTIONS

@app.route('/uploader', methods=['GET', 'POST'])
def uploader():
    if request.method == 'POST':
        if 'file' not in request.files:
            return render_template('index.html', msg='No file part')
        file = request.files['file']

        if file.filename == '':
            return render_template('index.html', msg='No file selected')
        
        if file and allowed_file(file.filename):
            file.save(file.filename)
            return render_template('index.html', msg='File uploaded successfully!')
        else:
            return render_template('index.html', msg=f'Not Supported Extension. Allowed Extensions {ALLOWED_EXTENSTIONS}')
        
if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)