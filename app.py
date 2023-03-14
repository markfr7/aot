
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
    j = """
    {
      "title": "Patagonia",
      "sub-head": "Visit the Land of the Untamed",
      "head-img-url": "http://blah.jpg",
      "to-do-list": "[Trek on the Patagonian Ice Field,Go Whitewater Rafting in Futaleufu,Hiking and wildlife watching in Torres del Paine,Ride the train to the end of the world in Tierra del Fuego,Take a sailing expedition on the Beagle Channel]",
      "to-see-list": "[Explore Perito Moreno Glacier,Cruise through the Marble Caves,Go Whale Watching,Go Glacier Trekking]",
      "img-path": "/img/patagonia/",
      "img-filenames": "caves.jpg,glacier.jpg,horses.jpg,mt-fritz-sunset.jpg,paddle.jpg,sea-birds.jpg",
      "description": "Patagonia is the land of the untamed. Left behind in time, inhabited mostly by rheas, guanacos and sheep inland and settled only by those who can find happiness in solitude and the vastness of its sights.  Frequently visited by whales and the Magel lan penguins by its coast\\\, wilderness is ubiquitous. Gauchos, working ranches and fishing lodges coexist with jagged glaciers completing the picture.  Its dramatic wind ridden landscape and bare steppe would mesmerize you. And its playful wind would intrigue you.\\n A far away land that has captivated explorers and scientist alike w ould unquestionably stun you as well  "
    }
    """
    #  return render_template('destination.html', name=name, data=jsonify(j))   json.loads(json_string)
    data = json.loads(j)
    f_list = data["img-filenames"]

    print(type(f_list))
    new_list = f_list.split(",")
    print(type(new_list))
    # for i in new_list:
    #     print(i)

    return render_template('destination.html', name=name, data=data, img_files=new_list)


@app.route('/page/')
@app.route('/page/<pagenum>')
def page(pagenum=None):
    return render_template('page.html', page=pagenum)


@app.route('/test')
def test():
    return render_template('test.html')


# if __name__ == '__main__':
#     app.run(debug=True)
