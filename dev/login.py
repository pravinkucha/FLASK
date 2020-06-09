from flask import Flask,redirect,url_for,request
app =   Flask(__name__)
@app.route('/success/<name>')

def fn_success(name):
	return 'Welcome %s' % name
	
@app.route('/login',methods=['POST','GET'])

def fn_login():
	if request.method=='POST':
		user = request.form['nm']
		return redirect(url_for('fn_success',name=user))
	else:
		user = request.args.get('nm')
		return redirect(url_for('fn_success',name=user))
if __name__ =='__main__':
	app.run(debug=True)
