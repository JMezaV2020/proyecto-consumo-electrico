from flask import Flask, render_template
import json

app = Flask(__name__)

def procesar_datos():
    with open('datos.json', encoding='utf-8') as f:
        data = json.load(f)
    processed_data = []
    for item in data:
        for key, value in item.items():
            fields = value.split(';')
            processed_data.append({
                'anio': fields[0],
                'mes': fields[1],
                'region': fields[2],
                'comuna': fields[3],
                'tipo_clientes': fields[4],
                'tarifa': fields[5],
                'clientes_facturados': fields[6],
                'e1_kwh': fields[7],
                'e2_kwh': fields[8],
                'energia_kwh': fields[9],
            })
    return processed_data

# Ruteos y vistas
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/datos')
def datos():
    data = procesar_datos()
    return render_template('datos.html', datos=data)

# Configuración de archivo estático CSS
@app.route('/static/<path:path>')
def static_file(path):
    return app.send_static_file(path)

if __name__ == '__main__':
    app.run(debug=True)
