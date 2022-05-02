import requests
from flask import Flask,render_template,url_for
from flask import request as req


app = Flask(__name__)
@app.route("/",methods=["GET","POST"])
def Index():
    return render_template("index.html")

@app.route("/Summarize",methods=["GET","POST"])
def Summarize():
    if req.method== "POST":
        API_URL = "https://api-inference.huggingface.co/models/faisalahmad/summarizer2"
        headers = {"Authorization": "Bearer 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"}

        data=req.form["data"]

        maxL=int(req.form["maxL"])
        minL=maxL//4
        def query(payload):
            response = requests.post(API_URL, headers=headers, json=payload)
            return response.json()

        output = query({
            "inputs":data,
            "parameters":{"min_length":minL,"max_length":maxL},
        })[0]
        print(output)
        return render_template("index.html",result=output["generated_text"])
    else:
        return render_template("index.html")
