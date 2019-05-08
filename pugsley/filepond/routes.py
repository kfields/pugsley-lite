import os
from flask import render_template, redirect, url_for, flash, request, jsonify
from werkzeug.utils import secure_filename
from werkzeug.urls import url_parse
from pugsley import app, db
from pugsley.jwt import encode_auth_token
from pugsley.filepond import bp
from pugsley.models.users import User
from pugsley.models.gallery import Image

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@bp.route('', methods=['POST'])
def upload_file():
    # check if the post request has the file part
    print(request.files)
    if 'filepond' not in request.files:
        raise Exception('No file part')
    file = request.files['filepond']
    # if user does not select file, browser also
    # submit an empty part without filename
    if file.filename == '':
        raise Exception('No selected file')
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['MEDIA'], filename))
        img = Image(
            title=filename,
            filename=filename
        )
        db.session.add(img)
        db.session.commit()
        return 'ok'
