from xml.dom import minidom
myxmlfile='C:\\Users\\Admin\\Documents\\GitHub\\python_for_qa_synechron\\resumeXML\\resume_w_xsl.xml'
a=minidom.parse(myxmlfile)
print(a.childNodes)
for node in a.getElementsByTagName("short_desc"):
	print(node.firstChild.data)
