from flask import Flask, render_template, request, jsonify
from werkzeug.utils import secure_filename
import os
import json

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def detectbox(img_path):
    return {"status": "success", "boxes": [{"x": 10, "y": 20, "w": 50, "h": 50}]}

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        file = request.files.get('image')
        if file and file.filename.endswith(('.png', '.jpg', '.jpeg')):
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)
            result = detectbox(filepath)
            result = json.dumps(result, indent=4)
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
