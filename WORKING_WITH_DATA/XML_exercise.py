#!/usr/bin/python3
#				"XML"
import xml.dom.minidom 
import xml.sax
from ActorHandler import ActorHandler

path='./data/exemel.xml'
file = xml.dom.minidom.parse(path)
actors = file.getElementsByTagName("actor")
print("			***Original file***")
for actor in actors:
	first_name = actor.getElementsByTagName("first_name")[0]
	last_name = actor.getElementsByTagName("last_name")[0]
	birth_date = actor.getElementsByTagName("birth_date")[0]
	role = actor.getElementsByTagName("role")[0]
	print("Name: %s %s, Born in: %s, Played: %s"%(first_name.firstChild.data, last_name.firstChild.data, birth_date.firstChild.data, role.firstChild.data))

#modify first_name tag's value to "Jeff" and save to a new file
new_path = "./data/exemel_out.xml"
for actor in actors:
	actor.getElementsByTagName("first_name")[0].childNodes[0].nodeValue = "Jeff"
with open(new_path,"w+") as f2:	
	f2.write(file.toxml())
	f2.close()

print("			***Modified file***")

last_path = './data/exemel_final.xml'
parser = xml.sax.make_parser()
parser.setFeature(xml.sax.handler.feature_namespaces, 0)
Handler = ActorHandler()
parser.setContentHandler( Handler )

parser.parse(new_path)
