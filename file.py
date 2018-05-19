def fileopen (path,mode)
fp = open("path","mode")
status = fp.closed
name = fp.name
tu = {'name':name, 'status': status}
print (tu)