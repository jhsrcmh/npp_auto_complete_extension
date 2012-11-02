#encoding=utf-8
'''
	Powered by twins in HIT
	@Date:2012.11.1.pm
	So, if we want to make the plugins of the notepad++, of course we can
	Change the file in the xml directory which contains the footer.xml and 
	Header.xml and put the new file into the directory of the notepad++, webbrowser
	Can get a new world!
'''
import sys

def get_lines(filename):

	'''
		getlines of a file
	'''
	strl =""
	f=file(filename)
	while True:
		line=f.readline()
		if len(line) != 0:
			strl+=line
		else:
			break
	return strl
def write_to_xml(dictory=dict()):
	
	'''
		read and write the dict to the file, but if we want to make the detail autocomplete, we should make the tuple
	'''
	str_first='<Overload retVal="void" >'+'\n'
	str_last='\t\t\t'+'</Overload>'+'\n'+'\t\t'+'</KeyWord>\n'
	str_temp=""
	str_list=[]
	for i, j in dictory.items():
		str_list.append(i)
	str_list.sort()
	
	for i in str_list:
		str_temp+='\t\t'+'<KeyWord name="'+i+'" func="yes">'+'\n\t\t\t'+str_first+'\t\t\t\t'+'<Param name="'+dictory[i].strip()+'"/>\n'+str_last
	return str_temp
	
def print_dict(a=dict()):
	
	'''to print a dictory'''
	for i,j in a.items():
		print i,"is",j,
			
class File:
	'''
		Define the file class and make the operation of the file
	'''
	def __init__(self, filename):
		self.filename=filename
		print 'file init successfully'
	def read_line(self):
		'''
			Read the file
		'''
		f=file(self.filename)
		while True:
			line = f.readline()
			if len(line) != 0:
				print line,
			else:
				break
		f.close
	
	def read_line_to_dict(self):
		
		'''
			Read from a file and make the pip of the file
			@return dict
		'''
		dict_of_function=dict()
		f=file(self.filename)
		while True:
			line = f.readline()
			if len(line)!= 0:
				#split by "\t"
				stringtemp= line.split("\t")
				
				#It's the split we can find
				if len(stringtemp) == 2:
					dict_of_function[stringtemp[0]]=stringtemp[1]
			else:
				break
		f.close()
		return dict_of_function
		
	def get_new_xml(self,outputname="matlab.xml",a={}):
		
		'''
			Write the dict to the file
		'''
		filename1="xml/header.xml"
		filename2="xml/footer.xml"
		temp=get_lines(filename1)
		temp+=write_to_xml(a)
		temp+=get_lines(filename2)
		f = file(outputname,'w')
		f.writelines(temp)
		f.close()
		
	def __del__(self):
		print 'file destory successfully'

# p= File("poem.txt")
# a=p.read_line_to_dict()
# p.get_new_xml("matlab.xml",a)
if __name__ == "__main__":  
	if len(sys.argv) < 2:
		print 'No choice you can make\n'
		sys.exit()
	if sys.argv[1].startswith('--'):
		op=sys.argv[1][2:]
		if op=='version':
			print 'auto_make_npp 1.0\n'
		elif op=='help':
			print '''
This program is designed for the studiers 
in matlab at first, because I cant't find 
a tool that can serve me for the function's
auto complete.
Option is list as follows:
	--version: Print the version of the 
	program.
	--help   : Print the help messages
	args: ./file_operate funciton_list.txt output.xml
			'''
		else:
			print 'Sorry, you should check you argument.\n'
		sys.exit()
	if len(sys.argv) == 3:
		pfile=File(sys.argv[1].strip())
		aread=pfile.read_line_to_dict()
		pfile.get_new_xml(sys.argv[2].strip(), aread)
	else:
		pass
	sys.exit()