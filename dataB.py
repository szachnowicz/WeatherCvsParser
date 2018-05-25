import sqlite3


def create():
    try:
        c.execute("CREATE TABLE `User` ( `id` INTEGER, `name` TEXT NOT NULL, `last_name` TEXT NOT NULL, `age` INTEGER NOT NULL, `time_id` INTEGER UNIQUE, PRIMARY KEY(`id`) )""")
    except:
        pass


def insert():
    c.execute("""INSERT INTO User (name,last_name,age) values('Janusz','Tracz',60)""")


def select(verbose=True):
    sql = "SELECT * FROM User"
    recs = c.execute(sql)
    if verbose:
        for row in recs:
            print(row)


db_path = r'time.db'
conn = sqlite3.connect(db_path)
c = conn.cursor()
create()
insert()
conn.commit()  # commit needed
select()
c.close()
