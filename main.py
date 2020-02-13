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
    cur.execute("""create table sales (
    	id INT,
    	inv_id INT,
    	quantity DECIMAL(7,2),
    	created_at DATE
    );
    insert into sales (id, inv_id, quantity, created_at) values (1, 16, 538.45, '5/14/2020');
    insert into sales (id, inv_id, quantity, created_at) values (2, 13, 7801.14, '9/13/2020');
    insert into sales (id, inv_id, quantity, created_at) values (3, 25, 7694.8, '6/23/2019');
    insert into sales (id, inv_id, quantity, created_at) values (4, 26, 7791.22, '6/19/2020');
    insert into sales (id, inv_id, quantity, created_at) values (5, 3, 7135.58, '9/10/2020');
    insert into sales (id, inv_id, quantity, created_at) values (6, 18, 2854.37, '5/15/2019');
    insert into sales (id, inv_id, quantity, created_at) values (7, 27, 5035.35, '5/4/2020');
    insert into sales (id, inv_id, quantity, created_at) values (8, 25, 5216.47, '8/12/2020');
    insert into sales (id, inv_id, quantity, created_at) values (9, 27, 7040.34, '3/3/2020');
    insert into sales (id, inv_id, quantity, created_at) values (10, 8, 5930.77, '4/11/2020');
    insert into sales (id, inv_id, quantity, created_at) values (11, 15, 5552.86, '9/2/2020');
    insert into sales (id, inv_id, quantity, created_at) values (12, 14, 7503.14, '5/7/2019');
    insert into sales (id, inv_id, quantity, created_at) values (13, 17, 6867.12, '10/13/2019');
    insert into sales (id, inv_id, quantity, created_at) values (14, 13, 8644.56, '3/10/2020');
    insert into sales (id, inv_id, quantity, created_at) values (15, 10, 3364.19, '7/17/2019');
    insert into sales (id, inv_id, quantity, created_at) values (16, 9, 4166.68, '10/10/2019');
    insert into sales (id, inv_id, quantity, created_at) values (17, 14, 7323.69, '5/26/2020');
    insert into sales (id, inv_id, quantity, created_at) values (18, 22, 2568.38, '9/21/2019');
    insert into sales (id, inv_id, quantity, created_at) values (19, 20, 469.79, '12/20/2019');
    insert into sales (id, inv_id, quantity, created_at) values (20, 11, 9362.65, '3/15/2020');
    insert into sales (id, inv_id, quantity, created_at) values (21, 19, 96.32, '8/2/2020');
    insert into sales (id, inv_id, quantity, created_at) values (22, 12, 4837.4, '7/14/2019');
    insert into sales (id, inv_id, quantity, created_at) values (23, 20, 2065.14, '3/22/2020');
    insert into sales (id, inv_id, quantity, created_at) values (24, 5, 7766.79, '12/4/2019');
    insert into sales (id, inv_id, quantity, created_at) values (25, 6, 3763.41, '9/9/2020');
    insert into sales (id, inv_id, quantity, created_at) values (26, 15, 2638.67, '8/19/2020');
    insert into sales (id, inv_id, quantity, created_at) values (27, 28, 4992.87, '6/30/2019');
    insert into sales (id, inv_id, quantity, created_at) values (28, 16, 145.89, '8/22/2020');
    insert into sales (id, inv_id, quantity, created_at) values (29, 24, 4638.07, '11/14/2019');
    insert into sales (id, inv_id, quantity, created_at) values (30, 8, 7026.3, '12/12/2019');
    insert into sales (id, inv_id, quantity, created_at) values (31, 21, 4713.49, '7/17/2020');
    insert into sales (id, inv_id, quantity, created_at) values (32, 25, 5281.33, '11/3/2019');
    insert into sales (id, inv_id, quantity, created_at) values (33, 23, 3360.82, '10/14/2019');
    insert into sales (id, inv_id, quantity, created_at) values (34, 7, 9442.02, '7/30/2020');
    insert into sales (id, inv_id, quantity, created_at) values (35, 28, 8352.62, '4/8/2019');
    insert into sales (id, inv_id, quantity, created_at) values (36, 8, 6171.89, '2/21/2019');
    insert into sales (id, inv_id, quantity, created_at) values (37, 6, 9109.22, '6/21/2020');
    insert into sales (id, inv_id, quantity, created_at) values (38, 8, 9456.51, '3/31/2019');
    insert into sales (id, inv_id, quantity, created_at) values (39, 2, 8044.91, '7/8/2019');
    insert into sales (id, inv_id, quantity, created_at) values (40, 25, 1610.45, '3/5/2019');

       """)
    cur.execute("SELECT * FROM sales;")
    records = cur.fetchall()
    conn.commit()
    cur.close()
    conn.close()




    # cur.execute("""SELECT EXTRACT(MONTH FROM s.created_at) AS months,
    #                  SUM(s.quantity) as total_sales
    #                  FROM public.sales as s
    #                  GROUP BY months
    #                  ORDER BY months""")
    # records = cur.fetchall()

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

