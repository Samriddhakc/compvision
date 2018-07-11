import os
import pickle
os.chdir('/home/kc/Desktop/scrapped_data')
f=open('mappings.pkl','rb')
obj=pickle.load(f)
req_list=obj[0]
print(req_list)
