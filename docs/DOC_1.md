This is documentation of the newai.py script. This was originally written for my own reference since I had written this code a long time ago and I've forgot how my own code words and that has haulted all progress. 

This code at the moment uses some basic math (including the math module), PIL module and random module. 

1. We start off by getting all the pixel data of the image. This is in a list format and it contains width x height number of pixels (area of image). And each element in the pixel list is represented by (r, g, b) values which makes the pixel list a nested list. 

2. Now we move on to calculating the average color of the image. This is done by calculating the average r, g and b values. Here its done by iterating through the pixel list and accumulating all the pixel values individually(sum). And then divide each of those accumulated value by the total number of pxiels. The end result is average r, g and b value of the image.

3. The diff function just returns a positive difference of the given parameters.

4. [INCOMPLETE] nplot just puts a pixel at given parameter x3, y3 with a specific color. It works sort of like a pixel painter. Which has some limits (0 and set_limit)

5. [INCOMPLETE] similarity : Following is how this function works : 

    i. It works the same way as grow function. Except it adds the pixels to the pixel pool list and calls nplot function.
    
    ii. nplot finds the neighbouring pixels which are set_limit similar to the current pixel. set_limit = 0 detects no neighbours and set_limit = 255 detects all neighbours.

6. [INCOMPLETE] grow : Following is how this function works :

    i. We define set0. First we iterate through 0, set0 + 1 which is the same as (0, 1). The reason we don't directly define the range as (0,1) so that we can later change this range if we wanted to. 
    
    ii. The parameters x and y are the pixel's coordinate. Now we find and paint set0 number of pixels outside of the current pixel (sort of like the pixels are growing). To better explain this consider the pixels were arranged in the following order : 
    
    [0],[1],[2] [y-coordinate 0]
    
    [3],[4],[5] [y-coordinate 1]
    
    [6],[7],[8] [y-coordinate 2]
    
    where each element represents the horizontal index/ horizontal position/ x,coordinate of the pixel. So if we were to apply the coordinate of the pixel 4, that is (4,1) and pass it to grow, the pixels that would get painted with set0 value 1 are : 0,1,2,3,4,5,6,7,8, that is all the pixels. And with set0 value = 0, only 4 would get painted (because grow paints the pixel itself as well due the range starting from 0). And grow paints pixels only that are within the image boundary.
    
    iii. [INCOMPLETE] The boundaries are basically the image's width and height, but there's more to that.
    
    iv. [CHECK] The painted pixels are added to a pixel pool list. Which is used in later parts of the code.

7. Now we iterate through all the pixels. Then : 

    i. We calculate the positive difference between each pixel and the average pixel value
    
    ii. We define upper limit and lower limit. And r0, g0 and b0 values.
    
    iii. Now if the difference values falls inside these limit values, we find the width and height (x and y coordinate) of the pixel by using an iterative method.
    
    iv. Finally, we call the grow method

8. [INCOMPLETE] finder and path_finder
