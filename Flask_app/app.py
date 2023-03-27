from flask import Flask, render_template, request
import re

app = Flask(__name__)


@app.route('/',methods = ['GET','POST'])
def index_page():
    
    if request.method == 'POST':
        user_name = request.form.get('in_1')
        upper = user_name.upper()
        return render_template('index.html',upper = upper)
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)




    
