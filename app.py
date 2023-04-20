
from flask import Flask
import json
from flask import render_template, jsonify


app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/where')
def where():
    return render_template('where.html')


@app.route('/experience')
def experience():
    return render_template('experience.html')


@app.route('/expect')
def expect():
    return render_template('expect.html')


@app.route('/country')
def country():
    return render_template('country.html')


@app.route('/destination')
@app.route('/destination/')
@app.route('/destination/<name>')
def destination(name=None):
   
    with open('templates/dest/dest-'+ name +'.txt','r') as reader:
        #simply read the file and discard newlines
        dat = reader.read().replace('\n', '')
    
    #deserialize
    data = json.loads(dat)
    #make lists to send to template
    file_list = data["img-filenames"].split(",")
    todo_list = data["to-do-list"].split(",")
    tosee_list = data["to-see-list"].split(",")
    try:
        links_list = data["links"].split(",")
    except:
        links_list = []
    print(links_list)
    #description uses '||' to separate paragraphs
    descrip = data["description"].split("||")

    return render_template('destination.html', name=name, data=data, img_files=file_list, paras=descrip, todos=todo_list, tosees=tosee_list, links=links_list)


@app.route('/page/')
@app.route('/page/<pagenum>')
def page(pagenum=None):
    return render_template('page.html', page=pagenum)


@app.route('/test')
def test():
    return render_template('test.html')


# if __name__ == '__main__':
#     app.run(debug=True)
