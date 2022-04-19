# Pythono3 code to rename multiple
# files in a directory or folder

# importing os module
import os
from sys import argv
import os.path
import math

#dump_time = 1000
# Function to rename multiple files
def main():
        dump_time = input("Enter dump every N cycles: ")
        chop = int(math.log10(int(dump_time)))
        jump = int(dump_time)/10**chop
        print('jump = ', jump)
        folder_name = argv
        default_folder = '/media/vancleve/Disk2/examples/'
        folder = default_folder+'%s' %(folder_name)[1]+'/'
        name_list=os.listdir(folder)
        name_list_size = []
        for name in name_list:
          if (name[-4:] == ".jpg" and name[6:9] != "top"):
            name_list_size.append(len(name))
          #elif(name[6:9] == "top"):
          #  print(name)
        maxi = max(name_list_size)
        same = 0
        diff = 0
        end1 = 0
        end2 = 0
        diffA = []
        n = 1
        Zarray = []
        print(folder)       
        for count, filename in enumerate(os.listdir(folder)):
          if (filename[-4:] == ".jpg" and filename[6:9] != "top"):    
            f = filename
            if n == 1:
              print('filename center = ',filename[6:9])
              print('filename = ', filename)
              n = 2
            len_file_name = len(filename)
            zeros = -len_file_name+maxi
            Zarray.append(zeros)
            zero_string = ""
            if zeros==0:
              same +=1
            else:
              diff +=1
              diffA.append(len_file_name)
            for z in range(zeros+1):
              zero_string=zero_string+"0"
            end = len_file_name-chop-4
            start_s = f[6:end]
            #print('end = ',end)
            if jump != 1:
              start_n = int(start_s)/jump
              start_n = int(start_n)
              mod_s = str(start_n)
              l_diff = len(start_s) - len(mod_s)
              if l_diff > 0:
                z_start = ""
                for i in range(l_diff):
                  z_start = "0"+z_start
                mod_s = z_start+mod_s
              start_s = mod_s
              dst = folder+f[0:6]+zero_string+start_s+".jpg"
            else:
              dst = folder+f[0:6]+zero_string+f[6:end]+".jpg"
            #print(f[0:6]+"0"+f[6:8]+".jpg")  
#            if len(filename) == 15:
              #f[6:8] is for every 1000 images, f[6:9] is for every 100 images
#              dst = folder+f[0:6]+"00000"+f[6:end]+".jpg"  
#            elif len(filename) == 16:
#              dst = folder+f[0:6]+"0000"+f[6:end+1]+".jpg"
#            elif len(filename) == 17:
#              dst = folder+f[0:6]+"000"+f[6:end+2]+".jpg"
#            elif len(filename) == 18:
#              dst = folder+f[0:6]+"00"+f[6:end+3]+".jpg"
#            elif len(filename) == 19:
#              dst = folder+f[0:6]+"0"+f[6:end+4]+".jpg"
              #print("file 16")
            src =folder+f
            #print(dst)
        # rename() function will
        # rename all the files
            os.rename(src,dst)
        print("min size = ",min(diffA))
        print("max size = ",max(diffA))
        print("min size Zarray= ",min(Zarray))
        print("max size Zarray= ",max(Zarray))
        print("same = ",same)
        print("diff = ", diff)
        print("max = ",maxi)
        print('number of digits = ', maxi-12)
        print("done")

# Driver Code
if __name__ == '__main__':
	
	# Calling main() function
	main()

