import json
import os
from json2html import *

DHIS_metadata = open('E:\MoH Interoperability\HIS Metadata\CBIS-DHIS2\DHIS2-metadata.json') #replace with the path to the DHIS2 metadata in json format, which is exported from DHIS2
data = json.load(DHIS_metadata)

file_json = open('E:\MoH Interoperability\HIS Metadata\CBIS-DHIS2\CBIS_data_in_JsonArray.json', 'w') #put the file in the folder where you want to see the result

for dataset1 in data:
  if dataset1 == 'dataElementGroups':
    file_json.write('{')
    for x in data[dataset1]:
	  groupName = x['name']
	  if 'CBIS' in groupName: # to extract metadata of other subsystems (if applicable), replace the keyword "CBIS" with another relevant keyword. 
	    file_json.write('"' + groupName + '": [')  #data element group
	    firstIdElement = True
	    if len(x['dataElements']) == 0:  #for situations when the list is empty
		  file_json.write('],')
	    for element in x['dataElements']:
		  lastIdElement = x['dataElements'][-1]
		  id = element['id']		  
		  for dataset2 in data:
		    if dataset2 == 'dataElements':
		      for y in data[dataset2]:			    
			    if y['id'] == id:
				  if firstIdElement == True: 
				    file_json.write('{"' + y['name'].encode('utf-8') + '":[" Value Type: ' + y['valueType'].encode('utf-8') + '"]}')  #data elements
				    firstIdElement = False
				  else:
				    file_json.write(',{"' + y['name'].encode('utf-8') + '":[" Value Type: ' + y['valueType'].encode('utf-8') + '"]}')
				  if element == lastIdElement:
				    file_json.write('],')
file_json.seek(-1, os.SEEK_END)  #takes away the last ','
file_json.write('}')
file_json.close()
DHIS_metadata.close()


# Convert JSON to HTML

result_data = open('E:\MoH Interoperability\HIS Metadata\CBIS-DHIS2\CBIS_data_in_JsonArray.json') # Open the JSON file; the file shoud be the same as in line8
result_json = json.load(result_data)
result_html = json2html.convert(json = result_json, table_attributes="class=\"table table-bordered table-hover\"")

file_html = open('E:\MoH Interoperability\HIS Metadata\CBIS-DHIS2\CBIS-Metadata.html','w') #put the file in the folder where you want to see the result
file_html.write(result_html)

file_html.close()
