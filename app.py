from flask import Flask, render_template, request
import pyfiglet

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    ascii_art = None
    if request.method == 'POST':
        text = request.form['text']
        font = request.form['font']
        try:
            ascii_art = pyfiglet.figlet_format(text, font=font)
        except:
            ascii_art = "Error: Invalid font selected"
    
    return render_template('index.html', ascii_art=ascii_art)

if __name__ == '__main__':
    app.run(debug=True)