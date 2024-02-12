'''
AN ACTUAL SHADOWED ROTATING CUBE
1) somehow looping through z axis also*
2) See the rotating z axis*
3)Find Corss Product*
4)Create a Pleane of custom size and widtb 


Cross Product = [(A2*B3) – (A3*B2), (A3*B1) – (A1*B3), (A1*B2) – (A2*B1)]

A with elements (A1, A2, A3)
B with elements (B1, B2, B3)
'''
import math
import time

import timeit
 
x_lower = -5
x_upper = 5
y_lower = -3
y_upper = 3

def shadow_the_cube(coords=(),B=(0,0,0),A=(1,1,1),lc=(10,10,10)):
    new_vals = []
    for i in coords:
        A1 = A[0] - i[0]
        A2 = A[1] - i[1]
        A3 = A[2] - i[2]
        
        B1 = B[0] - i[0]
        B2 = B[1] - i[1]
        B3 = B[2] - i[2]
        
        cross = [round((A2*B3) - (A3*B2),1), round((A3*B1) - (A1*B3),1), round((A1*B2) - (A2*B1),1)]
        
        LV = (round((lc[0] - i[0]),1), round((lc[1] - i[1]),1), round((lc[2]-i[2]),1))
        #print("Cross is :",cross)
        mod_lv = math.sqrt(LV[0]**2+LV[1]**2+LV[2]**2)
        mod_cross = math.sqrt(cross[0]**2+cross[1]**2+cross[2]**2)

        if mod_lv*mod_cross != 0:
            dot = round((cross[0]*LV[0]+cross[1]*LV[1]+cross[2]*LV[2])/(mod_lv*mod_cross),1)
        else :
            dot = 0.9
        #print("Dot is :",dot)
        new_vals.append([i[0],i[1],i[2],dot])
    return new_vals
        

def find_Plane_coords(A=(10,10,0),B=(-10,10,0),C=(10,-10,0),D=(-10,-10,0)):
    #plan 2 Method 2
    l1 = connect_pts(A,C)
    l2 = connect_pts(B,D)
    coords = set()
    #print(connect_pts(A,C))
    #print(connect_pts(B,D))
    
    for i in range(len(l1)):
        for j in range(len(l2)):
            #print(j,"of l2 connected to ",i,"Of l1")
            temp=connect_pts(l1[i],l2[j],tup=True)
            for k in temp:
                coords.add(k)
            
    #print(len(coords))
    #print(coords)
    return coords            
    
    

def connect_pts(pt1=(0,0,0),pt2=(10,10,10),tup=False):#pt1 = a pt_2 = b
    pts = []
    dist = math.sqrt((pt2[0]-pt1[0])**2+(pt2[1]-pt1[1])**2+(pt2[2]-pt1[2])**2)
    dist = round(dist,2)
    #print(dist)
    for i in range(0,int(dist),1):
        x = pt1[0]+((1/int(dist))*i)*(pt2[0]-pt1[0])
        y = pt1[1]+((1/int(dist))*i)*(pt2[1]-pt1[1])
        z = pt1[2]+((1/int(dist))*i)*(pt2[2]-pt1[2])
        if tup:
            pts.append( (round(x,1),round(y,1),round(z,1) ) )
        else:
            pts.append( [round(x,1),round(y,1),round(z,1)] )
    return pts
    



def render(coords,x_lower,x_upper,y_lower,y_upper):
    #light='._,:;~!$&#@'
    light = ',-~:!;*=#$@'
    y = y_upper
    while y >=y_lower:
        x = x_lower
        while x <= x_upper:
            #print(f"({x},{y}),",end ="")
            
            #if y == 0:
                #print("#",end="")
            #elif x == 0:
                #print("#",end ="")
                
            if (x,y) in coords:
                light_val = coords[coords.index((x,y))+1]*10
                #print(light_val)
                print(light[int(light_val)],end = "")
                #print("@",end='')
            else:
                print(" ",end="")
            
            x = x+0.1
            x = round(x,1)
        print()
        y = (y-0.1)
        y = round(y,1)



def rotate(origin, point, angle):
    """
    Rotate a point counterclockwise by a given angle around a given origin.

    The angle should be given in radians.
    """
    ox, oy = origin
    px, py = point

    qx = ox + math.cos(angle) * (px - ox) - math.sin(angle) * (py - oy)
    qy = oy + math.sin(angle) * (px - ox) + math.cos(angle) * (py - oy)
    return (round(qx,1), round(qy,1))



