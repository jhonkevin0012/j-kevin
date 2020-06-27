from flask import Flask

app = Flask(__name__)

@app.route('/')
def home ():
    return 'Home page'
    
@app.route('/About')
def About ():
    return 'About pages'

if __name__=='__main__':
    app.run(debug=True)
