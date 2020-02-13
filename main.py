from flask import Flask, render_template
import pygal
import psycopg2

app = Flask(__name__)

@app.route('/about')
def about():
        return render_template("about.html", header="About Page")

@app.route('/service')
def service():
    return render_template("service.html")
@app.route('/person/<name>/<int:age>')
def person(name,age):
    return f'{name} is {age} years old'

@app.route('/')
def index():
    conn=psycopg2.connect("dbname = dffhf6pdqo27uj user=dpxcczdczuepco host= ec2-52-73-247-67.compute-1.amazonaws.com password=6fd9d07cdea8dd82f56c3c6963ca35e3b1db9fb47b4853e67de34fbf502869fb")
    cur = conn.cursor()
    # cur.execute("SELECT DROP inventories")
    # cur.execute("SELECT DROP stock")
    cur.execute("SELECT DROP sales")
    #
    # cur.execute("""create table stock (
    #     	id INT,
    #     	inv_id INT,
    #     	stock DECIMAL(7,2),
    #     	created_at DATE
    #     );
    #     insert into stock (id, inv_id, stock, created_at) values (1, 28, 2530.71, '11/15/2019');
    #     insert into stock (id, inv_id, stock, created_at) values (2, 1, 6677.35, '6/28/2019');
    #     insert into stock (id, inv_id, stock, created_at) values (3, 4, 7819.44, '9/23/2019');
    #     insert into stock (id, inv_id, stock, created_at) values (4, 5, 9846.09, '8/14/2019');
    #     insert into stock (id, inv_id, stock, created_at) values (5, 18, 7414.54, '12/3/2019');
    #     insert into stock (id, inv_id, stock, created_at) values (6, 4, 4155.82, '6/11/2019');
    #     insert into stock (id, inv_id, stock, created_at) values (7, 22, 8829.03, '1/19/2019');
    #     insert into stock (id, inv_id, stock, created_at) values (8, 12, 6033.72, '3/25/2020');
    #     insert into stock (id, inv_id, stock, created_at) values (9, 19, 6022.82, '9/30/2019');
    #     insert into stock (id, inv_id, stock, created_at) values (10, 20, 6746.16, '9/3/2020');
    #     insert into stock (id, inv_id, stock, created_at) values (11, 11, 271.97, '6/10/2020');
    #     insert into stock (id, inv_id, stock, created_at) values (12, 14, 1259.4, '3/14/2020');
    #     insert into stock (id, inv_id, stock, created_at) values (13, 5, 2412.3, '5/26/2019');
    #     insert into stock (id, inv_id, stock, created_at) values (14, 28, 3420.05, '3/14/2019');
    #     insert into stock (id, inv_id, stock, created_at) values (15, 15, 4233.19, '2/26/2020');
    #     insert into stock (id, inv_id, stock, created_at) values (16, 20, 3006.08, '3/7/2019');
    #     insert into stock (id, inv_id, stock, created_at) values (17, 6, 8660.08, '4/15/2019');
    #     insert into stock (id, inv_id, stock, created_at) values (18, 19, 8897.59, '1/20/2020');
    #     insert into stock (id, inv_id, stock, created_at) values (19, 7, 9776.91, '11/23/2019');
    #     insert into stock (id, inv_id, stock, created_at) values (20, 12, 3447.28, '9/12/2020');
    #     insert into stock (id, inv_id, stock, created_at) values (21, 6, 5731.3, '9/24/2019');
    #     insert into stock (id, inv_id, stock, created_at) values (22, 13, 1671.89, '5/23/2019');
    #     insert into stock (id, inv_id, stock, created_at) values (23, 29, 5380.14, '4/25/2019');
    #     insert into stock (id, inv_id, stock, created_at) values (24, 15, 2962.08, '7/15/2019');
    #     insert into stock (id, inv_id, stock, created_at) values (25, 19, 2821.84, '1/31/2019');
    #     insert into stock (id, inv_id, stock, created_at) values (26, 20, 5532.23, '8/25/2020');
    #     insert into stock (id, inv_id, stock, created_at) values (27, 7, 8098.29, '11/16/2019');
    #     insert into stock (id, inv_id, stock, created_at) values (28, 12, 4895.13, '3/12/2020');
    #     insert into stock (id, inv_id, stock, created_at) values (29, 27, 2355.97, '8/7/2019');
    #     insert into stock (id, inv_id, stock, created_at) values (30, 27, 9066.83, '9/2/2020');
    #     insert into stock (id, inv_id, stock, created_at) values (31, 2, 3999.27, '1/27/2019');
    #     insert into stock (id, inv_id, stock, created_at) values (32, 13, 92.75, '8/28/2020');
    #     insert into stock (id, inv_id, stock, created_at) values (33, 23, 6697.54, '4/5/2019');
    #     insert into stock (id, inv_id, stock, created_at) values (34, 20, 6723.54, '6/29/2020');
    #     insert into stock (id, inv_id, stock, created_at) values (35, 11, 7946.35, '7/27/2019');
    #     insert into stock (id, inv_id, stock, created_at) values (36, 27, 9774.26, '7/5/2019');
    #     insert into stock (id, inv_id, stock, created_at) values (37, 21, 4724.6, '1/11/2020');
    #     insert into stock (id, inv_id, stock, created_at) values (38, 1, 1302.91, '2/10/2019');
    #     insert into stock (id, inv_id, stock, created_at) values (39, 28, 7218.72, '3/16/2020');
    #     insert into stock(id, inv_id, stock, created_at) values (40, 22, 7930.9, '10/5/2020');
    #
    #         """)
    # cur.execute("SELECT * FROM stock;")
    # cur.fetchall()
    conn.commit()
    # cur.close()
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





    # x = []
    # y = []
    # for i in records:
    #     x.append(i[0])
    #     y.append(i[1])
    #
    # line_chart = pygal.Line()
    # line_chart.title = 'sales 2019'
    # line_chart.x_labels = map(str, x)
    # line_chart.add("Sales", y)
    # line_data = line_chart.render_data_uri()

    return render_template('index.html', pie_data=pie_data,)
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
    return render_template("line.html")

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

