import json
import simplejson as json
from json2html import *
import os

file_json = open('D:\MoH Interoperability\HIS Metadata\HMIS-DHIS2\DHIS2 Metadata-splitted\\dashboardItems.json') #replace with the path and file you want to convert
data_json = json.load(file_json)
result_html = json2html.convert(json = data_json, table_attributes="class=\"table table-bordered table-hover\"").encode('utf-8')

file_html = open('D:\MoH Interoperability\HIS Metadata\HMIS-DHIS2\DHIS2 Metadata-splitted\\dashboardItems.html','w') #replace with the path where you want to see the result, replace the file name with how you want to call the result
file_html.write(result_html)

file_html.close()
