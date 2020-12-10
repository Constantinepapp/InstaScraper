import pickle
import urllib.request,re
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

profiles = select_all_tasks()
profiles = [item for (item,) in profiles]
total = len(profiles)
i = 0
emails = 0
for item in profiles:
    print(i," of ",total)
    
    try:
        site = "https://www.instagram.com/"+item+"/"
        update_status(item)
        f = urllib.request.urlopen(site)
        s = f.read()
        emails = re.findall(b"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4}",s)
        try:
            update(item,emails[0].decode('utf-8'))
            emails = emails + 1
            print(emails)
        except:
            pass
    except:
        pass
    i = i + 1
    
    #newemails = list(set(emails))
    #print (newemails)
    


    
    