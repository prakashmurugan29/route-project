from flask import Flask
app=Flask('__name__')
@app.route('/')
def hello():
    return "<h1 style='color:red;text-align:center;'>It's your 1st hello</h1>"
@app.route('/1')
def hello1():
    return "<h1 style='color:green;text-align:center;'>It's your 2nd hello</h1>"
@app.route('/1/2')
def hello2():
    return "<h1 style='color:blue;text-align:center;'>It's your 3rd hello</h1>"

if __name__=='__main__':
    app.run(debug=True)