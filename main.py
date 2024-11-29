from flask import Flask, render_template, request
import requests

app = Flask(__name__)

def get_weather_data(city):
    API_KEY = 'affebb5ce8e04aaf18d18adcbf9f886f'
    idioma = 'es'
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&lang={idioma}'
    r = requests.get(url).json()
    return r

@app.route("/", methods=['GET', 'POST'])
def index():
    ciudad = ''
    temperatura = ''
    descripcion = ''
    icon = ''
    mostrar_card = False
    
    if request.method == 'POST':
        ciudad = request.form.get('txtCiudad') 
        print(ciudad) 
        if ciudad:
            data = get_weather_data(ciudad)  
            if data.get('cod') == 200:  
                temperatura = data.get('main').get('temp') - 273.15 
                descripcion = data.get('weather')[0].get('description')
                icon = data.get('weather')[0].get('icon')
                mostrar_card = True  
            else:
                ciudad = "Ciudad no encontrada"
                temperatura = ''
                descripcion = ''
                icon = ''
                mostrar_card = True 
    
    return render_template('index.html', ciudad=ciudad, temperatura=temperatura, descripcion=descripcion, icon=icon, mostrar_card=mostrar_card)

@app.route("/cv")
def cv():
    return render_template("cv.html")


if __name__ == "__main__":
    app.run(debug=True)