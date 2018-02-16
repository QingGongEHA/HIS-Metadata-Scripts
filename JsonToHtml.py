import json
from json2html import *
import os

file_json = open('E:\MoH Interoperability\HIS Metadata\HMIS-DHIS2\DHIS2 Metadata-splitted\userGroups.json') #replace with the .json file you want to convert
data_json = json.load(file_json)
result_html = json2html.convert(json = data_json, table_attributes="class=\"table table-bordered table-hover\"").encode('utf-8')

file_html = open('E:\MoH Interoperability\HIS Metadata\HMIS-DHIS2\DHIS2 Metadata-splitted\userGroups.html','w') #replace with the same directory as in line 5 but with .html as extension. 
file_html.write(result_html)

file_html.close()
