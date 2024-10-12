from flask import Flask

app = Flask(__name__)

@app.route("/") # การสร้าง path route จะเรียกใช้งานฟังชันด้านล่างเลย
def index():
    return "<h1>Hello, World!</h1>"

@app.route("/user/<name>/<age>") 
def member(name,age):
    return "<h1>Hello, World! {} , age: {} </h1>".format(name,age)


if __name__ == "__main__":
    app.run(debug=True) #เปิด debug mode
