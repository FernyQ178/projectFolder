from flask import Flask, render_template, request

app = Flask(__name__)

# @app.route("/")
# def hello():
#     return render_template('base.html')

def readDetails(filename):
    with open(filename, 'r') as f:
        return [line for line in f]
    
def writeToFile(filename, message):
    with open(filename, 'a') as f:
        f.write(message)


@app.route('/')
def homePage():
    name = "Ferny's Page"
    details = ['this is my name', 'this is my background', 'potatoes']
    details = readDetails('static/details.txt')
    return render_template("base.html", name = name, aboutMe = details)

@app.route('/user/<name>')
def greet(name):
    return f'<p>Hello, {name}!</p>'

@app.route('/form', methods=['GET', 'POST'])
def formDemo():
    name = None
    if request.method == 'POST':
        # if request.form['name']:
        #     name = request.form['name']
        if request.form['message']:
            writeToFile('static/comments.txt', request.form['message'])
    return render_template('form.html', name=name)


## When running this file directly
if __name__ == "__main__":
    app.run(debug=True)
