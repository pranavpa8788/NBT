from PIL import Image
import math, random

im = Image.open('cat2.jpg')

#pixels is the list of all the rgb values of the pixels in the image
pixels = list(im.getdata())

rgb_im = im.convert('RGB')

width, height = im.size

x,y,z = 0,0,0

#This snippet gets the sum of the r,g,b values of all the pixels
for i in range(0, len(pixels)):
        x = x + pixels[i][0]
        
for i in range(0, len(pixels)):
        y = y + pixels[i][1]
        
for i in range(0, len(pixels)):
        z = z + pixels[i][2]

#avgR = x/len(pixels)
#avgG = y/len(pixels)
#avgB = z/len(pixels)

#Calculates the average r,g,b color values
avgR = int(0.5*(x/len(pixels)))
avgG = int(0.5*(y/len(pixels)))
avgB = int(0.5*(z/len(pixels)))

#avgR = 255
#avgG = 255
#avgB = 255

def avg_limiter(x):
    if x < 255:
        return x
    elif x >= 255:
        return 255

def modulus(X):
    if X >= 0:
        return X
    else :
        return -X
    
def diff(a,b) :
    A = modulus(a-b)
    return A

avgR = avg_limiter(avgR)
avgG = avg_limiter(avgG)
avgB = avg_limiter(avgB)

def nplot(a0, b0, c0, a1, b1, c1, x3, y3):
    D0 = diff(a0,a1)
    D1 = diff(b0, b1)
    D2 = diff(c0, c1)
    set_limit = 50
    if (D0 >= 0 and D0 < set_limit) and (D1 >= 0 and D1 < set_limit) and (D2 >= 0 and D2 < set_limit) :
        im.putpixel( (x3,y3), (r0,g0,b0) )
 
def similarity():
    #print(x,y)
    im.putpixel( (x,y), (r0,g0,b0) )
    set0 = 0
    for x0 in range(0, set0 + 1):
        x1 = x + x0
        x2 = x - x0
        if x1 <= width-1 and x2 <= width-1 and x2 >= 0:
            r1, g1, b1 = rgb_im.getpixel((x2,y))
            r2, g2, b2 = rgb_im.getpixel((x1,y))
            nplot(r1, g1, b1, r, g, b, x2, y)
            nplot(r2, g2, b2, r, g, b, x1, y)
        for y0 in range(0, set0 + 1):
            y1 = y + y0
            y2 = y - y0
            if x1 <= width-1 and x2 <= width-1 and x2 >= 0 and y1 <= height-1 and y2 <= height-1 and y2 >= 0:
                r3, g3, b3 = rgb_im.getpixel((x2,y1))
                r4, g4, b4 = rgb_im.getpixel((x1,y1))
                r5, g5, b5 = rgb_im.getpixel((x2,y2))
                r6, g6, b6 = rgb_im.getpixel((x1,y2))
                nplot(r3, g3, b3, r, g, b, x2, y1)
                nplot(r4, g4, b4, r, g, b, x1, y1)
                nplot(r5, g5, b5, r, g, b, x2, y2)
                nplot(r6, g6, b6, r, g, b, x1, y2)
 
def grow(x ,y):
    set0 = 0
    for x0 in range(0, set0 + 1):
        #print(x0)
        x1 = x + x0
        x2 = x - x0
        if x1 <= width-1 and x2 <= width-1 and x2 >= 0:
            pixel_pool.append((x2,y))
            pixel_pool.append((x1,y))
            im.putpixel( (x2,y), (r0,g0,b0) )
            im.putpixel( (x1,y), (r0,g0,b0) )
        for y0 in range(0, set0 + 1):
            y1 = y + y0
            y2 = y - y0
            if y1 <= height-1 and y2 <= height-1 and y2 >= 0 and x2>=0:  
                pixel_pool.append((x2,y1))
                pixel_pool.append((x1,y1))
                pixel_pool.append((x2,y2))
                pixel_pool.append((x1,y2))
                im.putpixel( (x2,y1), (r0,g0,b0) )
                im.putpixel( (x1,y1), (r0,g0,b0) )
                im.putpixel( (x2,y2), (r0,g0,b0) )
                im.putpixel( (x1,y2), (r0,g0,b0) )
        
pixel_pool= []        
black_list=[]

for i in range(0, len(pixels)):
    diffR = pixels[i][0] - avgR
    diffG = pixels[i][1] - avgG
    diffB = pixels[i][2] - avgB
    
    diffR = modulus(diffR)
    diffG = modulus(diffG)
    diffB = modulus(diffB)
    
    ulimit = 30
    llimit = 0
    
    r0 = 255
    g0 = 0
    b0 = 0
    
    if (diffR >= llimit and diffR < ulimit) and (diffG >= llimit and diffG < ulimit) and (diffB < ulimit and diffB >= llimit) :
        for x in range(width):
            for y in range(height):
                r, g, b = rgb_im.getpixel((x, y))
                if (r,g,b) == (pixels[i][0], pixels[i][1], pixels[i][2]):
                    #pixel_pool2.append((x,y))
                    #similarity()
                    grow(x, y)
