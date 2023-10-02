from flask import Flask, render_template
from flask import request
import mongo as dbase



app = Flask(__name__)


@app.route("/")
def home():
    return render_template('index.html')
    #return "<p>PRIMERO</p>"

@app.route("/lectura")
def lectura():
   # resul=db_client.find_one()
    #print(resul)
    return "f<p>SEG</p>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)