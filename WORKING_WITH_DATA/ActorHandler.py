#!/usr/bin/python3
import xml.sax
class ActorHandler( xml.sax.ContentHandler ):
   def __init__(self):
      self.CurrentData = ""
      self.first_name = ""
      self.last_name = ""
      self.birth_date = ""
      self.role = ""

   # Call when an element starts
   def startElement(self, tag, attributes):
      self.CurrentData = tag
      if tag == "actor":
         print ("*****Actor*****")

   # Call when an elements ends
   def endElement(self, tag):
      if self.CurrentData == "first_name":
         print ("First name:", self.first_name)
      elif self.CurrentData == "last_name":
         print ("Last name:", self.last_name)
      elif self.CurrentData == "birth_date":
         print ("Born:", self.birth_date)
      elif self.CurrentData == "role":
         print ("Role:", self.role)
      self.CurrentData = ""

   # Call when a character is read
   def characters(self, content):
      if self.CurrentData == "first_name":
         self.first_name = content
      elif self.CurrentData == "last_name":
         self.last_name = content
      elif self.CurrentData == "birth_date":
         self.birth_date = content
      elif self.CurrentData == "role":
         self.role = content

