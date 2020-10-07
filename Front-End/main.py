from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

@app.route("/hello")
def hello():
    return {"message": "Hello world"}

@app.route("/access/data")
def home():
    return render_template('home.html')

@app.route("/access/data/<name>")
def read_data(name):
    print ("name",name)
    data = pd.read_csv(f"{name}.csv")
    return render_template('index.html',  tables=[data.to_html(classes='data')], titles=data.columns.values)

if __name__ == "__main__":
    app.run(debug=True)