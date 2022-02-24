from flask import Flask, render_template
app = Flask(__name__)
@app.route('/welcome')
def welcome():
    return render_template('well.html')

# # @app.route('/std/<name>')
# # def studentname(name):
#     return render_template("stud.html", sname = name)

if __name__ == "__main__":
    app.run()