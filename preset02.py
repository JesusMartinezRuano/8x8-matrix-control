import requests

s = requests.Session()
s.get('http://192.168.0.178/cgi-bin/MUH44TP_getsetparams.cgi',auth=('admin','admin'))

print (s.cookies)

s.post('http://192.168.0.178/cgi-bin/MMX32_Keyvalue.cgi',auth=('admin','admin'),data='{CMD=PresetRecall02.')