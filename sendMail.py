import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import sqlite3

sender_email = "*****"
password = "********"

message = MIMEMultipart("alternative")
message["Subject"] = "Leading pace Running analysis and metrics web app"
message["From"] = sender_email



def select_all_emails():
    conn=sqlite3.connect("profiles.db")
    cur = conn.cursor()
    cur.execute("SELECT email FROM profiles WHERE status='scraped'")
    rows = cur.fetchall()
    conn.close()
    return (rows)

def update(email):
    conn=sqlite3.connect("profiles.db")
    cur=conn.cursor()
    cur.execute("UPDATE profiles SET status='one_sent' WHERE email=?",(email,))
    conn.commit()
    conn.close()
# Create the plain-text and HTML version of your message
text = """\

"""

# Turn these into plain/html MIMEText objects
part1 = MIMEText(text, "plain")
part2 = MIMEText(html, "html")

# Add HTML/plain-text parts to MIMEMultipart message
# The email client will try to render the last part first
message.attach(part1)
message.attach(part2)

emails= select_all_emails() 
emails = [mail for (mail,) in emails]

mailTarget = int(input("how many mails to send?  :"))


noMails = 0
# Create secure connection with server and send email
context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(sender_email, password)
    for mail in emails:
        if len(mail)>4:
            try:
                
                if noMails<mailTarget:
                    server.sendmail(
                        sender_email, mail, message.as_string()
                    )
                    update(mail)
                    noMails = noMails + 1
                    print(noMails,"----",mail)
                else:
                    print("done")
                    break
            except:
                print("something went wrong with",mail)
