from flask import Flask, session, render_template, request
app = Flask(__name__)

# Þessi verður að vera inni til að session virki, best að fá random gildi...
app.config['SECRET_KEY'] = 'Leyno'

vorur= [[0, 'Bugatti', 'Bugatti.jpg', 5000],
		[1, 'Castle', 'Castle.jpg', 10000],
		[2, 'Mansion', 'Mansion.jpg', 8000]
]

@app.route('/')
def index():
	karfa=[]
	fjoldi=0
	if 'karfa' in session:
		karfa=session['karfa']
		fjoldi=len(karfa)
	return render_template("home.html", v=vorur, fjoldi=fjoldi)

@app.route("/add/<int:id>")
def listir(id):
	karfa=[]
	fjoldi=0
	if 'karfa' in session:
		karfa=session['karfa']
		karfa.append(vorur[id])
		session['karfa']=karfa

	else:
		karfa.append(vorur[id])
		session['karfa']=karfa
		fjoldi=len(karfa)
	return render_template("home.html", v=vorur, fjoldi=fjoldi)

@app.route('/carts')
def carts():
	return render_template("carts.html")

if __name__ == "__main__":
	app.run(debug=True)
