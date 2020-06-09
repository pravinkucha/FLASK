from flask import Flask
app =  Flask(__name__)
@app.route('/hello')
def Hello_word():
	return 'Hello World!'
app.add_url_rule('/','Hello welcome',Hello_word)	
if __name__ == '__main__':
	app.run(debug=True)
