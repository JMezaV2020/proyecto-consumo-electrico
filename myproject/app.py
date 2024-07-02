from flask import Flask, render_template, send_file
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
                'anio': fields[0].strip(),
                'mes': fields[1].strip(),
                'region': fields[2].strip(),
                'comuna': fields[3].strip(),
                'tipo_clientes': fields[4].strip(),
                'tarifa': fields[5].strip(),
                'clientes_facturados': fields[6].strip(),
                'e1_kwh': fields[7].strip(),
                'e2_kwh': fields[8].strip(),
                'energia_kwh': fields[9].strip(),
            })
    
    return processed_data

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

@app.route('/api/datos')
def api_datos():
    data = procesar_datos()
    return json.dumps(data, ensure_ascii=False)

@app.route('/static/<path:path>')
def static_file(path):
    return app.send_static_file(path)

@app.route('/download_csv')
def download_csv():
    filepath = '/home/jmezav/mysite/se_facturacion_clientes_regulados.csv'
    return send_file(filepath, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)

