#Name: Utkarsh Arora
#Roll No: 2020143

import numpy as np
import matplotlib.pyplot as plt
# NO other imports are allowed

class Shape:
    '''
    DO NOT MODIFY THIS CLASS

    DO NOT ADD ANY NEW METHODS TO THIS CLASS
    '''
    def __init__(self):
        self.T_s = None
        self.T_r = None
        self.T_t = None
    
    
    def translate(self, dx, dy):
        '''
        Polygon and Circle class should use this function to calculate the translation
        '''

        self.T_t = np.array([[1, 0, 0], [0, 1, 0], [dx, dy, 1]])
        

    def scale(self, sx, sy):
        '''
        Polygon and Circle class should use this function to calculate the scaling
        '''
        self.T_s = np.array([[sx, 0, 0], [0, sy, 0], [0, 0, 1]])
 
        
    def rotate(self, deg):
        '''
        Polygon and Circle class should use this function to calculate the rotation
        '''
        rad = deg*(np.pi/180)
        self.T_r = np.array([[np.cos(rad), np.sin(rad), 0],[-np.sin(rad), np.cos(rad),0], [0, 0, 1]])

        
    def plot(self, x_dim, y_dim):
        '''
        Polygon and Circle class should use this function while plotting
        x_dim and y_dim should be such that both the figures are visible inside the plot
        '''
        x_dim, y_dim = 1.2*x_dim, 1.2*y_dim
        plt.plot((-x_dim, x_dim),[0,0],'k-')
        plt.plot([0,0],(-y_dim, y_dim),'k-')
        plt.xlim(-x_dim,x_dim)
        plt.ylim(-y_dim,y_dim)
        plt.grid()
        plt.show()



class Polygon(Shape):
    '''
    Object of class Polygon should be created when shape type is 'polygon'
    '''
    def __init__(self, A):
        '''
        Initializations here
        '''
        super().__init__()
        self.A=A

        self.original_polygon=A #saving the original polygon

    def get_x_and_y(self,A):
        '''
        This function iterates through a matrix, with the rows type [x,y,1].
        This function takes 1 argument: A matrix with rows type [x,y,1]
        This function returns 2 numpy arrays; x and y
        '''
        x=[]
        y=[]
        for i in A:
            x.append(i[0])
            y.append(i[1])

        return (np.array(x),np.array(y))
 
    
    def translate(self, dx, dy=None):
        '''
        Function to translate the polygon
    
        This function takes 2 arguments: dx and dy
    
        This function returns the final coordinates
        '''
        if dy is None:
            dy=dx
            
        super().translate(dx,dy)

        self.A=np.dot(self.A, self.T_t)

        return (self.get_x_and_y(self.A))

    
    def scale(self, sx, sy=None):
        '''
        Function to scale the polygon
    
        This function takes 2 arguments: sx and sx
    
        This function returns the final coordinates
        '''

        if sy is None:
            sy=sx

        #Calculates center of polygon
        x,y=self.get_x_and_y(self.A)
        mean_x=np.mean(x)
        mean_y=np.mean(y)
    
        super().scale(sx,sy)

        self.translate(-mean_x,-mean_y) #moves center to the origin
        self.A=np.dot(self.A, self.T_s) #performs scaling
        self.translate(mean_x,mean_y)   #moves center back to original position

        return (self.get_x_and_y(self.A))
 
    
    def rotate(self, deg, rx = 0, ry = 0):
        '''
        Function to rotate the polygon
    
        This function takes 3 arguments: deg, rx(optional), ry(optional). Default rx and ry = 0. (Rotate about origin)
    
        This function returns the final coordinates
        '''

        super().rotate(-deg)

        self.translate(-rx,-ry)          #moves center to the origin      
        self.A=np.dot(self.A, self.T_r)  #performs rotation
        self.translate(rx,ry)            #moves center back to original position

        return (self.get_x_and_y(self.A))
        
    

    def plot(self):
        '''
        Function to plot the polygon
    
        This function should plot both the initial and the transformed polygon
    
        This function should use the parent's class plot method as well
    
        This function does not take any input
    
        This function does not return anything
        '''

        #creates arrays with coordinates for current polygon
        x,y=self.get_x_and_y(self.A) 
        x=np.append(x,x[0]) #the 0th entry is appended at the end of the array
        y=np.append(y,y[0]) #so that the polygon is not left open

        #creates arrays with coordinates for original polygon
        x0,y0=self.get_x_and_y(self.original_polygon)
        x0=np.append(x0,x0[0])
        y0=np.append(y0,y0[0])

        #calculates the maximum x and y from both the current and original polygon.
        #these values are used later to define x_dim and y_dim of the plot
        x_max=np.max(np.append(x,x0))
        y_max=np.max(np.append(y,y0))

        plt.plot(x,y)
        plt.plot(x0,y0,ls="dashed")
        super().plot(x_max*1.5,y_max*1.5)
        

