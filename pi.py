#imports
import random
import math

#throwing needles
def pi_estimation(dis,length, needles):    
    cross =0.0 #how many needles crosses the lines
    needle_count = 0.0 # total number of needles
    
    #throws count
    for i in range(length, needles):
          needle_count+=1
          
          #random point (a,b) on the needle
          a = random.uniform(dis/2, dis*1.5)
          b = random.uniform(150,550)
          #radius of the needle
          r= length/2
          
          #To get sharp end and blunt end of the needle
          k=1
          x_1=0
          x_2=0
          while (k>=1):
             x_1=random.uniform(-1,1)
             x_2=random.uniform(-1,1)
             k=x_1*x_1+x_2*x_2

          #calculating point on the circle of the given radius
          x = (x_1 ** 2 - x_2 ** 2) / (x_1 ** 2 + x_2 ** 2)#(x1^2-x2^2)/(x1^2+x2^2)
          y = (2 * x_1 * x_2) / (x_1 ** 2 + x_2 ** 2) # (2x1x2/x1^2+x2^2)

          #calculating the slope instead of theta
          m=(y/x)
          #slope extension
          x3 = math.sqrt((r ** 2) / (1 + m ** 2))
          if(x <0):
            x3=-x3
          y3=m *x3
          x4 = -x3
          y4 = -y3
          
          #finding out the sharp and blunt ends from the points on the needle and through radius points
          sharp_x= a+x3
          sharp_y= b+y3
          blunt_x= a+x4
          blunt_y= b+y4
          #exchanging if it is less
          if blunt_x < sharp_x:
            sharp_x, blunt_x = blunt_x, sharp_x
          
          #checking if the needles crosses the line
          if sharp_x <= dis and blunt_x >= dis:
             cross+=1
             
    #probability
    p = cross/needle_count
    #pi calculation
    pi = (2.0 * length) / (p * dis)
  
    print("Pi is estimated as %f" % pi)


        

def pi():
    distance = 100
    needle_length = 99
    needle_count = 100000
    pi_estimation(distance, needle_length, needle_count)

if __name__ == "__main__":
    pi()
