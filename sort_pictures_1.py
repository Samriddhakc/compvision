import os
import pickle

#folder_path='/nfs/sleipnir2/ExpediaHotels/'
folder_path='/home/kc/Desktop/'
os.chdir(folder_path)

#file_name='hotel.txt'
#file_name='ActivePropertyList.txt'
file_name="dummy_2.txt"

import os.path
file_1=open(file_name,'r')
text=file_1.read()
os.chdir('/home/kc/Desktop/scrapped_data')
with open('obj_1.pkl','wb') as f:
        pickle.dump([text],f)


#images=[f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path,f))]
#print(len(images))
#folder_path='/nfs/sleipnir2/ExpediaHotels/Bathroom'


