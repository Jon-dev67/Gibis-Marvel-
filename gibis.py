from flask import Flask, render_template

app = Flask(__name__)

@app.route("/", methods=["POST","GET"])
def home_page():
  return render_template("index.html")
  
@app.route("/hulk")
def hulk_page():
  return render_template("Hulk.html")
  
@app.route("/luke_cage")
def Luke_Cage():
  return render_template("Luke_cage.html")
  
@app.route("/superman")
def Superman():
  return render_template("Superman.html")
  
  
if __name__=="__main__":
  app.run(debug=True)
  
  