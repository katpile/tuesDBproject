import psycopg2
import psycopg2.extras

conn = psycopg2.connect(host='localhost', port=6543, database='tues', user='alex', password='Alex')
with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as c:
    c.execute("select * from \"firstApp_person\" p join \"firstApp_personidcard\" pid on p.id_card_id = pid.id  where p.id=1")
    res = c.fetchall()
    resDct = [{"id":1,"name":"alex"}, {"id":2, "name":"pesho"}]
    for row in res:
        # print(row.__class__)
        resDct.append(dict(row))
    print(resDct)
    