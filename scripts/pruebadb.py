import psycopg2
#lastc
conn= psycopg2.connect("dbname=moodle2021 user=moodle2021 host=156.35.233.163 password=91937852748688a368b5a710c3c3ad6")
cur=conn.cursor()
cur.execute("select * from mdl_course where id=7951")

curso = cur.fetchone()
print(curso)
print ("imprimir todas las actividades del curso")
cur.execute("select meetingid,course,id from mdl_bigbluebuttonbn where course=7951")
listaActividades=cur.fetchall()


listaMeetingID=[]
for actividad in listaActividades:
    meetingID=actividad[0]+'-'+str(actividad[1])+'-'+str(actividad[2])
    listaMeetingID.append(meetingID)





#hacer cambios persistentes
conn.commit()
#cerrar la comunicacion con la bd
cur.close()
conn.close()

