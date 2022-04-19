# Pythono3 code to rename multiple
# files in a directory or folder

# importing os module
import os

# Function to rename multiple files
def main():

        folder = "./"
        for count, filename in enumerate(os.listdir(folder)):
          if filename[-4:] == ".jpg":    
            f = filename
            #print(f[0:6]+"0"+f[6:8]+".jpg")
            if len(filename) == 15:
              dst = folder+f[0:6]+"00"+f[6:8]+".jpg"
            elif len(filename) == 16:
              dst = folder+f[0:6]+"0"+f[6:9]+".jpg"
              #print("file 16")
            src =folder+f
            #print(dst)
        # rename() function will
        # rename all the files
            os.rename(src,dst)
        print("done")

# Driver Code
if __name__ == '__main__':
	
	# Calling main() function
	main()

