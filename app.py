from flask import Flask, request, render_template, jsonify, url_for

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template("index.html")

@app.route('/even', methods=['GET', 'POST'])
def even():
    n=request.form['num']
    n=int(n)
    if(n%2==0):
        result = {
            "Number" : n,
            "Even" : True
        }
    else:
        result = {
            "Number" : n,
            "Even" : False
        }
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)