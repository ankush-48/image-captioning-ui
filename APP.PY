from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
from PIL import Image
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads'

# Dummy model integration (Replace this with your actual model)
def generate_caption(image):
    return "This is a dummy caption. Replace this with your model output."

def preprocess_image(file_path):
    image = Image.open(file_path).convert("RGB")
    return image

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files['image']
        if file and file.filename:
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)
            image = preprocess_image(filepath)
            caption = generate_caption(image)
            return render_template('index.html', filename=filename, caption=caption)
    return render_template('index.html', filename=None, caption=None)

@app.route('/display/<filename>')
def display_image(filename):
    return redirect(url_for('static', filename='uploads/' + filename), code=301)

if __name__ == '__main__':
    app.run(debug=True)
