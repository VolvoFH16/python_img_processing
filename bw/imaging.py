from PIL import Image
img=Image.open("../rgb/1.png").convert('1')
pix=img.load()
f= open("BW_1.txt","w+")
len,width=img.size
img.show()
for i in range(0,len) :
	for j in range(0,width) :
		if pix[i,j]==255 :
			f.write(str(1)+" ")
		else :
			f.write(str(pix[i,j])+" ")
	f.write("\r\n");
img.save('BW_1.png')
f.close()
