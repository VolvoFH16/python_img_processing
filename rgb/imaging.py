from PIL import Image
img=Image.open("1.png")
pix=img.load()
f= open("rgb_1.txt","w+")
len,width=img.size
for i in range(0,len) :
	for j in range(0,width) :
		f.write("("+str(pix[i,j][0])+","+str(pix[i,j][1])+","+str(pix[i,j][2])+")")
	f.write("\r\n");
f.close()
