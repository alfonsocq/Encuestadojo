from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'el-viaje- de-Chihiro'
@app.route('/')                           
def principal():

    return render_template('index.html')  

@app.route("/success", methods=["POST"])
def proyectar():
    print(request.form)

    session["usuario"] = request.form["nombre"]
    session["lugar"] = request.form["locacion"]
    session["lenguaje"] = request.form["favorito"]
    session["opinion"] = request.form["comentarios"]

    return redirect("/resultado")

@app.route("/resultado")
def resultado():
    return render_template("resultado.html")  

if __name__=="__main__":
    app.run(debug=True) 
