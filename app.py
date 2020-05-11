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
	return render_template("home.html", v=vorur, fjoldi=fjoldi, karfa=karfa)

@app.route("/add/<int:id>")
def listir(id):
	karfa=[]
	fjoldi=0
	if 'karfa' in session:
		karfa=session['karfa']
		karfa.append(vorur[id])
		session['karfa']=karfa
		fjoldi=len(karfa)
		total= []
		for x in karfa:
			total.append(x[3])
		summa=sum(total)
		return render_template("carts.html", v=vorur, fjoldi=fjoldi, karfa=karfa, summa=summa)
	else:
		karfa.append(vorur[id])
		session['karfa']=karfa
		fjoldi=len(karfa)
		total= []
		for x in karfa:
			total.append(x[3])
		summa=sum(total)
		return render_template("carts.html", v=vorur, fjoldi=fjoldi, karfa=karfa, summa=summa)

@app.route('/carts')
def carts():
	karfa=session['karfa']
	fjoldi=len(karfa)
	total= []
	for x in karfa:
		total.append(x[3])
	summa=sum(total)
	return render_template("carts.html", v=vorur, fjoldi=fjoldi, karfa=karfa, summa=summa)

@app.route('/off')
def sessionoff():
    if 'karfa' in session:
        session.pop('karfa', None)
        return '<h3>Session poped</h3><h3><a href="/">Home</a></h3>'
    else:
        return '<h3>Session was not set</h3><h3><a href="/">Home</a></h3>'

if __name__ == "__main__":
	app.run(debug=True)