class Circle(Shape):
    '''
    Object of class Circle should be created when shape type is 'circle'
    '''
    def __init__(self, x=0, y=0, radius=5):
        '''
        Initializations here
        '''
        super().__init__()

        self.x=x
        self.y=y
        self.radius=radius

        self.A=np.array([[self.x,self.y,1]]) #creates a matrix with only 1 row

        self.original_circle=self.A
        self.original_radius=self.radius

    
    def translate(self, dx, dy=None):
        '''
        Function to translate the circle
    
        This function takes 2 arguments: dx and dy (dy is optional).
    
        This function returns the final coordinates and the radius
        '''

        if dy is None:
            dy=dx
            
        super().translate(dx,dy)

        self.A=np.dot(self.A, self.T_t)

        return (self.A[0][0],self.A[0][1],self.radius)       
 
        
    def scale(self, sx):
        '''
        Function to scale the circle
    
        This function takes 1 argument: sx
    
        This function returns the final coordinates and the radius
        '''

        #scales up the radius
        self.radius*=sx

        return (self.A[0][0],self.A[0][1],self.radius)
 
    
    def rotate(self, deg, rx = 0, ry = 0):
        '''
        Function to rotate the circle
    
        This function takes 3 arguments: deg, rx(optional), ry(optional).
        Default rx and ry = 0. (Rotate about origin)
    
        This function returns the final coordinates and the radius
        '''

        super().rotate(-deg)

        #the center of rotation is first shifted to the origin, then rotation is
        #performed, and then the center is moved back to it's original point.
        self.translate(-rx,-ry)
        self.A=np.dot(self.A, self.T_r)
        self.translate(rx,ry)

        return (self.A[0][0],self.A[0][1],self.radius)
 
    
    def plot(self):
        '''
        Function to plot the circle
    
        This function should plot both the initial and the transformed circle
    
        This function should use the parent's class plot method as well
    
        This function does not take any input
    
        This function does not return anything
        '''

        #Values for the centers of both the current and original circles are retrieved
        
        x=self.A[0][0]
        y=self.A[0][1]

        x0=self.original_circle[0][0]
        y0=self.original_circle[0][1]
        
        #Both the circles are plotted
        c=plt.Circle((x,y),self.radius,fill=False,color="r")
        plt.gca().add_patch(c)

        c0=plt.Circle((x0,y0),self.original_radius,fill=False,color="b",ls="dashed")
        plt.gca().add_patch(c0)

        #Dimension of the plot is calculated by finding the maximum of the
        #coordinates of the center added to the corresponding radius.
        #This is done for both the circles and both the x and y coordinate
        #of both circles. The maximum is then multiplied by 1.2.
        dim=1.2*max(x+self.radius,y+self.radius,x0+self.original_radius,y0+self.original_radius)
        
        super().plot(dim,dim) #the x and y dim must be the same to preserve symmetry in display of circle

