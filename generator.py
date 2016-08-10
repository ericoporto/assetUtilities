from PIL import Image




number_to_generate=60        #any number
opacity=204                   #0 is transparent and 255 is not
num_font='normal'             #'normal' or 'flat'
up=False                      # True or False, sets position
frame_type='reverse'           #'normal' or 'reverse'
color='pink'

###########################################################
#                   program
###########################################################
num_type={'normal':'n_shadow/','flat':'n_clean/'}
colors={'black':(0,0,0),
'dark_purple':(34,32,52),
'purple':(69,40,60),
'dark_brown':(102,57,49),
'brown':(143,86,59),
'orange':(223,113,38),
'beige':(217,160,102),
'cream':(238,195,154),
'yellow':(251,242,54),
'light_green':(153,229,80),
'green':(106,190,48),
'green_oil':(55,148,110),
'dark_green':(75,105,47),
'dark_blue':(63,63,116),
'blue_oil':(48,96,130),
'blue':(91,110,225),
'light_blue':(99,155,255),
'lighter_blue':(95,205,228),
'cream_blue':(203,219,252),
'white':(255,255,255),
'light_gray':(155,173,183),
'gray':(132,126,135),
'dark_gray':(105,106,106),
'light_purple':(118,66,138),
'red':(172,50,50),
'light_red':(217,87,99),
'pink':(215,123,186),
'green_brown':(143,151,74)}
total_height=32*int(number_to_generate/6)
img = Image.new('RGBA', (192, total_height))

if(frame_type=='reverse'):
    frame=Image.open('reverse_frame.png')    
else:
    frame=Image.open('frame.png')
number_im=[]
for i in range(0,10):
    number_im.append(Image.open(num_type[num_font]+str(i)+'.png'))

def tpint(n):
    return n>0 if int(n) else 0
   
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
    
def colorize_img(val):
    datas = img.getdata()
    c=colors[val]
    newData = []
    for item in datas:
        if(item[3]!=0):
            if(item[0]==255 and item[1]==255 and item[2]==255):
                newData.append((c[0],
                                c[1],
                                c[2],
                                item[3]))
            else:
                newData.append(item)
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

colorize_img(color)
change_img_opacity(opacity)
img.save('final.png', "png")
