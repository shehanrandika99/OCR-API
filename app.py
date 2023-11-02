from flask import Flask, request, render_template
import easyocr
from PIL import Image

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'file' not in request.files:
            return render_template('index.html', error="No file part")
        file = request.files['file']
        if file.filename == '':
            return render_template('index.html', error="No selected file")
        if file:
            image = Image.open(file)
            reader = easyocr.Reader(['en'])  # Set the languages you want to detect here
            results = reader.readtext(image)
            return render_template('index.html', results=results, filename=file.filename)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
