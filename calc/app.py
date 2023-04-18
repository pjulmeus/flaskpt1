# Put your app in here.
from flask import Flask, request

from operations import add, sub, mult, div

app = Flask(__name__)

@app.route('/add')
def add_numbers():
    print (request.args)
    a = request.args["a"]
    b = request.args["b"]
    a_num = int(a)
    b_num = int(b)
    total = add(a_num, b_num)
    print(total)
    return f"""<h1>The total a + b = {total}</h1>"""

@app.route('/sub')
def sub_numbers():
    a = request.args["a"]
    b = request.args["b"]
    a_num = int(a)
    b_num = int(b)
    total = sub(a_num, b_num)
    return f"""<h1> A - B = {total}</h1>"""

@app.route("/mult")
def mult_number():
    a = request.args["a"]
    b = request.args["b"]
    a_num = int(a)
    b_num = int(b)
    total = mult(a_num, b_num)
    return f"""<h1> A multiplied by B = {total}</h1>"""

@app.route("/div")
def div_number():
    a = request.args["a"]
    b = request.args["b"]
    a_num = int(a)
    b_num = int(b)
    total = div(a_num, b_num)
    final = int(total)
    return f"""<h1> A divided by B = {final}</h1>"""

opert = {
    "add" : add,
    "sub" : sub,
    "div" : div,
    "mult" : mult
}

@app.route("/math/<operation>")
def math_operator(operation):
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    total = opert[operation](a, b)
    return f"""<h1> The total is {total}"""


