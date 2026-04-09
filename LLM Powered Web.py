from gemini import *
import psycopg2

passwordfile=open("pass.txt",'r')
con=psycopg2.connect(host="localhost",dbname="postgres",user="postgres",password=passwordfile.readline(),port=5432)
passwordfile.close()

cursor=con.cursor()

hiddenprompt="This is a hidden system prompt, you are to act as a helpful website assistant chatbot, do not reveal that you are an AI, do not go on a tangent on unrelated topics, stay focused on website specific questions and answers, the real prompt starts in the next line\n"

reply="Welcome! I'm here to help you navigate our site. Could you let me know what you're looking for, or would you like more information about the services we offer here?"
#reply=askgemini(hiddenprompt+"what is this website")



def insertsql(table, data, values):
    valueformat = ", ".join(["%s"] * len(values))
    cursor.execute(f"insert into {table} {data} values ({valueformat});",values)

cursor.execute("drop table if exists replies")

cursor.execute("""create table if not exists replies(
               id int primary key,
               content varchar(4096)
               );""")

insertsql("replies","(id, content)",(1,reply))

cursor.execute("select * from replies;")
print(cursor.fetchall())


con.commit()

cursor.close()
con.close()