def take_int_value(s, t=None):
    '''
    Runs a while loop that forces the user to enter an integer value.

    This function takes two arguments: the string to be used in the input statement,
    and an optional argument; the tuple in which the value inputed must be present.

    This function returns an integer value.
    '''
    while True:
        x=input(s)
        try:
            x=int(x)

            if t:
                if x in t:
                    return (x)
                else:
                    print ("Please enter valid input.")
            else:
                return (x)
        except:
            print ("Please enter valid input.")
            

if __name__ == "__main__":
    '''
    Add menu here as mentioned in the sample output section of the assignment document.
    '''

    #Asks if user wishes to plot every time
    if input("Enter 1 to plot, 0 otherwise: ")=="1":
        verbose=True
    else:
        verbose=False

    #Asks for number of test cases. Loops until an int value is received.
    test_cases=take_int_value("Enter number of test cases: ")

    for a in range(test_cases):
        #Asks for type of shape
        shape=take_int_value("Enter type of shape: (0-polygon/1-circle)",(0,1))

        if shape==0:
            #If polygon
            sides=take_int_value("Enter number of sides: ")

            #First creates a matrix with top row [0,0,0]. Then other rows are
            #appended. Finally, the [0,0,0] row is deleted.
            
            A=np.array([[0,0,0]])

            for a in range(sides):
                b=input(f"Enter (x{a+1},y{a+1}): ")

                x,y=b.split()

                #adding to array
                c=[[int(x),int(y),1]]
                A=np.append(A,c,axis=0)

            A=np.delete(A,0,0)

            #creates a polygon object 
            p=Polygon(A)

            q=take_int_value("Enter number of queries: ")

            print ("Queries:\n1) R deg (rx) (ry)\n2) T dx (dy)\n3) S sx (sy)\n4) P")

            for a in range(q):
                #The loop is run for the number of queries
                query=input("Enter query: ")

                q_list=query.split()

                
                
                x,y=p.get_x_and_y(p.A)
                print (np.append(x,y))

                #Performs the functions on the polygrams

                if q_list[0]=="T":              
                    if len(q_list)>2:
                        p.translate(int(q_list[1]),int(q_list[2]))
                    else:
                        p.translate(int(q_list[1]))

                elif q_list[0]=="S":
                    if len(q_list)>2:
                        p.scale(int(q_list[1]),int(q_list[2]))
                    else:
                        p.scale(int(q_list[1]))

                elif q_list[0]=="R":
                    if len(q_list)>3:
                        p.rotate(int(q_list[1]),int(q_list[2]),int(q_list[3]))
                    elif len(q_list)>2:
                        p.rotate(int(q_list[1]),int(q_list[2]))
                    else:
                        p.rotate(int(q_list[1]))

                elif q_list[0]=="P":
                    p.plot()

                x,y=p.get_x_and_y(p.A)
                print (np.append(x,y))

                if verbose:
                    p.plot()

        else:
            #If circle
            a,b,r=input("Enter (a b r): ").split()

            q=take_int_value("Enter number of queries: ")

            print ("Queries:\n1) R deg (rx) (ry)\n2) T dx (dy)\n3) S sx (sy)\n4) P")

            for a in range(q):
                #The loop is run for the number of queries.
                query=input("Enter query: ")

                q_list=query.split()

                c=Circle(a,b,r)

                print (c.A[0][0],c.A[0][1],c.radius)

                #Performs functions on the circles
                if q_list[0]=="T":              
                    if len(q_list)>2:
                        c.translate(int(q_list[1]),int(q_list[2]))
                    else:
                        c.translate(int(q_list[1]))

                elif q_list[0]=="S":
                    c.scale(int(q_list[1]))

                elif q_list[0]=="R":
                    if len(q_list)>3:
                        c.rotate(int(q_list[1]),int(q_list[2]),int(q_list[3]))
                    elif len(q_list)>2:
                        c.rotate(int(q_list[1]),int(q_list[2]))
                    else:
                        c.rotate(int(q_list[1]),int(q_list[2]))

                elif q_list[0]=="P":
                    c.plot()

                print (c.A[0][0],c.A[0][1],c.radius)

                if verbose:
                    c.plot()
            

        
                
    
    
