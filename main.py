from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from config import Production
import pygal
import psycopg2




app = Flask(__name__)
app.config.from_object(Production)

#server = app.server
db = SQLAlchemy(app)
from models.stock import Stock
from models.sales import Sales
from models.inventory import Inventories

@app.before_first_request
def create_tables():
    db.create_all()



conn=psycopg2.connect("dbname = d8pv4s4i8mtljv user=prhysvlnbfrktf host=ec2-18-233-32-61.compute-1.amazonaws.com port=5432 password=d8b756cb01d30dbbb011bf8dd69c97a1fd92f0821646b7ce560e9dcaa9d1dca0")
#conn=psycopg2.connect("dbname = sales_demo user=postgres host=localhost port=5432 password=cinadhis99")
cur = conn.cursor()


@app.route('/')
def home():
        return render_template("index.html")

@app.route('/about')
def about():
        return render_template("index.html")
@app.route('/services')
def services():
        return render_template("index.html")



# @app.route('/person/<name>/<int:age>')
# def person(name,age):
#     return f'{name} is {age} years old'
@app.route('/inventories', methods=['POST','GET'])
def inventories():
    # http verbs (post,put/update get,delete)-help you create,read,delete from database
    r = Inventories.query.order_by(Inventories.id).all()
    
    cur.execute("""SELECT inv_id, sum(quantity) as "stock"
            	FROM ((SELECT st.inv_id, sum(stock) as "quantity"
            	FROM public.new_stock as st
            	GROUP BY inv_id) union all
            		 (SELECT sa.inv_id, - sum(quantity) as "quantity"
            	FROM public.new_sales as sa
            	GROUP BY inv_id) 
            		 ) stsa
            	GROUP BY inv_id
            	ORDER BY inv_id""")

    remStock = cur.fetchall()

    if request.method=='POST':
        name= request.form['name']
        type = request.form['type']
        buying_price = request.form['buying_price']
        selling_price = request.form['selling_price']

        records = Inventories(name=name,type=type,bp=buying_price,sp=selling_price )
        db.session.add(records)
        db.session.commit()

        return redirect(url_for('inventories'))
    return render_template('inventories.html',records=r, remStock=remStock)

@app.route('/stock/<inv_id>', methods=['POST', 'GET'])
def stock(inv_id):
        # http verbs (post,put/update get,delete)-help you create,read,delete from database
        if request.method == 'POST':
            stock = request.form['stock']

            record = Stock(inv_id=inv_id, stock=stock)
            db.session.add(record)
            db.session.commit()

            return redirect(url_for('inventories'))





        return render_template('inventories.html' )


@app.route('/sales/<inv_id>', methods=['POST','GET'])
def sales(inv_id):
    # http verbs (post,put/update get,delete)-help you create,read,delete from database
    if request.method=='POST':
        sale= request.form['sale']
        print(sale)
        record = Sales(inv_id=inv_id,quantity=sale)
        db.session.add(record)
        db.session.commit()

        return redirect(url_for('inventories'))

    return render_template('inventories.html')
@app.route('/edit/<inv_id>', methods=['POST','GET'])
def edit(inv_id):
    # http verbs (post,put/update get,delete)-help you create,read,delete from database
    if request.method=='POST':
        name = request.form['name']
        type = request.form['type']
        buying_price = request.form['buying_price']
        selling_price = request.form['selling_price']

        record = Inventories.query.filter_by(id=inv_id).first()
        record.name = name
        record.type = type
        record.bp = buying_price
        record.sp = selling_price
        db.session.commit()



        return redirect(url_for('inventories'))
    return render_template('inventories.html')
@app.route('/delete/<inv_id>', methods=['POST','GET'])
def delete(inv_id):
    if request.method == 'POST':
        record = Inventories.query.filter_by(id=inv_id).first()
        Stock.query.filter_by(inv_id=inv_id).delete()
        Sales.query.filter_by(inv_id=inv_id).delete()
        db.session.delete(record)

        db.session.commit()
        return redirect(url_for('inventories'))
    return render_template('inventories.html')

@app.route('/dashboard')
def charts():


    cur.execute("""SELECT EXTRACT(MONTH FROM s.created_at) AS months,
                     SUM(s.quantity) as total_sales
                     FROM new_sales as s
                     GROUP BY months
                     ORDER BY months""")
    records = cur.fetchall()
    conn.commit()
    # cur.close()
    # conn.close()

    data=[("Jumia", 20),("Instagram", 15), ("Website", 25), ("Shop-visits", 40)]
    pie_chart=pygal.Pie()
    pie_chart.title="Selling Mediums Used"
    pie_chart.add(data[0][0],data[0][1])
    pie_chart.add(data[1][0],data[1][1])
    pie_chart.add(data[2][0],data[2][1])
    pie_chart.add(data[3][0],data[3][1])
    pie_data=pie_chart.render_data_uri()

    x = []
    y = []
    for i in records:
        x.append(i[0])
        y.append(i[1])

    line_chart = pygal.Line()
    line_chart.title = 'sales 2019'
    line_chart.x_labels = map(str, x)
    line_chart.add("Monthly Sales", y)
    line_data = line_chart.render_data_uri()

    return render_template('dashboard.html', pie_data=pie_data,line_data=line_data)
@app.route('/line')
def line():
    data_line=[("Jan", 30),
               ("Feb", 40),
               ("March", 30),
               ("April", 30),
               ("May", 10),
               ("June", 20),
               ("July", 30),
               ("August", 15)]
    x=[]
    y = []
    for i in data_line:
        x.append(i[0])
        y.append(i[1])


    line_chart = pygal.Line()
    line_chart.title = 'Sugar sales 2020'
    line_chart.x_labels = map(str,x)
    line_chart.add("Sales",y)
    line_data=line_chart.render_data_uri()
    return render_template("line.html",line_data=line_data)

    # line_chart=pygal.Line()
    # line_chart.title = 'Browser usage evolution (in %)'
    # line_chart.x_labels = map(str, range(2002, 2013))
    # line_chart.add('Firefox', [None, None, 0, 16.6, 25, 31, 36.4, 45.5, 46.3, 42.8, 37.1])
    # line_chart.add('Chrome', [None, None, None, None, None, None, 0, 3.9, 10.8, 23.8, 35.3])
    # line_chart.add('IE', [85.8, 84.6, 84.7, 74.5, 66, 58.6, 54.7, 44.8, 36.2, 26.6, 20.1])
    # line_chart.add('Others', [14.2, 15.4, 15.3, 8.9, 9, 10.4, 8.9, 5.8, 6.7, 6.8, 7.5])
    # line_data=line_chart.render_data_uri()
    # return render_template('line.html', line_data=line_data)






if __name__ == '__main__':
    app.run(debug=True)

