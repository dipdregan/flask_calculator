from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/',methods = ['GET'])
def index():
    """ Display the index page accessible at '/' """
    return render_template("index.html")

@app.route('/operation/', methods=['POST'])
def operation():
    """
    Route where we send calculator from input
    """
    if(request.method=='POST'):
        math= request.form['math']
        num1 = int(request.form['num1'])
        num2 = int(request.form['num2'])

        result = 0

        if math=='add':
            result = num1 + num2
        elif math== 'sub':
            result = num1-num2
        elif math== 'mul':
            result = num1*num2
        elif math== 'div':
            result = num1/num2
        else:
            return('Please select some operation ')

        return render_template("result.html",math=math,result=result)

if __name__=="__main__":
    app.run(debug=True,port =1111)