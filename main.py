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
    cur.execute("""create table inventories (
	id INT,
	name VARCHAR(50),
	bp DECIMAL(7,2),
	sp DECIMAL(7,2),
	type VARCHAR(10)
);
insert into inventories (id, name, bp, sp, type) values (1, 'Mushroom - Morels, Dry', 2477.77, 3468.878, 'fruits');
insert into inventories (id, name, bp, sp, type) values (2, 'Scallops - 20/30', 2232.52, 3125.528, 'fruits');
insert into inventories (id, name, bp, sp, type) values (3, 'Turkey - Oven Roast Breast', 8230.33, 11522.462, 'vegetables');
insert into inventories (id, name, bp, sp, type) values (4, 'Spring Roll Wrappers', 4008.56, 5611.984, 'fruits');
insert into inventories (id, name, bp, sp, type) values (5, 'Gingerale - Schweppes, 355 Ml', 7473.83, 10463.362, 'fruits');
insert into inventories (id, name, bp, sp, type) values (6, 'Puff Pastry - Slab', 6380.64, 8932.896, 'vegetables');
insert into inventories (id, name, bp, sp, type) values (7, 'Lid - Translucent, 3.5 And 6 Oz', 2836.14, 3970.596, 'vegetables');
insert into inventories (id, name, bp, sp, type) values (8, 'Beer - Mcauslan Apricot', 9740.62, 13636.868, 'fruits');
insert into inventories (id, name, bp, sp, type) values (9, 'Pastry - Baked Scones - Mini', 6047.61, 8466.654, 'fruits');
insert into inventories (id, name, bp, sp, type) values (10, 'Bread - White, Sliced', 8987.62, 12582.668, 'fruits');
insert into inventories (id, name, bp, sp, type) values (11, 'Table Cloth 54x54 White', 5243.56, 7340.984, 'vegetables');
insert into inventories (id, name, bp, sp, type) values (12, 'Napkin - Beverge, White 2 - Ply', 6815.01, 9541.014, 'vegetables');
insert into inventories (id, name, bp, sp, type) values (13, 'Sugar - Individual Portions', 6066.86, 8493.604, 'vegetables');
insert into inventories (id, name, bp, sp, type) values (14, 'Sauce - Hoisin', 4533.05, 6346.27, 'vegetables');
insert into inventories (id, name, bp, sp, type) values (15, 'Chilli Paste, Ginger Garlic', 4835.75, 6770.05, 'fruits');
insert into inventories (id, name, bp, sp, type) values (16, 'Rice - Aborio', 2949.63, 4129.482, 'fruits');
insert into inventories (id, name, bp, sp, type) values (17, 'Vegetable - Base', 1150.02, 1610.028, 'vegetables');
insert into inventories (id, name, bp, sp, type) values (18, 'Cilantro / Coriander - Fresh', 1009.11, 1412.754, 'fruits');
insert into inventories (id, name, bp, sp, type) values (19, 'Wine - Ej Gallo Sonoma', 3278.04, 4589.256, 'vegetables');
insert into inventories (id, name, bp, sp, type) values (20, 'Cafe Royale', 9873.15, 13822.41, 'vegetables');
insert into inventories (id, name, bp, sp, type) values (21, 'Lemonade - Kiwi, 591 Ml', 5318.15, 7445.41, 'fruits');
insert into inventories (id, name, bp, sp, type) values (22, 'Chocolate - Milk Coating', 2922.98, 4092.172, 'vegetables');
insert into inventories (id, name, bp, sp, type) values (23, 'Butter - Salted, Micro', 8050.95, 11271.33, 'vegetables');
insert into inventories (id, name, bp, sp, type) values (24, 'Nut - Pecan, Halves', 1692.34, 2369.276, 'vegetables');
insert into inventories (id, name, bp, sp, type) values (25, 'Cactus Pads', 3498.4, 4897.76, 'vegetables');
insert into inventories (id, name, bp, sp, type) values (26, 'Table Cloth 54x72 White', 5476.9, 7667.66, 'fruits');
insert into inventories (id, name, bp, sp, type) values (27, 'Cheese - Victor Et Berthold', 1405.51, 1967.714, 'vegetables');
insert into inventories (id, name, bp, sp, type) values (28, 'Juice - Apple, 341 Ml', 8253.34, 11554.676, 'vegetables');
insert into inventories (id, name, bp, sp, type) values (29, 'Tuna - Salad Premix', 9656.04, 13518.456, 'fruits');
insert into inventories (id, name, bp, sp, type) values (30, 'Lettuce - California Mix', 2049.03, 2868.642, 'vegetables');

                """)


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

