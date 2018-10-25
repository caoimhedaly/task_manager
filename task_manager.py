from flask import Flask, render_template, request, redirect
import os
from flask_pymongo import PyMongo

app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")

mongo = PyMongo(app)


@app.route("/")
def show_hi():
    tasks = mongo.db.tasks.find()
    return render_template("tasks.html", tasks= tasks)
    
@app.route("/add_task", methods =["GET", "POST"])
def add_task():
    
    if request.method=="POST":
        mongo.db.tasks.insert_one(request.form.to_dict()) 
        # this line converts our form to dictionary form and inserts it to mongo
        return redirect("/")
        
        
    
    else:
        categories = mongo.db.categories.find()
        return render_template("add_task.html", categories=categories)

if __name__ == "__main__":
        app.run(host=os.getenv('IP', '0.0.0.0'), port=int(os.getenv('PORT', 8080)), debug=True)




