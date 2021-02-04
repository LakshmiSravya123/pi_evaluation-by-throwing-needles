# pi_evaluation-by-throwing-needles

The main issue with original Buffon’s experiment is using the value of π in the estimation of the value of π which is self-contradictory and does not make any sense.  In order to reduce this contradiction i came upon with the help of Wolfram circular point picking.The circular point estimation of area is quite easier compared to needle.  In my program i haven’t used any of trigonometric functions and value of π instead we calculated the sharp and blunt ends of the needle using geometry.The calculation of sharp end and blunt end goes as follows:
1) A random point on the needle is taken (a,b) with and radius =(length of needle/2)
2) A random point in the circle given radius can be obtained by picking two numbers x1, x2 from an uniformdistribution(-1,1) using Wolfram circular point picking technique and calculating (x,y)
3) Calculate the slope of (x,y) and extend it to larger radius and calculate the point (x3,y3) 
4) The  second  point  (x4,y4)  =  (-x3,-y3)  is  obtained  by  passing  it  the  center  of  larger  radius.  
5) Thesetwo pointsadded to (a,b) give the sharp end and blunt end of the needle  
6) The probability is calculated by(number of needles crossed/number of needles thrown).Through which the π value is calculated

# Language
Python
