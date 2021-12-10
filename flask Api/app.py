from flask import Flask, jsonify
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello,Vinayak</p>"

@app.route("/leapYear/<int:year>")
def leapYear(year):
    if year % 4 == 0 and year % 100 != 0:
        result = {
            "year":year,
            "leapYear": True,
            "statement":"this year divisible by 4"
        }
        return jsonify(result)
    elif year % 100 == 0:
        result = {
            "year":year,
            "leapYear": False,
            "statement":"this year divisible by 100"
        }
    elif year % 400 ==0:
        result = {
            "year":year,
            "leapYear": True,
            "statement":"this year divisible by 400"
        }
    else:
        result = {
            "year":year,
            "leapYear": False,
            "statement":"this is not leap year"
        }
    return jsonify(result)


if __name__=="__main__":
    app.run(debug=True)