from flask import Flask,render_template,request

app=Flask(__name__)
@app.route("/")
def hello():
    return render_template("home.html")



@app.route("/Register",methods=["POST"])
def Register():
    if request.method=="POST":
        name=request.form.get('name')
        age=request.form.get('age')
        address=request.form.get('address')
        contact=request.form.get('contact')
        mail=request.form.get('mail')
        return render_template("result.html",name=name,age=age,address=address,contact=contact,mail=mail)




if __name__=='__main__':
    app.run(debug=True)