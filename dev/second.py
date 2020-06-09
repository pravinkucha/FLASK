from flask import Flask
app =  Flask(__name__)
@app.route('/blog/<int:Postid>')
def show_blog(Postid):
	return 'Blog is %s '% Postid

@app.route('/rev/<float:RevId>')
def show_revid(RevId):
	return 'Revision id is %s'% RevId
	
if __name__ =='__main__':
	app.debug = True
	app.run()
	


