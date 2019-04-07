from flask import Flask, render_template, send_file
app = Flask(__name__)
console_output=""
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/logo.png')
def logo():
    return send_file('logo_crop.png',mimetype='image/png')
@app.route('/style.css')
def css():
    return send_file('style.css',mimetype='text/css')
@app.route('/reset')
def reset():
    console_output=""
    return "Console cleared!"
@app.route('/console_text')
def console_text():
    return console_output
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0',port=8000)
