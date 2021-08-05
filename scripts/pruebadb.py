from utilidades import obtenerSHA1 , sacarGrabaciones

import sys #para currar con argumentos
import psycopg2
import wget
import os # para poder ejecutar clear en consola
import urllib #para poder descargar fichero de forma alternativa a wget

#lastc
conn= psycopg2.connect("dbname=moodle2021 user=moodle2021 host=156.35.233.163 password=91937852748688a368b5a710c3c3ad6c")
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

#borrar pantalla
os.system('clear')

#ahora obtengo el sha1 necesario 
secret='usmJEqowjsDrpDX4vsfzucIcJNtRrvoqlPj3ShYF7cY'
server='https://conferenciasweb.uniovi.es/bigbluebutton/'

#poner el listaMeetingID[del que queremos obtener recordigs]
cadena='getRecordingsmeetingID='+listaMeetingID[2]+secret

sha1=obtenerSHA1(cadena)

#print(sha1)
#a continuacion poner el listaMeetingID[que queramos obtener recordings]
urlDescargaXMLrecordings = server+'api/getRecordings?meetingID='+listaMeetingID[2]+'&checksum='+sha1
#print(urlDescargaXMLrecordings)

#wget.download(urlDescargaXMLrecordings,'recordings.xml')
urllib.request.urlretrieve(urlDescargaXMLrecordings,'recordings.xml')

#print ("descarga de xml realizada para meetingID = "+listaMeetingID[0])

sacarGrabaciones("recordings.xml")

