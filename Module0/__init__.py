from flask import Flask
import markdown
import os
# ENV PYTHONPATH / test_project


app = Flask(__name__)
@app.route('/')
def index():
    return 'hello world'
#     with open(os.path.dirname(app.root_path) + '/sample.txt', 'r') as opened_file:
#         content = opened_file.read()
#         return markdown.markdown(content)
