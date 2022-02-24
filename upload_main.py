from flask import Flask, render_template, request
app = Flask(__name__)
@app.route('/upload')
def upload():
    return render_template("upload.html")

@app.route('/success', methods = ['POST']) #POST is used to hide the file details on the URL
def success():
    if request.method == 'POST':
        f = request.files['file']
    return render_template("success.html", fname = f.filename)

if __name__ == "__main__":
    app.run()