from flask import Flask
from flask import request
import re
from joblib import load

def cleaning(title):
    #Removing leading and tailing spaces
    title_cleaned = title.strip()
    title_cleaned = title_cleaned.split('-')
    title_cleaned = title_cleaned[0]
    # Making sure that all of the letters are lower
    title_cleaned = title_cleaned.lower()
    #Removing unuseful words
    words_to_remove = ['senior','junior','full','pre','mid','part','entry level','time','arabic','english'
                       ,'up','to','based',' and',' &',' in',' of']
    for word in words_to_remove:
        title_cleaned = title_cleaned.replace(word, '')
    #Keeping only words
    title_cleaned = re.sub(r"[^a-zA-Z ]","",title_cleaned)
    return title_cleaned

app = Flask(__name__)
model_in = load('SGDModel1.joblib')

@app.route("/")
def hello():
    if (request.args.get('jobtitle')):
        job_title = request.args.get('jobtitle')
        jobtitle_cleaned = cleaning(job_title)
        return list(model_in.predict([jobtitle_cleaned]))[0]
    else:
        return "Hello! enter jobtitle parameter"