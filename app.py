from flask import Flask


FRONT_FOLDER = 'front/dist'
app = Flask(__name__, template_folder=FRONT_FOLDER, static_folder=FRONT_FOLDER, static_url_path='')


