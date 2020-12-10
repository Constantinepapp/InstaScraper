import sqlite3



def select_all_tasks():
    conn=sqlite3.connect("profiles.db")
    cur = conn.cursor()
    cur.execute("SELECT name FROM profiles WHERE status='not scraped for emails'")
    rows = cur.fetchall()
    conn.close()
    return (rows)

def update(name,email):
    conn=sqlite3.connect("profiles.db")
    cur=conn.cursor()
    cur.execute("UPDATE profiles SET email=? WHERE name=?",(email,name))
    conn.commit()
    conn.close()

def update_status(name):
    conn=sqlite3.connect("profiles.db")
    cur=conn.cursor()
    cur.execute("UPDATE profiles SET status='scraped' WHERE name=?",(name,))
    conn.commit()
    conn.close()


def insert(link,scraped):
    conn=sqlite3.connect("profiles.db")
    cur=conn.cursor()
    cur.execute("INSERT OR REPLACE INTO sources VALUES(?,?)",(link,scraped))
    conn.commit()
    conn.close()
    
def check_if_exists(link):

    conn=sqlite3.connect("profiles.db")
    cur=conn.cursor()
    link_exists = cur.execute('SELECT 1 FROM sources WHERE link="%s" LIMIT 1' % link)
    link_exists = cur.fetchone() is not None
    return (link_exists)


add_link = input("add source link ('end' to stop): ")

while add_link != "end":
    checker = check_if_exists(add_link)
    if checker == False:
        insert(add_link,0)
        print('success')
    else:
        print('already in database')
    add_link = input("add source link ('end' to stop): ")