import psycopg2

def create_table():
    conn = psycopg2.connect("dbname='database1' user='postgres' password='postgres123' host='localhost' port='5432'")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")
    conn.commit()
    conn.close()


def insert(item,quantiy,price):
    conn = psycopg2.connect("dbname='database1' user='postgres' password='postgres123' host='localhost' port='5432'")
    cur = conn.cursor()
    #cur.execute("INSERT INTO store VALUES ('%s','%s','%s')" % (item,quantiy,price))
    cur.execute("INSERT INTO store VALUES (%s,%s,%s)" , (item, quantiy, price))
    conn.commit()
    conn.close()


def view():
    conn = psycopg2.connect("dbname='database1' user='postgres' password='postgres123' host='localhost' port='5432'")
    cur = conn.cursor()
    cur.execute("SELECT * FROM store")
    rows = cur.fetchall()
    conn.close()
    return rows


def update(quantity,price,item):
    conn = psycopg2.connect("dbname='database1' user='postgres' password='postgres123' host='localhost' port='5432'")
    cur = conn.cursor()
    cur.execute("UPDATE store set quantity=%s, price=%s WHERE item=%s",(quantity,price,item))
    conn.commit()
    conn.close()


#update(11,10,"Water bottle")
#print(view())
create_table()
#insert("Orange",5,80)
update(10,160,"Orange")
print(view())
