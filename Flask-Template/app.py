from flask import *



#initiallize flask 
app = Flask(__name__)

#Display first simple welcome msg
@app.route('/index')
def home():
    return render_template("index.html")

#Display second page for welcome user
@app.route('/index1')
def about():
    return render_template('index1.html')

#run code in debug mode
if __name__ == '__main__':
    app.run(debug=True)



