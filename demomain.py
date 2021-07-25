from flask import Flask, render_template,request,redirect,url_for
import json
app= Flask(__name__, template_folder='templates')



@app.route("/", methods=["GET","POST"])
def Hello():
    if request.method == 'GET':
        return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
