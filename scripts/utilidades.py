import os
import collections

import fileinput #necesario para reemplazar cadenas como se hace con sed -i
import subprocess

from xml.dom import minidom  #para trabajar con xml

import hashlib #para trabajo con sha

#sustituye una cadena en un fichero por otra nueva
def sustituir(fichero,cadenavieja,cadenanueva):
    subprocess.call(["sed", "-i",'s/'+cadenavieja+'/'+cadenanueva+'/g',fichero])



#sacar un listado con las grabaciones de un fichero xml
def sacarGrabaciones(fichero):
    doc=minidom.parse(fichero)
    grabaciones=doc.getElementsByTagName('recording')

    for grabacion in grabaciones:
        meetingIDunico= grabacion.getElementsByTagName('recordID')[0]
        playbackurl= "https://conferenciasweb.uniovi.es/playback/presentation/2.0/playback.html?meetingId="+meetingIDunico.childNodes[0].data
        print(meetingIDunico.childNodes[0].data)
        print(playbackurl)


#Sustituye el startTime de un recording por uno nuevo  1-10-2021
#calcula el nuevo endTime equivalente
def nuevoStartTime(fichero,startTimeNuevo):
    doc=minidom.parse(fichero)
    grabaciones=doc.getElementsByTagName('recording')

    for grabacion in grabaciones:
        #element startTime
        startTime=grabacion.getElementsByTagName('startTime')[0]
#        print(type(startTime))
        #element endTime
        endTime=grabacion.getElementsByTagName('endTime')[0]
	#node startTimeNode
        startTimeNode=startTime.childNodes[0];
#        print(type(startTimeNode))
        #node endTimeNode
        endTimeNode=endTime.childNodes[0]

#        print("startTimeNode data->"+startTimeNode.data)

        duracion=int(endTimeNode.data)-int(startTimeNode.data)

#        print(endTimeNode.data+"-"+startTimeNode.data+"="+str(duracion))


#        print(str(endTimeNode.data+str(duracion)))
        endTimeNuevo=str(int(startTimeNuevo)+duracion)

        startTimeNode.data=startTimeNuevo
        endTimeNode.data=endTimeNuevo

        #print(doc.toxml())
        f=open(fichero,'w')
        doc.writexml(f)
        f.close()


#ejemplo modificar valor file.getElementsByTagName( "age" )[ 0 ].childNodes[ 0 ].nodeValue = "29"        #



#def obtenerXML(meetingID):
 

def obtenerSHA1(cadena):
    hash_obj = hashlib.sha1(cadena.encode())
    # print (hash_obj.hexdigest())
    return hash_obj.hexdigest()
