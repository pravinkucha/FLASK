from flask import Flask,redirect,url_for,request,render_template
app =   Flask(__name__)

@app.route("/reg",methods=['POST','GET'])
def fn_reg():
   return render_template("register.html")

@app.route('/singup',methods=['POST','GET'])
def fn_login():
	if request.method=='POST':		
		return render_template('register.html',results=request.form)
	else:
		return redirect(url_for('fn_reg'))
if __name__ =='__main__':
	app.run(debug=True)
