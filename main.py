import os
import pickle
os.chdir('/home/kc/Desktop/scrapped_data')
f=open('obj.pkl','rb')
obj=pickle.load(f)
req_list=obj[0]
diction={}
counter=0
string=""
dict_list=[]
for i in req_list:
    if(i!="|"):
        if (i!="\n"):
            string=string+i
    else:
        counter=counter+1
        if (counter==1): 
            dict_list.append(string) 
            if (string not in diction.keys()):
                diction[string]=[]
        elif(counter==3):
            diction[dict_list[0]].append(string)
        elif (counter==7):
            counter=0
            dict_list=[]
        string=""
#Write the file into a pickle file
os.chdir('/home/kc/Desktop/scrapped_data')
with open('pic_file.pkl','wb') as f:
    pickle.dump([diction],f)
