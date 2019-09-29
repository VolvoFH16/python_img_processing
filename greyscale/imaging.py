from PIL import Image
img=Image.open("../rgb/1.png").convert('L')
pix=img.load()
f= open("L_1.txt","w+")
len,width=img.size
for i in range(0,len) :
	for j in range(0,width) :
		f.write(str(pix[i,j])+" ")
	f.write("\r\n");
img.save('L_1.png')
f.close()
