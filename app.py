from B_Input_Createsong import bell_prediction
from flask import Flask, render_template, url_for,request, send_file

import B_Input_Createsong as B

#import B_Createsong as B

app = Flask(__name__)


@app.route('/', methods = ["GET", "POST"] )
def B_Input_Createsong():
    my_bell = None
    if request.method == "POST":
        text = request.form['text']
        bell_pred = B.bell_prediction(text)
        bell=bell_pred

       

    #return render_template("index.html", bell=my_bell)
    return render_template("index.html")

@app.route('/Download')
def download_file():
    b = "test_success.mid"
    return send_file(b,as_attachment=False)
   
if __name__=="__main__":
    app.run(debug=True)


'''

@app.route("/sub", methods = ['POST'] )
def submit():
    # HTML -> .py
    if request.method == "POST":
        name = request.form["username"]

    # .py -> HTML
    return render_template("sub.html", n = name  )
'''


if __name__ == '__main__':

    app.run(debug=True)
   

