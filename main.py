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
    cur.execute("""create
    table
    inventories(
        id
    INT,
    name
    VARCHAR(50),
    bp
    DECIMAL(7, 2),
    sp
    DECIMAL(7, 2),
    type
    VARCHAR(10)
    );
    insert
    into
    inventories(id, name, bp, sp, type)
    values(1, 'Mushroom - Morels, Dry', 2477.77, 3468.878, 'fruits');
    insert
    into
    inventories(id, name, bp, sp, type)
    values(2, 'Scallops - 20/30', 2232.52, 3125.528, 'fruits');
    insert
    into
    inventories(id, name, bp, sp, type)
    values(3, 'Turkey - Oven Roast Breast', 8230.33, 11522.462, 'vegetables');
    insert
    into
    inventories(id, name, bp, sp, type)
    values(4, 'Spring Roll Wrappers', 4008.56, 5611.984, 'fruits');
    insert
    into
    inventories(id, name, bp, sp, type)
    values(5, 'Gingerale - Schweppes, 355 Ml', 7473.83, 10463.362, 'fruits');
    insert
    into
    inventories(id, name, bp, sp, type)
    values(6, 'Puff Pastry - Slab', 6380.64, 8932.896, 'vegetables');
    insert
    into
    inventories(id, name, bp, sp, type)
    values(7, 'Lid - Translucent, 3.5 And 6 Oz', 2836.14, 3970.596, 'vegetables');
    insert
    into
    inventories(id, name, bp, sp, type)
    values(8, 'Beer - Mcauslan Apricot', 9740.62, 13636.868, 'fruits');
    insert
    into
    inventories(id, name, bp, sp, type)
    values(9, 'Pastry - Baked Scones - Mini', 6047.61, 8466.654, 'fruits');
    insert
    into
    inventories(id, name, bp, sp, type)
    values(10, 'Bread - White, Sliced', 8987.62, 12582.668, 'fruits');
    insert
    into
    inventories(id, name, bp, sp, type)
    values(11, 'Table Cloth 54x54 White', 5243.56, 7340.984, 'vegetables');
    insert
    into
    inventories(id, name, bp, sp, type)
    values(12, 'Napkin - Beverge, White 2 - Ply', 6815.01, 9541.014, 'vegetables');
    insert
    into
    inventories(id, name, bp, sp, type)
    values(13, 'Sugar - Individual Portions', 6066.86, 8493.604, 'vegetables');
    insert
    into
    inventories(id, name, bp, sp, type)
    values(14, 'Sauce - Hoisin', 4533.05, 6346.27, 'vegetables');
    insert
    into
    inventories(id, name, bp, sp, type)
    values(15, 'Chilli Paste, Ginger Garlic', 4835.75, 6770.05, 'fruits');
    insert
    into
    inventories(id, name, bp, sp, type)
    values(16, 'Rice - Aborio', 2949.63, 4129.482, 'fruits');
    insert
    into
    inventories(id, name, bp, sp, type)
    values(17, 'Vegetable - Base', 1150.02, 1610.028, 'vegetables');
    insert
    into
    inventories(id, name, bp, sp, type)
    values(18, 'Cilantro / Coriander - Fresh', 1009.11, 1412.754, 'fruits');
    insert
    into
    inventories(id, name, bp, sp, type)
    values(19, 'Wine - Ej Gallo Sonoma', 3278.04, 4589.256, 'vegetables');
    insert
    into
    inventories(id, name, bp, sp, type)
    values(20, 'Cafe Royale', 9873.15, 13822.41, 'vegetables');
    insert
    into
    inventories(id, name, bp, sp, type)
    values(21, 'Lemonade - Kiwi, 591 Ml', 5318.15, 7445.41, 'fruits');
    insert
    into
    inventories(id, name, bp, sp, type)
    values(22, 'Chocolate - Milk Coating', 2922.98, 4092.172, 'vegetables');
    insert
    into
    inventories(id, name, bp, sp, type)
    values(23, 'Butter - Salted, Micro', 8050.95, 11271.33, 'vegetables');
    insert
    into
    inventories(id, name, bp, sp, type)
    values(24, 'Nut - Pecan, Halves', 1692.34, 2369.276, 'vegetables');
    insert
    into
    inventories(id, name, bp, sp, type)
    values(25, 'Cactus Pads', 3498.4, 4897.76, 'vegetables');
    insert
    into
    inventories(id, name, bp, sp, type)
    values(26, 'Table Cloth 54x72 White', 5476.9, 7667.66, 'fruits');
    insert
    into
    inventories(id, name, bp, sp, type)
    values(27, 'Cheese - Victor Et Berthold', 1405.51, 1967.714, 'vegetables');
    insert
    into
    inventories(id, name, bp, sp, type)
    values(28, 'Juice - Apple, 341 Ml', 8253.34, 11554.676, 'vegetables');
    insert
    into
    inventories(id, name, bp, sp, type)
    values(29, 'Tuna - Salad Premix', 9656.04, 13518.456, 'fruits');
    insert
    into
    inventories(id, name, bp, sp, type)
    values(30, 'Lettuce - California Mix', 2049.03, 2868.642, 'vegetables');""")
    cur.execute("SELECT * FROM inventories;")
    cur.fetchall()
    conn.commit()
    cur.close()
    conn.close()

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
    cur.fetchall()
    conn.commit()
    cur.close()
    conn.close()

    cur.execute("""create table stock (
	id INT,
	inv_id INT,
	stock DECIMAL(7,2),
	created_at DATE
);
insert into stock (id, inv_id, stock, created_at) values (1, 28, 2530.71, '11/15/2019');
insert into stock (id, inv_id, stock, created_at) values (2, 1, 6677.35, '6/28/2019');
insert into stock (id, inv_id, stock, created_at) values (3, 4, 7819.44, '9/23/2019');
insert into stock (id, inv_id, stock, created_at) values (4, 5, 9846.09, '8/14/2019');
insert into stock (id, inv_id, stock, created_at) values (5, 18, 7414.54, '12/3/2019');
insert into stock (id, inv_id, stock, created_at) values (6, 4, 4155.82, '6/11/2019');
insert into stock (id, inv_id, stock, created_at) values (7, 22, 8829.03, '1/19/2019');
insert into stock (id, inv_id, stock, created_at) values (8, 12, 6033.72, '3/25/2020');
insert into stock (id, inv_id, stock, created_at) values (9, 19, 6022.82, '9/30/2019');
insert into stock (id, inv_id, stock, created_at) values (10, 20, 6746.16, '9/3/2020');
insert into stock (id, inv_id, stock, created_at) values (11, 11, 271.97, '6/10/2020');
insert into stock (id, inv_id, stock, created_at) values (12, 14, 1259.4, '3/14/2020');
insert into stock (id, inv_id, stock, created_at) values (13, 5, 2412.3, '5/26/2019');
insert into stock (id, inv_id, stock, created_at) values (14, 28, 3420.05, '3/14/2019');
insert into stock (id, inv_id, stock, created_at) values (15, 15, 4233.19, '2/26/2020');
insert into stock (id, inv_id, stock, created_at) values (16, 20, 3006.08, '3/7/2019');
insert into stock (id, inv_id, stock, created_at) values (17, 6, 8660.08, '4/15/2019');
insert into stock (id, inv_id, stock, created_at) values (18, 19, 8897.59, '1/20/2020');
insert into stock (id, inv_id, stock, created_at) values (19, 7, 9776.91, '11/23/2019');
insert into stock (id, inv_id, stock, created_at) values (20, 12, 3447.28, '9/12/2020');
insert into stock (id, inv_id, stock, created_at) values (21, 6, 5731.3, '9/24/2019');
insert into stock (id, inv_id, stock, created_at) values (22, 13, 1671.89, '5/23/2019');
insert into stock (id, inv_id, stock, created_at) values (23, 29, 5380.14, '4/25/2019');
insert into stock (id, inv_id, stock, created_at) values (24, 15, 2962.08, '7/15/2019');
insert into stock (id, inv_id, stock, created_at) values (25, 19, 2821.84, '1/31/2019');
insert into stock (id, inv_id, stock, created_at) values (26, 20, 5532.23, '8/25/2020');
insert into stock (id, inv_id, stock, created_at) values (27, 7, 8098.29, '11/16/2019');
insert into stock (id, inv_id, stock, created_at) values (28, 12, 4895.13, '3/12/2020');
insert into stock (id, inv_id, stock, created_at) values (29, 27, 2355.97, '8/7/2019');
insert into stock (id, inv_id, stock, created_at) values (30, 27, 9066.83, '9/2/2020');
insert into stock (id, inv_id, stock, created_at) values (31, 2, 3999.27, '1/27/2019');
insert into stock (id, inv_id, stock, created_at) values (32, 13, 92.75, '8/28/2020');
insert into stock (id, inv_id, stock, created_at) values (33, 23, 6697.54, '4/5/2019');
insert into stock (id, inv_id, stock, created_at) values (34, 20, 6723.54, '6/29/2020');
insert into stock (id, inv_id, stock, created_at) values (35, 11, 7946.35, '7/27/2019');
insert into stock (id, inv_id, stock, created_at) values (36, 27, 9774.26, '7/5/2019');
insert into stock (id, inv_id, stock, created_at) values (37, 21, 4724.6, '1/11/2020');
insert into stock (id, inv_id, stock, created_at) values (38, 1, 1302.91, '2/10/2019');
insert into stock (id, inv_id, stock, created_at) values (39, 28, 7218.72, '3/16/2020');
insert into stock (id, inv_id, stock, created_at) values (40, 22, 7930.9, '10/5/2020');

    """)
    cur.execute("SELECT * FROM stock;")
    cur.fetchall()
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

