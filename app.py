from flask import Flask, render_template, request
import requests

app = Flask (__name__)

@app.route('/', methods = ["POST", "GET"])
def home():
    if request.method == 'POST':
        breed = request.form['breed']
        url = f'https://dog.ceo/api/breed/{breed}/images'
        r = requests.get(url)
        pics = r.json()['message']
        return render_template('dogs.html', breed = breed, pics = pics)
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug = True, port = 4000)