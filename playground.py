from flask import Flask, render_template  
app = Flask(__name__)


@app.route('/')
def welcome():
    return render_template("basic_two.html",times=3, div_color="blue")

@app.route('/play/<x>')
def firstplay(x):
    return render_template("basic_two.html",times=int(x), div_color = "blue")

@app.route('/play/<x>/<color>')
def secondplay (x,color):
    return render_template("basic_two.html",times=int(x), div_color = color)


if __name__=="__main__":       
    app.run(debug=True)   