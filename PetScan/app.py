from flask import Flask, render_template, request
from model import predict_image
from forms import UploadForm
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads'
app.secret_key = 'supersecretkey'

@app.route('/', methods=['GET', 'POST'])
def index():
    form = UploadForm()
    if form.validate_on_submit():
        image_file = request.files['image']
        image_path = os.path.join('static', 'uploads', image_file.filename)
        image_file.save(image_path)
        prediction = predict_image(image_path)
        return render_template('index.html', form=form, prediction=prediction, image_path=image_path)
    return render_template('index.html', form=form)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=12000, debug=True)