def convert(coords=[],screen_dist=2,obj_dist = 20,Shadow=False):
    new_coords=[]
    #print(coords)
    for i in coords:
        if obj_dist+i[2]!= 0:
            x = (screen_dist*i[0]) / (obj_dist+i[2])
        else:
            x = (screen_dist*i[0]) / (obj_dist+i[2]-1)
        if obj_dist+i[2] !=0:
            y = (screen_dist*i[1])/(obj_dist+i[2])
        else:
            y = (screen_dist*i[1])/(obj_dist+i[2]-1)
        new_coords.append((round(x,1),round(y,1)))
        if Shadow:
            new_coords.append(i[3])
    return new_coords



'''
points = [[-5,-1,-5],[-5,-1,5],[5,-1,5],[5,-1,-5],
          [-5,5,-5],[-5,5,5],[5,5,5],[5,5,-5]]
'''
'''
points = []
points.extend(connect_pts((0,0,0),(20,20,20)))
points.extend( connect_pts((0,0,0),(-20,20,20)))
points.extend( connect_pts((0,0,0),(-20,20,-20)))
points.extend( connect_pts((0,0,0),(20,20,-20)))

points.extend( connect_pts((10,10,10),(-10,10,10)) )
points.extend( connect_pts((10,10,10),(10,10,-10)) )

points.extend( connect_pts((20,20,20),(-20,20,20)) )
points.extend( connect_pts((20,20,20),(20,20,-20)) )

points.extend( connect_pts((-10,10,-10),(-10,10,10)) )
points.extend( connect_pts((-10,10,-10),(10,10,-10)) )

points.extend( connect_pts((-20,20,-20),(-20,20,20)) )
points.extend( connect_pts((-20,20,-20),(20,20,-20)) )

#print(points)
for i in range(50):
    
    for j in points:
        #print(j[0],j[2])
        #print(rotate((0,0),(j[0],j[2]),1))
        j[0],j[2] = rotate((0,0),(j[0],j[2]),0.1)
    
    coords = convert(points,screen_dist=3,obj_dist = 50)
    #print(coords)

    
    render(coords,x_lower,x_upper,y_lower,y_upper)
    time.sleep(0.1)


'''
'''

points_temp = find_Plane_coords()

points=[]
for j in points_temp:
    points.append(list(j))

#points=shadow_the_cube(points,A=(10,10,0),B=(-10,10,0),lc=(0,0,5))
#coords = convert(points)
#render(coords,x_lower,x_upper,y_lower,y_upper)

points=shadow_the_cube(points,A=(10,10,0),B=(-10,10,0),lc=(0,0,5))
    
for i in range(100):
    startTime = timeit.default_timer()
 
    for j in points:
        #print(j[0],j[2])
        #print(rotate((0,0),(j[0],j[2]),1))
        j[0],j[2] = rotate((0,0),(j[0],j[2]),0.1)

    
    
    coords = convert(points,Shadow=True)
    #print(coords)

    
    render(coords,x_lower,x_upper,y_lower,y_upper)
    endTime = timeit.default_timer()
 
    
    #print(endTime - startTime)
    time.sleep(0.1)

#find_Plane_coords((-5,-1,-5),(-5,-1,5),(5,-1,5),(5,-1,-5))

#points = find_Plane_coords()


  
#render(tuple(coords))
#render()
'''
#the complicated plane coord finder
points = [[10,10,0],[-10,10,0],[10,-10,0],[-10,-10,0]]


for i in range(150):
    #print(points)
    points_temp = find_Plane_coords(points[0],points[1],points[2],points[3])
    points_f=[]
    for j in points_temp:
        points_f.append(list(j))
    #print(points_f)
    points_f=shadow_the_cube(points_f,points[0],points[1],lc=(2,7,5))
    coords = convert(points_f,Shadow=True)
    render(coords,x_lower,x_upper,y_lower,y_upper)
    #print(endTime - startTime)
    for j in points:
        j[0],j[1] = rotate((0,0),(j[0],j[1]),0.5)
    for j in points:
        j[1],j[2] = rotate((0,0),(j[1],j[2]),0.5)
        

    
    
    
    
    
    
