from flask import Flask, render_template, request, redirect, url_for, jsonify

from models.data import db, Countrytable

app = Flask(__name__)

# Set up the SQLAlchemy Database URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///country.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Disable modification tracking

# Initialize the database
db.init_app(app)

# Create the tables when app context is loaded
with app.app_context():
    db.create_all()


# Home Route
@app.route('/home')
def home():
    return render_template('index.html')


# Country Comparison Route - Fetch data from the database and pass to template

@app.route('/table')
def country_comparison1():
    # Query the Countrytable to get all countries data
    country_data = Countrytable.query.all()
    return render_template('table.html', countries=country_data)


@app.route('/tableadmin')
def country_comparison():
    # Query the Countrytable to get all countries data
    country_mod= Countrytable.query.all()
    return render_template('tableadmin.html', countries=country_mod)


@app.route('/')
def index():
    return render_template('index.html')
@app.route('/aboutus')
def aboutus():
    return render_template('aboutus.html')

@app.route('/finance')
def finance():
    return render_template('financialplaning.html')

@app.route('/budget')
def budget():
    return render_template('budget.html')

@app.route('/saving')
def saving():
    return render_template('saving.html')

@app.route('/analyze')
def analyze():
    return render_template('analyze.html')

@app.route('/insite')
def insite():
    return render_template('insite.html')



# Route to add a new country
@app.route('/add_country', methods=['POST'])
def add_country():
    rank = request.form['rank']
    country_name = request.form['country']
    cost_of_living = request.form['costOfLiving']
    rent_index = request.form['rentIndex']
    groceries_index = request.form['groceriesIndex']
    restaurant_index = request.form['restaurantIndex']
    local_purchase = request.form['localPurchase']

    new_country = Countrytable(
        Rank=rank,
        Country=country_name,
        Cost_Of_Living=cost_of_living,
        Rent_Index=rent_index,
        Groceries_Index=groceries_index,
        Restaurant_Index=restaurant_index,
        Local_Purchase=local_purchase
    )

    db.session.add(new_country)
    db.session.commit()

    return redirect(url_for('country_comparison1'))

# Route to update an existing country
# Route to fetch country data for editing
@app.route('/api/country/<int:rank>', methods=['GET'])
def get_country(rank):
    country = Countrytable.query.get_or_404(rank)
    return jsonify({
        'rank': country.Rank,
        'country': country.Country,
        'costOfLiving': country.Cost_Of_Living,
        'rentIndex': country.Rent_Index,
        'groceriesIndex': country.Groceries_Index,
        'restaurantIndex': country.Restaurant_Index,
        'localPurchase': country.Local_Purchase
    })
# Route to update an existing country
@app.route('/update_country/<int:rank>', methods=['POST'])
def update_country(rank):
    country = Countrytable.query.get_or_404(rank)

    country.Rank = request.form['rank']
    country.Country = request.form['country']
    country.Cost_Of_Living = request.form['costOfLiving']
    country.Rent_Index = request.form['rentIndex']
    country.Groceries_Index = request.form['groceriesIndex']
    country.Restaurant_Index = request.form['restaurantIndex']
    country.Local_Purchase = request.form['localPurchase']

    db.session.commit()  # Commit the changes to the database

    return redirect(url_for('country_comparison1'))  # Redirect to the country comparison page


# Route to delete a country
@app.route('/delete_country/<int:rank>', methods=['POST'])
def delete_country(rank):
    country = Countrytable.query.get_or_404(rank)
    db.session.delete(country)
    db.session.commit()

    return redirect(url_for('country_comparison1'))

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
