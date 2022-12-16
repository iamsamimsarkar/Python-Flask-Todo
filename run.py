from flask import *
import json
import string
import random
def tokenGen(tokenLen):
  ch = string.ascii_lowercase
  dg = string.digits
  sp = string.punctuation
  mix = ch+dg
  mixLen = len(mix)
  token = ""
  for i in range(tokenLen):
    randNumb = random.randint(0,mixLen-1)
    token += mix[randNumb]
  return token

app = Flask(__name__)

@app.route("/")
def func():
  return "<h1>Welcome to my Todo Application</h1>"
@app.route("/database/")
def database():
  fi = open("data.json","r")
  data = fi.read()
  fi.close()
  if data == "" or data == " ":
    data = [{"fname":"","number":"0","address":"","token":"abc"}]
  else:
    data = json.loads(data)
  return render_template("index.html",res=data,numb=len(data))
@app.route("/insert-form/")
def insert_form():
  return render_template("form.html");
@app.route("/insert-success",methods=["POST"])
def insert_success():
  fname = request.form['fname']
  number = request.form['number']
  address = request.form['address']
  token = tokenGen(24)
  fi = open("data.json","r")
  data = fi.read()
  fi.close()
  if data == "" or data == " ":
    data = []
  else:
    data = json.loads(data)
  obj = {
    "fname": fname,
    "number": number,
    "address": address,
    "token": token,
  }
  data.append(obj)
  fi = open("data.json","w")
  fi.write(json.dumps(data))
  fi.close() 
  return redirect(url_for("database"))
@app.route("/update-form/<tokenId>")
def update_form(tokenId):
    fi = open("data.json","r")
    data = json.loads(fi.read())
    fi.close()
    for x in data:
      if x["token"] == tokenId:
        obj = x
        break
    return render_template("update.html",fname=obj["fname"],number=obj["number"],address=obj["address"],token=obj["token"] )
@app.route("/update-success",methods=["POST"])
def update_success():
  fi = open("data.json","r")
  data = json.loads(fi.read())
  fi.close()
  fname = request.form["fname"]
  number = request.form["number"]
  address = request.form["address"]
  token = request.form["token"]
  for x in data:
    if x["token"] == token:
      x["fname"] = fname
      x["number"] = number
      x["address"] = address
      break
  fi = open("data.json","w")
  fi.write(json.dumps(data))
  fi.close()
  return redirect(url_for("database"))
@app.route("/delete/<tokenId>")
def delete_data(tokenId):
  fi = open("data.json","r")
  data = json.loads(fi.read())
  fi.close()
  for x in data:
    if x["token"] == tokenId:
      data.remove(x)
      break
  fi = open("data.json","w")
  fi.write(json.dumps(data))
  fi.close()
  return redirect(url_for("database"))


if __name__ == "__main__":
  app.run(debug=True,port=8080)