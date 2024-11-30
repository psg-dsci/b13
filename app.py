from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html", 
                           name="John Doe", 
                           about="I am a passionate software developer with expertise in Python, Flask, and web development.",
                           skills=["Python", "Flask", "Django", "HTML", "CSS", "JavaScript"],
                           projects=[
                               {"title": "Portfolio Website", "description": "A simple portfolio website using Flask."},
                               {"title": "E-commerce App", "description": "An online shopping platform built with Django."},
                               {"title": "To-Do App", "description": "A basic task management web app built using Flask."}
                           ])

if __name__ == "__main__":
    app.run(debug=True)
