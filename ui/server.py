from flask import Flask, render_template, send_file,request, g
# import actions


cache={"text":""}
app = Flask(__name__)

@app.route('/')
def index():
    g.console = ""
    return render_template('index.html')
@app.route('/logo.png')
def logo():
    return send_file('logo.png',mimetype='image/png')
@app.route('/style.css')
def css():
    return send_file('style.css',mimetype='text/css')
@app.route('/reset')
def reset():
    cache["text"]=""
    return "Console cleared!"
@app.route('/consoletext')
def console_text():
    return cache["text"].replace("\n","<br>")

@app.route('/input')
def getinput():

    cache["text"]+=request.args.get('text')

    # return cache["text"]
    return "done"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0',port=8004)
