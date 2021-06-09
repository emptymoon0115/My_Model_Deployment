from flask import Flask,send_file, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('download.html')

@app.route('/download')
def download_file():
    p = "test_download.mid"
    return send_file(p,as_attachment=True)


if __name__=="__main__":
    app.run(debug=True)