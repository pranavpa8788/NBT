This is documentation of the newai.py script. This was originally written for my own reference since I had written this code a long time ago and I've forgot how my own code words and that has haulted all progress. 

This code at the moment uses some basic math (including the math module), PIL module and random module. 

1. We start off by getting all the pixel data of the image. This is in a list format and it contains width x height number of pixels (area of image). And each element in the pixel list is represented by (r, g, b) values which makes the pixel list a nested list. 

2. Now we move on to calculating the average color of the image. This is done by calculating the average r, g and b values. Here its done by iterating through the pixel list and accumulating all the pixel values individually(sum). And then divide each of those accumulated value by the total number of pxiels. The end result is average r, g and b value of the image.

3. [CHECK] There are parts of this code that don't make sense to me now that I'm re-reading it. And avg_limiter function is one of those functions. It basically prevents any of the average values to excede 255(which is the maximum value that any of r,g or b can have). Which theoretically should never be possible as no pixel value will ever excede 255 in the image and therefore, the average can never excede 255. 

4. The diff function just returns a positive difference of the given parameters.

5. [INCOMPLETE] nplot just puts a pixel at given parameter x3, y3 with a specific color. It works sort of like a pixel painter.
