import os
import pickle
folder_path='/home/kc/Desktop/'
os.chdir(folder_path)
#file_name='ActivePropertyList.txt'
file_name="dummy_2.txt"
import os.path
file_1=open(file_name,'r')
diction={}
counter=0
string=""
for line in file_1:
    dict_list=[]

    for i in line:
        if(i!="|"):
            string=string+i
        else:
            counter=counter+1
            if (counter==1):
                dict_list.append(string)
                if (string not in diction.keys()):
                    diction[string]=[]
            elif(counter==3):
                diction[dict_list[0]].append(string)
            string=""
    string=""
    counter=0
    dict_list=[]
print(diction)
#Write the file into a pickle file
os.chdir('/home/kc/Desktop/scrapped_data')
with open('mappings.pkl','wb') as f:
    pickle.dump([diction],f)



