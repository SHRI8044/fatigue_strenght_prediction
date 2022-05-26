from flask import Flask,render_template,request

app = Flask(__name__)

@app.route("/")

def index():
    return render_template("index.html")


@app.route("/data",methods = ["GET","POST"])
def data():
    if request.method == "POST":
        data = request.form
        print(data)



    return render_template("disply.html",data_user =data)


if __name__ == "__main__":
    app.run(debug=True) 