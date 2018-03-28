import json
import os
from json2html import *

DHIS_metadata = open('C:\pythonCode\metadata.json') #replace with the path to the DHIS2 metadata in json format, which is exported from DHIS2
data = json.load(DHIS_metadata)

file_json = open('C:\pythonCode\CBIS_indicators_JsonArray.json', 'w') #put the file in the folder where you want to see the result

for dataset3 in data:
  if dataset3 == 'indicatorGroups':  
    file_json.write('{')
    for x in data[dataset3]:
	  groupName = x['name']
	  if 'CBIS' in groupName: # to extract metadata of other subsystems (if applicable), replace the keyword "CBIS" with another relevant keyword. 
	    file_json.write('"' + groupName + '": ')  #data element group
	    firstIdElement = True
	    if len(x['indicators']) == 0:  #for situations when the list is empty
		  file_json.write(',')
	    for element in x['indicators']:
		  lastIdElement = x['indicators'][-1]
		  id = element['id']		  
		  for dataset4 in data:
		    if dataset4 == 'indicators':
		      for y in data[dataset4]:			    
			    if y['id'] == id:
				  if firstIdElement == True: 
				    file_json.write('[["' + y['name'].encode('utf-8') + '"')  #indicators
				    firstIdElement = False
				  else:
				    file_json.write(',"' + y['name'].encode('utf-8') + ']"')
				  if element == lastIdElement:
				    file_json.write(']],')
					
					
file_json.seek(-1, os.SEEK_END)  #takes away the last ','
file_json.write('}')
file_json.close()
DHIS_metadata.close()


# Convert JSON to HTML
result_data = open('C:\pythonCode\CBIS_indicators_JsonArray.json') # Open the JSON file; the file should be the same as in line8
result_json = json.load(result_data)
result_html = json2html.convert(json = result_json, table_attributes="class=\"table table-bordered table-hover\"")

file_html = open('C:\pythonCode\CBIS_indicators.html','w') #put the file in the folder where you want to see the result
file_html.write(result_html)

file_html.close()

