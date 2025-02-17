from flask import Flask,render_template,request
import google.generativeai as genai
import os

#os.environ["MAKERSUITE_API_KEY] = ""
api = "AIzaSyCSn86Q5Ml98BGO1tgRWUk1vsrIykSQji4"
genai.configure(api_key=api)
model = genai.GenerativeModel("gemini-1.5-flash")

app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def index():
    return(render_template("index.html"))

@app.route("/ai_agent", methods=["GET","POST"])
def ai_agent():
    return(render_template("ai_agent.html"))

@app.route("/ai_agent_reply", methods=["GET","POST"])
def ai_agent_reply():
    q = request.form.get("q")
    r = model.generate_content(q)
    return(render_template("ai_agent_reply.html",r=r.text))

@app.route("/prediction", methods=["GET","POST"])
def prediction():
    return(render_template("index.html"))

@app.route("/paynow", methods=["GET","POST"])
def paynow():
    return(render_template("paynow.html"))

if __name__ == "__main__":
    app.run()
