from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/<category>/<int:character_id>', methods=['GET'])
def show_character(category, character_id):
    if category == 'people':
        url = f'https://swapi.py4e.com/api/people/{character_id}/'
        
        response = requests.get(url)
        
        if response.status_code == 200:
            character_data = response.json()  
            return render_template('swapi.html', character_data=character_data)
    
    return render_template('swapi.html', character_data=None)


if __name__ == '__main__':
    app.run(debug=True)