#print(pixel_pool)
#print(pixel_pool2)
#print(len(pixel_pool))

#r7, g7, b7 = 75, 0, 130
#def finder():
    #for x4 in pixel_pool:
        #x5 = x4[0]
        #x6 = x4[1]
        #set_limit1 = 10
        #set_limit2 = 1
        #for x7 in range(set_limit2, set_limit1 + 1):
            #x8 = x5 + x7
            #x9 = x5 - x7
            #if (x8,x6) not in black_list:
                #if ((x8, x6) in pixel_pool):
                    #if x8 <= width-1 and x9 <= width-1 and x9 >= 0:
                        #black_list.append((x8,x6))
                        #black_list.append((x5,x6))
                        #path_finder(x5,x6,x8,x6)
                        #im.putpixel( (x8, x6), (r7,g7,b7) )
            #if (x9,x6) not in black_list:
                #if ((x9, x6) in pixel_pool):
                    #if x8 <= width-1 and x9 <= width-1 and x9 >= 0:
                        #black_list.append((x9,x6))
                        #black_list.append((x5,x6))
                        #path_finder(x5,x6,x9,x6)
                        #im.putpixel( (x9, x6), (r7,g7,b7) )
            #for y4 in range(0, set_limit1 + 1):
                #y5 = x6 + y4
                #y6 = x6 - y4
                #if (x8,y5) not in black_list:
                    #if ((x8, y5) in pixel_pool):
                        #if x8 <= width-1 and x9 <= width-1 and y5 <= height-1 and y6 <= height-1 and y6 >= 0:
                            #black_list.append((x8,y5))
                            #black_list.append((x5,x6))
                            #path_finder(x5,x6,x8,y5)
                            #im.putpixel( (x8, y5), (r7,g7,b7) )
                #if (x8,y6) not in black_list:
                    #if ((x8, y6) in pixel_pool):
                        #if x8 <= width-1 and x9 <= width-1 and y5 <= height-1 and y6 <= height-1 and y6 >= 0:
                            #black_list.append((x8,y6))
                            #black_list.append((x5,x6))
                            #path_finder(x5,x6,x8,y6)
                            #im.putpixel( (x8, y6), (r7,g7,b7) )
                #if (x9,y5) not in black_list:
                    #if ((x9, y5) in pixel_pool):
                        #if x8 <= width-1 and x9 <= width-1 and y5 <= height-1 and y6 <= height-1 and y6 >= 0 and x9 >= 0:
                            #black_list.append((x9,y5))
                            #black_list.append((x5,x6))
                            #path_finder(x5,x6,x9,y5)
                            #im.putpixel( (x9, y5), (r7,g7,b7) )
                #if (x9,y6) not in black_list:
                    #if ((x9, y6) in pixel_pool):
                        #if x8 <= width-1 and x9 <= width-1 and y5 <= height-1 and y6 <= height-1 and y6 >= 0 and x9 >= 0:
                            #black_list.append((x9,y6))
                            #black_list.append((x5,x6))
                            #path_finder(x5,x6,x9,y6)
                            #im.putpixel( (x9, y6), (r7,g7,b7) )
#def sq(x0,y0,x1,y1):
    #z =int(math.sqrt((x1 - x0)**2 + (y1 - y0)**2))
    #return z

