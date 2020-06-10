from flask import Flask,render_template
app = Flask(__name__)
@app.route('/hello/<user>/<int:score>')
def hello_name(user,score):
	dict = {'name':user,'marks':score,'data':{'Phy':56,'Che':75,'Maths':90}}
	print(dict)
	return render_template('hello.html',results=dict)
	
if __name__=='__main__':
	app.run(debug=True)
