from PIL import Image

number_to_generate=300
opacity=204

up=False

###########################################################
#                   program
###########################################################
total_height=32*int(number_to_generate/6)
img = Image.new('RGBA', (192, total_height))
frame=Image.open('frame.png')
number_im=[]
for i in range(0,10):
    number_im.append(Image.open('shadow_n/'+str(i)+'.png'))
   
def paste_frame(x,y):
    width, height = frame.size
    box=(x,y,x+width,y+height)
    img.paste(frame, box)
      
   
def paste_digit(i, x, y):
    width, height = number_im[i].size
    box=(x,y,x+width,y+height)
    img.paste(number_im[i], box)

def paste_number(n, x, y):
    split_n = [int(i) for i in str(n)]
    w=7
    reverse = len(split_n)*w
    i=0;
    for digit in split_n:
        paste_digit(digit,x-reverse+i*w,y)
        i+=1
        
def change_img_opacity(val):
    datas = img.getdata()
    newData = []
    for item in datas:
        if(item[3]!=0):
            newData.append((item[0],item[1],item[2],val))
        else:
            newData.append(item)
    img.putdata(newData)
    
for n in range(0,300):
    if(n!=0):
        x=int(n%6)*32
        y=int(n/6)*32
        paste_frame(x,y)
        if(up):
            paste_number(n,x+28,y+3)   
        else:
            paste_number(n,x+28,y+19)

change_img_opacity(opacity)
img.save('final.png', "png")
