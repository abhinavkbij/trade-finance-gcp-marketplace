import os
import urllib.request
from app import app
from flask import Flask, request, redirect, jsonify
from werkzeug.utils import secure_filename
import OCR
import Extract
import Align
ALLOWED_EXTENSIONS = set(['pdf'])

def allowed_file(filename):
	return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['POST'])
def upload_file():
	# check if the post request has the file part
	if 'file' not in request.files:
		resp = jsonify({'message' : 'No file part in the request'})
		resp.status_code = 400
		return resp
	file = request.files['file']
	if file.filename == '':
		resp = jsonify({'message' : 'No file selected for uploading'})
		resp.status_code = 400
		return resp
	if file and allowed_file(file.filename):
		filename = secure_filename(file.filename)
		file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
		file.save(file_path)
		resp = jsonify({'message' : 'File successfully uploaded'})
		dpi=300
		documentText, fname=OCR.Convert(file_path, dpi,str(1))
		data=Extract.Info(fname)
		data=Align.restructure(data)
		return str(data)
	else:
		resp = jsonify({'message' : 'Allowed file type is pdf'})
		resp.status_code = 400
		return resp

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int("4900"), debug=True)