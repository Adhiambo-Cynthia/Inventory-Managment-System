from flask import Flask, render_template
import pygal
import psycopg2

app = Flask(__name__)



@app.route('/')
def hello_world(name):
    #return "Hello!" + name
    return f'Hello {name}'
@app.route('/about')
def about():
        return render_template("about.html", header="About Page")

@app.route('/service')
def service():
    return render_template("service.html")
@app.route('/person/<name>/<int:age>')
def person(name,age):
    return f'{name} is {age} years old'

@app.route('/index')
def index():
    conn=psycopg2.connect("dbname = dffhf6pdqo27uj user=dpxcczdczuepco host= ec2-52-73-247-67.compute-1.amazonaws.com password=6fd9d07cdea8dd82f56c3c6963ca35e3b1db9fb47b4853e67de34fbf502869fb")
    cur = conn.cursor()
    cur.execute("CREATE TABLE inventories (id serial PRIMARY KEY, name varchar, bp numeric ,sp numeric, type varchar);")
    cur.execute("CREATE TABLE stock (id serial PRIMARY KEY, inv_id integer,stock numeric, created_at date,FOREIGN KEY (inv_id) REFERENCES inventories(id));")
    cur.execute("CREATE TABLE sales (id serial PRIMARY KEY, inv_id integer , quantity numeric, created_at date, FOREIGN KEY (inv_id) REFERENCES inventories(id) );")

    cur.execute("""SELECT EXTRACT(MONTH FROM s.created_at) AS months,
                     SUM(s.quantity) as total_sales
                     FROM public.sales as s 
                     GROUP BY months
                     ORDER BY months""")
    records = cur.fetchall()

    data=[("Instagram", 30),("Twitter", 10), ("Facebook", 50), ("Snapchat", 10)]
    pie_chart=pygal.Pie()
    pie_chart.title="Social Media Usage in Kenya"
    pie_chart.add(data[0][0],data[0][1])
    pie_chart.add(data[1][0],data[1][1])
    pie_chart.add(data[2][0],data[2][1])
    pie_chart.add(data[3][0],data[3][1])
    pie_data=pie_chart.render_data_uri()


    # data_line = [("Jan", 30),
    #                  ("Feb", 40),
    #                  ("March", 30),
    #                  ("April", 30),
    #                  ("May", 10),
    #                  ("June", 20),
    #                  ("July", 30),
    #                  ("August", 15)]





    x = []
    y = []
    for i in records:
        x.append(i[0])
        y.append(i[1])

    line_chart = pygal.Line()
    line_chart.title = 'sales 2019'
    line_chart.x_labels = map(str, x)
    line_chart.add("Sales", y)
    line_data = line_chart.render_data_uri()

    return render_template('index.html', pie_data=pie_data, line_data=line_data)
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


@app.route('/add/<int:one>/<int:two>')
def addition(one,two):
    return str(one+two)




if __name__ == '__main__':
    app.run(debug=True)

