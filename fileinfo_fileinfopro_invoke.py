import fileinfo

class FileInfoPro(fileinfo.FileInfo):
	def search(self,searchstring):
		for lno, line in enumerate(self.lines):
			if searchstring in line:
				print(lno + 1,line.rstrip())
				
f=FileInfoPro("input.txt")
f.getsize()
f.getage()
f.getfirstline()
f.getlastline()
f.getnthline(3)
f.getlinecount()
f.search("line")
f.close()
