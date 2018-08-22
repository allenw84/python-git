# coding=utf-8   //設置文本格式
import os,sys
import json 
from collections import OrderedDict
import codecs
'''
data1 = {
    'name' : 'ACME',
    'shares' : 100,
    'price' : 542.23
}
'''
with open('Safety.json','r') as f :
	data = json.load(f,object_pairs_hook=OrderedDict) #按照順序
#print(json.dumps(data, indent=4)) #縮排
dic = {}
def json_edit(dic_json):   #first time to parse 
	if isinstance(dic_json,dict):
		#print(json.dumps(dic_json))
		for key in dic_json:
			#print(json.dumps(dic_json[key]))
			if isinstance(dic_json[key],dict):
				json_ParsrTheDict(dic_json[key])
			elif isinstance(dic_json[key],list):
				#print(json.dumps(dic_json[key]))
				json_ParseTheList(dic_json[key])
			else:
				print('')
			'''
			if isinstance(dic_json[key],dict):
				print(key)
				print(dic_json[key])
				#print ('key'+ key + 'value' + dic_json[key])
				json_edit(dic_json[key])
				dic[key] = dic_json[key]
			else:
				#print ('key'+ key + 'value' + dic_json[key])
				dic[key] = dic_json[key]
			'''	
def json_ParseTheList(dic_json):
	#print('List')
	
	edit_key(dic_json)
	
def json_ParsrTheDict(dic_json):
	#print('Dict')
	edit_key(dic_json)

def edit_key(edic_json):
	if isinstance(edic_json,dict):
		for key in edic_json:
			if key == sh_key : #sh_key
				edic_json[key] = sh_value #sh_value #Safety_in_here
				print('checkOut')
			elif isinstance(edic_json[key],dict):
					json_ParsrTheDict(edic_json[key])
			elif isinstance(edic_json[key],list):
					json_ParseTheList(edic_json[key])
	elif isinstance(edic_json,list):
		for key in range(len(edic_json)):
			if key == sh_key : #sh_key
				edic_json[key] = sh_value #sh_value
				print('checkOut')
			elif isinstance(edic_json[key],dict):
					json_ParsrTheDict(edic_json[key])
			elif isinstance(edic_json[key],list):
					json_ParseTheList(edic_json[key])
	
#print('dic--'+ str(dic))


if __name__ == '__main__':
	sh_key  = 'lifecycle_events'
	sh_value = sys.argv[1]
	json_edit(data)
	print(json.dumps(data, indent=4))
	with codecs.open('new.json','w','utf8') as newfile: #codecs可輸入中文字
		str = json.dumps(data, indent=4) #中文 ,ensure_ascii=False
		newfile.write(str)
