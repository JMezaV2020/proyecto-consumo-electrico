from flask import Flask, render_template

app = Flask(__name__)

# Ruteos y vistas
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/datos')
def datos():
    return render_template('datos.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

# Configuración de archivo estático CSS
@app.route('/static/<path:path>')
def static_file(path):
    return app.send_static_file(path)

if __name__ == '__main__':
    app.run(debug=True)