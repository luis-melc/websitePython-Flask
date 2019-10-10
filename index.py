from flask import Flask


app = Flask(__name__) # __name__ variable de python

@app.route('/') #se crea la ruta principal
def home():
	return 'home page'

@app.route('/about')
def about():
	return 'about page'
if __name__ == '__main__':
	app.run();