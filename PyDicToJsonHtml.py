import json
from ast import literal_eval
from json2html import *

#open the original file that needs to be converted
original_file = open("E:\MoH Interoperability\HIS Metadata\LIS-Bika\Patients.txt")  #replace with original data from Bika

#read data from original file
unicode_python_dic = original_file.read()

#convert unicode python dictionary to normal python dictionary
normal_python_dic = literal_eval(unicode_python_dic)

#convert python dictionary to json
json_result = json.dumps(normal_python_dic, ensure_ascii=False) 

#open and write to file
json_file = open("E:\MoH Interoperability\HIS Metadata\LIS-Bika\Patients.json", "w")  #replace with the json file name

json_file.write(json_result)

#close opened files
original_file.close()
json_file.close()


#open json file 
file_json = open('E:\MoH Interoperability\HIS Metadata\LIS-Bika\Patients.json')  #replace with the json file name

#load to json data
data_json = json.load(file_json)

#convert json to html
result_html = json2html.convert(json = data_json, table_attributes="class=\"table table-bordered table-hover\"")

#create and write to html file
file_html = open('E:\MoH Interoperability\HIS Metadata\LIS-Bika\Patients.html','w')  #replace with html file name
file_html.write(result_html)

#close opened files
file_html.close()