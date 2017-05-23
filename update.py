from sys import argv
import os
def get_extention(filename = ""):
	str_length = len(filename)
	str_copad = ""
	str_copadf = ""
	kk = 0
	xm = str_length
	for x in range (1, str_length):
		str_copad += filename[(xm-x)]
		if (filename[(xm-x)] == "."): 
			kk = len(str_copad) - 1
			for y in range(0, len(str_copad)):
				str_copadf += str_copad[(kk-y)]
			break
		
		
	return str_copadf
	
def get_tag_pos(__starting_tagp = 1, __ending_tagp = 1, __file_contents = "", __stag = '<!--- HEADER --->', __etag = '<!--- /HEADER --->'):
	starting_tag_pos = 0
	ending_tag_pos = 0
	stag_comp = ""
	etag_comp = ""
	found_stag_pos = 0
	found_etag_pos = 0
	fcontents_c = len(__file_contents)
	for x in range(0, fcontents_c):
		for y in range(0, len(__stag)):
			if (found_stag_pos == 1 or (fcontents_c - x) < len(__stag)):
				break
			stag_comp += __file_contents[(x+y)]
		for z in range(0, len(__etag)):
			if (found_etag_pos == 1 or (fcontents_c - x) < len(__etag)):
				break
			etag_comp += __file_contents[(x+z)] 
			
		if (stag_comp == __stag):
			starting_tag_pos = x
			found_stag_pos = 1
			
		if (etag_comp == __etag):
			ending_tag_pos = x
			found_etag_pos = 1
			
		stag_comp = ""
		etag_comp = ""

	return starting_tag_pos, ending_tag_pos, found_stag_pos, found_etag_pos
	
def is_extention(__extention, __comp):
	if (__extention == __comp): return 1
	if (__extention != __comp): return 0
import sys
if __name__ == "__main__":
	icommand = ""
	directory = "L:\BTEC Level 1 Diploma in IT\L1-IT Creating a Website\QuantaGaming"
	file_contents = ""
	file_instance = None
	file_path = ""
	while(0 != 1):
		icommand = raw_input("Please Enter the Method: ")
		if (icommand == "nav"):
			for root, directories, files in os.walk(directory):
				for filename in files:
					if (is_extention(get_extention(filename), ".html") == 1):
						file_path = (directory + "\\" + filename)
						file_instance = open(file_path, "r");
						file_contents = file_instance.read()
						starting_tag = "<!--- HEADER --->"
						ending_tag = "<!--- /HEADER --->"
						starting_tag_pos = 0
						ending_tag_pos = 0
						found_stag_pos = 0
						found_etag_pos = 0
						
						print("Finnding tags in: ", filename)
						starting_tag_pos, ending_tag_pos, found_stag_pos, found_etag_pos = get_tag_pos(1, 1, file_contents, starting_tag, ending_tag)
						
						if (found_stag_pos == 1):
							for i in range(starting_tag_pos, starting_tag_pos+len(starting_tag)):
								sys.stdout.write(file_contents[i])
							
						print("")
						if (found_stag_pos == 1 and found_etag_pos == 1):
							for k in range(starting_tag_pos, ending_tag_pos):
								sys.stdout.write(file_contents[k])
								
						print("")
						
						if (found_etag_pos == 1):
							for o in range(ending_tag_pos, ending_tag_pos+len(ending_tag)):
								sys.stdout.write(file_contents[o])
							
						print(starting_tag_pos, ending_tag_pos)
					else:
						print("ERROR")
			icommand = ""
				
			#tmp = open("foo.txt", "wb");
			
		
	