#def path_finder(T0x,Z0y,T1x,Z1y):
    ##T0x,Z0y,T1x,Z1y
    ##T0x=random.randint(0,60)
    ##Z0y=random.randint(0,60)
    ##T1x=random.randint(0,60)
    ##Z1y=random.randint(0,60)
    
    ##T0x=45
    ##Z0y=20
    ##T1x=30
    ##Z1y=20
    
    #(T0, Z0) = (T0x,Z0y)
    #(T1, Z1) = (T1x,Z1y)
    ##print(T0,Z0)
    ##print(T1,Z1)
    #diagonal = sq(T0,Z0,T1,Z1)
    #set_limit3 = diagonal + 1
    ##print(diagonal, set_limit3)
    #if T1 > T0 and Z1 > Z0:
        ##im.putpixel( (T0x-1,Z0y-1), (255,255,0) )
        ##im.putpixel( (T1x+1,Z1y+1), (130,205,110) )
        #for I0 in range(1, diagonal + 1):
            #(T2, Z2) = (T0 + I0, Z0 + I0)
            #for I1 in range(1, set_limit3+1):
                #if (T2+I1,Z2) == (T1,Z1):
                    #for I2 in range(0, T1-T2+1):
                        #im.putpixel( (T2 + I2, Z2), (r7,g7,b7) )
                    #return None
                #elif (T2,Z2+I1) == (T1,Z1):
                    #for I2 in range(0, Z1-Z2+1):
                        #im.putpixel( (T2, Z2 + I2), (r7,g7,b7) )
                    #return None
                #else:
                    #im.putpixel( (T2, Z2), (r7,g7,b7) )
                    #if (T1,Z1) == (T2,Z2):
                        #return None
    #elif T1 > T0 and Z1 < Z0:
        ##im.putpixel( (T0x-1,Z0y+1), (255,255,0) )
        ##im.putpixel( (T1x+1,Z1y-1), (130,205,110) )
        #for I0 in range(1, diagonal + 1):
            #(T2, Z2) = (T0 + I0, Z0 - I0)
            #for I1 in range(1, set_limit3+1):
                #if (T2+I1,Z2) == (T1,Z1):
                    #for I2 in range(0, T1-T2+1):
                        #im.putpixel( (T2 + I2, Z2), (r7,g7,b7) )
                    #return None
                #elif (T2,Z2-I1) == (T1,Z1):
                    #for I2 in range(0, Z2-Z1+1):
                        #im.putpixel( (T2, Z2 - I2), (r7,g7,b7) )
                    #return None
                #else:
                    #im.putpixel( (T2, Z2), (r7,g7,b7) )
                    #if (T1,Z1) == (T2,Z2):
                        #return None
    #elif T1 < T0 and Z1 < Z0:
        ##im.putpixel( (T0x+1,Z0y+1), (255,255,0) )
        ##im.putpixel( (T1x-1,Z1y-1), (130,205,110) )
        #for I0 in range(1, diagonal + 1):
            #(T2, Z2) = (T0 - I0, Z0 - I0)
            #for I1 in range(1, set_limit3+1):
                #if (T2-I1,Z2) == (T1,Z1):
                    #for I2 in range(0, T2-T1+1):
                        #im.putpixel( (T2 - I2, Z2), (r7,g7,b7) )
                    #return None
                #elif (T2,Z2-I1) == (T1,Z1):
                    #for I2 in range(0, Z2-Z1+1):
                        #im.putpixel( (T2, Z2 - I2), (r7,g7,b7) )
                    #return None
                #else:
                    #im.putpixel( (T2, Z2), (r7,g7,b7) )
                    #if (T1,Z1) == (T2,Z2):
                        #return None
    #elif T1 < T0 and Z1 > Z0:
        ##im.putpixel( (T0x+1,Z0y-1), (255,255,0) )
        ##im.putpixel( (T1x-1,Z1y+1), (130,205,110) )
        #for I0 in range(1, diagonal + 1):
            #(T2, Z2) = (T0 - I0, Z0 + I0)
            #for I1 in range(1, set_limit3+1):
                #if (T2-I1,Z2) == (T1,Z1):
                    #for I2 in range(0, T2-T1+1):
                        #im.putpixel( (T2 - I2, Z2), (r7,g7,b7) )
                    #return None
                #elif (T2,Z2+I1) == (T1,Z1):
                    #for I2 in range(0, Z1-Z2+1):
                        #im.putpixel( (T2, Z2 + I2), (r7,g7,b7) )
                    #return None
                #else:
                    #im.putpixel( (T2, Z2), (r7,g7,b7) )
                    #if (T1,Z1) == (T2,Z2):
                        #return None
    #elif T1 == T0:
        #if Z1 > Z0:
            ##im.putpixel( (T0x,Z0y-1), (255,255,0) )
            ##im.putpixel( (T1x,Z1y+1), (130,205,110) )
            #for I1 in range(1, set_limit3+1):
                #if (T0,Z0+I1) == (T1,Z1):
                    #for I2 in range(0, Z1-Z0+1):
                        #im.putpixel( (T0, Z0+I2), (r7,g7,b7) )
                    #return None
    
        #elif Z1 < Z0:
            ##im.putpixel( (T0x,Z0y+1), (255,255,0) )
            ##im.putpixel( (T1x,Z1y-1), (130,205,110) )
            #for I1 in range(1, set_limit3+1):
                #if (T0,Z0-I1) == (T1,Z1):
                    #for I2 in range(0, Z0-Z1+1):
                        #im.putpixel( (T0, Z0-I2), (r7,g7,b7) )
                    #return None
    #elif Z1 == Z0:
        #if T1 > T0:
            ##im.putpixel( (T0x-1,Z0y), (255,255,0) )
            ##im.putpixel( (T1x+1,Z1y), (130,205,110) )
            #for I1 in range(1, set_limit3+1):
                #if (T0+I1,Z0) == (T1,Z1):
                    #for I2 in range(0, T1-T0+1):
                        #im.putpixel( (T0+I2, Z0), (r7,g7,b7) )
                    #return None
    
        #elif T1 < T0:
            ##im.putpixel( (T0x+1,Z0y), (255,255,0) )
            ##im.putpixel( (T1x-1,Z1y), (130,205,110) )
            #for I1 in range(1, set_limit3+1):
                #if (T0-I1,Z0) == (T1,Z1):
                    #for I2 in range(0, T0-T1+1):
                        #im.putpixel( (T0-I2, Z0), (r7,g7,b7) )
                    #return None
##path_finder()
#finder()
##print(black_list)
im.show()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
