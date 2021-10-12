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
        self.T_t = np.array([[1, 0, dx], [0, 1, dy], [0, 0, 1]])
 

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
        Shape.__init__(self)
        self.A = A

        self.x_old=[]
        self.y_old=[]

        for i in range(len(self.A)):
            self.x_old.append( self.A[i][0])
            self.y_old.append( self.A[i][1])

        self.x_old = np.array(self.x_old)
        self.y_old = np.array(self.y_old)



    def translate(self, dx, dy):
        '''
        Function to translate the polygon
    
        This function takes 2 arguments: dx and dy
    
        This function returns the final coordinates
        '''
        #Storing Old Coordinates
        self.x_old = []
        self.y_old = []
        for i in range(len(self.A)):
            self.x_old.append( self.A[i][0])
            self.y_old.append( self.A[i][1])

        self.x_old = np.array(self.x_old)
        self.y_old = np.array(self.y_old)

        #Translate Begins here
        Shape.translate(self, dx, dy)
        self.translated_coordinates=[]
        for i in range(len(self.A)):
            self.translated_coordinates.append(np.dot(self.T_t,self.A[i]))


        self.x_new=[]
        self.y_new=[]
        for j in range(len(self.A)):
            self.x_new.append( round(self.translated_coordinates[j][0], 2))
            self.y_new.append( round(self.translated_coordinates[j][1], 2))


        for i in range(len(self.A)):
            self.A[i][0] = self.x_new[i]
            self.A[i][1] = self.y_new[i]

        self.x_new = np.array(self.x_new)
        self.y_new = np.array(self.y_new)

        return [self.x_new, self.y_new]
    
    def scale(self, sx, sy):
        '''
        Function to scale the polygon
    
        This function takes 2 arguments: sx and sx
    
        This function returns the final coordinates
        '''
        # Storing Old Coordinates
        self.x_old = []
        self.y_old = []
        for i in range(len(self.A)):
            self.x_old.append(self.A[i][0])
            self.y_old.append(self.A[i][1])

        self.x_old = np.array(self.x_old)
        self.y_old = np.array(self.y_old)

        #Scale Begins Here
        self.sum_of_x_old_coordinates = 0
        self.sum_of_y_old_coordinates = 0

        for i in range(len(self.A)):
            self.sum_of_x_old_coordinates += self.A[i][0]
            self.sum_of_y_old_coordinates += self.A[i][1]


        self.old_centre_coordinates = [self.sum_of_x_old_coordinates / len(self.A),
                                                         self.sum_of_y_old_coordinates / len(self.A)]

        Shape.scale(self, sx, sy)
        self.scaled_coordinates = []

        for i in range(len(self.A)):
            self.scaled_coordinates.append(np.dot(self.T_s, self.A[i]))

        self.x_new = []
        self.y_new = []
        self.sum_of_x_new_coordinates = 0
        self.sum_of_y_new_coordinates = 0
        for j in range(len(self.A)):
            self.x_new.append(round(self.scaled_coordinates[j][0], 2))
            self.sum_of_x_new_coordinates += self.scaled_coordinates[j][0]

            self.y_new.append(round(self.scaled_coordinates[j][1], 2))
            self.sum_of_y_new_coordinates += self.scaled_coordinates[j][1]

        self.new_centre_coordinates_after_scaling=[self.sum_of_x_new_coordinates/len(self.A), self.sum_of_y_new_coordinates/len(self.A)]

        for i in range(len(self.A)):
            self.A[i][0] = self.x_new[i]
            self.A[i][1] = self.y_new[i]

        self.x_new = np.array(self.x_new)
        self.y_new = np.array(self.y_new)

        #Translate Begins here
        Shape.translate(self, self.old_centre_coordinates[0] - self.new_centre_coordinates_after_scaling[0],
                     self.old_centre_coordinates[1] - self.new_centre_coordinates_after_scaling[1])

        for i in range(len(self.A)):
            self.A[i] = (np.dot(self.T_t,self.A[i]))

        self.x_new = []
        self.y_new = []
        for j in range(len(self.A)):
            self.x_new.append(round(self.A[j][0], 2))
            self.y_new.append(round(self.A[j][1], 2))

        self.x_new = np.array(self.x_new)
        self.y_new = np.array(self.y_new)

        return [self.x_new, self.y_new]
    
    def rotate(self, deg, rx = 0, ry = 0):
        '''
        Function to rotate the polygon
    
        This function takes 3 arguments: deg, rx(optional), ry(optional). Default rx and ry = 0. (Rotate about origin)
    
        This function returns the final coordinates
        '''
        # Storing Old Coordinates
        self.x_old = []
        self.y_old = []
        for i in range(len(self.A)):
            self.x_old.append(self.A[i][0])
            self.y_old.append(self.A[i][1])

        self.x_old = np.array(self.x_old)
        self.y_old = np.array(self.y_old)

        # Rotate Begins Here

        for i in range(len(self.A)):
            self.A[i][0] = self.A[i][0] - rx
            self.A[i][1] = self.A[i][1] - ry

        Shape.rotate(self, deg)
        self.rotated_coordinates = []

        for i in range(len(self.A)):
            self.rotated_coordinates.append(np.dot(self.T_r, self.A[i]))

        self.x_new = []
        self.y_new = []
        for j in range(len(self.A)):
            self.x_new.append(round(self.rotated_coordinates[j][0], 2))
            self.y_new.append(round(self.rotated_coordinates[j][1], 2))


        for i in range(len(self.A)):
            self.A[i][0] = self.x_new[i]
            self.A[i][1] = self.y_new[i]

        self.x_new = np.array(self.x_new)
        self.y_new = np.array(self.y_new)

        for i in range(len(self.A)):
            self.A[i][0] = self.A[i][0] + rx
            self.A[i][1] = self.A[i][1] + ry

        self.x_new = []
        self.y_new = []
        for j in range(len(self.A)):
            self.x_new.append(round(self.A[j][0], 2))
            self.y_new.append(round(self.A[j][1], 2))

        self.x_new = np.array(self.x_new)
        self.y_new = np.array(self.y_new)


        return [self.x_new, self.y_new]

    def plot(self):
        '''
        Function to plot the polygon
    
        This function should plot both the initial and the transformed polygon
    
        This function should use the parent's class plot method as well
    
        This function does not take any input
    
        This function does not return anything
        '''


        self.x_new_plot_coordinates = []
        self.y_new_plot_coordinates = []


        self.x_dim_new=abs(self.x_new[0])
        for i in range(len(self.x_new)):
            self.x_new_plot_coordinates.append(self.x_new[i])
            self.x_dim_new=max(abs(self.x_dim_new), abs(self.x_new[i]))

        self.x_new_plot_coordinates.append(self.x_new[0])


        self.y_dim_new = abs(self.y_new[0])
        for i in range(len(self.y_new)):
            self.y_new_plot_coordinates.append(self.y_new[i])
            self.y_dim_new = max( abs(self.y_dim_new), abs(self.y_new[i]))

        self.y_new_plot_coordinates.append(self.y_new[0])


        self.x_dim_old = abs(self.x_old[0])
        for i in range(len(self.x_old)):
            self.x_dim_old = max(abs(self.x_dim_old), abs(self.x_old[i]))

        self.x_old_plot_coordinates = list(self.x_old)
        self.x_old_plot_coordinates.append(self.x_old[0])

        self.y_dim_old = abs(self.y_old[0])
        for i in range(len(self.y_old)):
            self.y_dim_old = max( abs(self.y_dim_old), abs(self.y_old[i]))

        self.y_old_plot_coordinates=list(self.y_old)
        self.y_old_plot_coordinates.append(self.y_old[0])

        plt.plot(self.x_new_plot_coordinates, self.y_new_plot_coordinates, color='#4CAF50')
        plt.plot(self.x_old_plot_coordinates, self.y_old_plot_coordinates, color='#4CAF50', linestyle = 'dashed')


        Shape.plot(self, max(abs(self.x_dim_new), abs(self.x_dim_old), abs(self.y_dim_new), abs(self.y_dim_old )),
                   max(abs(self.x_dim_new), abs(self.x_dim_old), abs(self.y_dim_new), abs(self.y_dim_old )))


class Circle(Shape):
    '''
    Object of class Circle should be created when shape type is 'circle'
    '''
    def __init__(self, x=0, y=0, radius=5):
        '''
        Initializations here
        '''
        Shape.__init__(self)
        self.x=x
        self.y=y
        self.radius=radius
        self.x_old=x
        self.y_old=y
        self.radius_old=radius

    
    def translate(self, dx, dy):
        '''
        Function to translate the circle
    
        This function takes 2 arguments: dx and dy (dy is optional).
    
        This function returns the final coordinates and the radius
        '''
        self.x_old=self.x
        self.y_old=self.y
        self.radius_old=self.radius

        Shape.translate(self, dx, dy)
        self.translated_coordinates=np.dot(self.T_t, np.array([self.x,self.y,1]))
        self.x = self.translated_coordinates[0]
        self.y = self.translated_coordinates[1]

        return ( round(self.x,2), round(self.y,2), round(self.radius,2))
        
    def scale(self, sx):
        '''
        Function to scale the circle
    
        This function takes 1 argument: sx
    
        This function returns the final coordinates and the radius
        '''
        self.x_old = self.x
        self.y_old = self.y
        self.radius_old = self.radius

        if sx<0:
            self.radius = self.radius*(abs(sx))
            Shape.rotate(self, 180)
            self.rotated_coordinates = np.dot(self.T_r, np.array([self.x, self.y, 1]))

            self.x = self.rotated_coordinates[0]
            self.y = self.rotated_coordinates[1]
        else:
            self.radius = self.radius*sx

        return (round(self.x, 2), round(self.y, 2), round(self.radius, 2))
    
    def rotate(self, deg, rx = 0, ry = 0):
        '''
        Function to rotate the circle
    
        This function takes 3 arguments: deg, rx(optional), ry(optional). Default rx and ry = 0. (Rotate about origin)
    
        This function returns the final coordinates and the radius
        '''
        self.x_old = self.x
        self.y_old = self.y
        self.radius_old = self.radius

        self.x = self.x - rx
        self.y = self.y - ry


        Shape.rotate(self, deg)
        self.rotated_coordinates = np.dot(self.T_r, np.array([self.x, self.y, 1]))

        self.x = self.rotated_coordinates[0]
        self.y = self.rotated_coordinates[1]

        self.x = self.x + rx
        self.y = self.y + ry

        return (round(self.x, 2), round(self.y, 2), round(self.radius, 2))
    
    def plot(self):
        '''
        Function to plot the circle
    
        This function should plot both the initial and the transformed circle
    
        This function should use the parent's class plot method as well
    
        This function does not take any input
    
        This function does not return anything
        '''
        circle_old = plt.Circle((self.x_old, self.y_old), self.radius_old, color='g', fill=False, linestyle = 'dashed')

        circle_new = plt.Circle((self.x, self.y), self.radius, color='g', fill=False)

        fig_new, ax_new = plt.subplots()
        ax_new.add_patch(circle_new)
        ax_new.add_patch(circle_old)

        x_dim = max((abs(self.x_old) + self.radius_old), (abs(self.x) +self.radius))
        y_dim = max((abs(self.y_old) + self.radius_old), (abs(self.y) + self.radius))
        Shape.plot(self, max(x_dim, y_dim), max(x_dim, y_dim))

if __name__ == "__main__":
    '''
    Add menu here as mentioned in the sample output section of the assignment document.
    '''
    verbose = int(input("verbose? 1 to plot, 0 otherwise: "))
    t=int(input("Enter the number of test cases: "))
    for z in range(t):
        print()
        shape_select=int(input("Enter type of shape (polygon/circle): "))
        if shape_select==0:
            no_of_sides=int(input("Enter the number of sides: "))

            A=[]

            for i in range(no_of_sides):
                temp=input("Enter (x" + str(i+1) + ",y" + str(i+1) +"): ").split()

                A.append([])
                A[i].append(float(temp[0]))
                A[i].append(float(temp[1]))
                A[i].append(float(1.0))

            p1=Polygon(A)
            q=int(input("Enter the number of queries: "))
            print("Enter Query")
            print("1) R deg (rx) (ry)")
            print("2) T dx (dy)")
            print("3) S sx (sy)")
            print("4) P")

            for j in range(q):
                print()
                tempq=input().split()

                for l in range(len(p1.A)):   #printing x coordinates
                    print(round(p1.A[l][0],2), end=" ")

                for l in range(len(p1.A)):   #printing y coordinates
                    print(round(p1.A[l][1], 2), end=" ")

                if tempq[0]=="R":       #Rotate
                    if len(tempq)==2:
                        print()
                        op=p1.rotate(float(tempq[1]))
                        print(' '.join(map(str, list(op[0]))), ' '.join(map(str, list(op[1]))))
                        if verbose==1:
                            p1.plot()

                    elif len(tempq)==3:
                        print()
                        op=p1.rotate(float(tempq[1]), float(tempq[2]), float(tempq[2]))
                        print(' '.join(map(str, list(op[0]))), ' '.join(map(str, list(op[1]))))
                        if verbose == 1:
                            p1.plot()

                    elif len(tempq)==4:
                        print()
                        op=p1.rotate(float(tempq[1]), float(tempq[2]), float(tempq[3]))
                        print(' '.join(map(str, list(op[0]))), ' '.join(map(str, list(op[1]))))
                        if verbose == 1:
                            p1.plot()


                elif tempq[0] == "T":       #Translate
                    if len(tempq) == 2:
                        print()
                        op=p1.translate(float(tempq[1]), float(tempq[1]))
                        print(' '.join(map(str, list(op[0]))), ' '.join(map(str, list(op[1]))))
                        if verbose == 1:
                            p1.plot()

                    elif len(tempq) == 3:
                        print()
                        op=p1.translate(float(tempq[1]), float(tempq[2]))
                        print(' '.join(map(str, list(op[0]))), ' '.join(map(str, list(op[1]))))
                        if verbose == 1:
                            p1.plot()

                elif tempq[0] == "S":       #Scale
                    if len(tempq) == 2:
                        print()
                        op=p1.scale(float(tempq[1]), float(tempq[1]))
                        print(' '.join(map(str, list(op[0]))), ' '.join(map(str, list(op[1]))))
                        if verbose == 1:
                            p1.plot()

                    elif len(tempq) == 3:
                        print()
                        op=p1.scale(float(tempq[1]), float(tempq[2]))
                        print(' '.join(map(str, list(op[0]))), ' '.join(map(str, list(op[1]))))
                        if verbose == 1:
                            p1.plot()

                elif tempq[0] == "P":
                    if j==0:
                        continue
                    p1.plot()

        elif shape_select == 1:
            temp=input("Enter (x,y,r): ").split()
            c1=Circle(float(temp[0]), float(temp[1]), float(temp[2]))

            q = int(input("Enter the number of queries: "))
            print("Enter Query")
            print("1) R deg (rx) (ry)")
            print("2) T dx (dy)")
            print("3) S sx ")
            print("4) P")

            for j in range(q):
                print()
                tempq = input().split()

                print(round(c1.x,2), round(c1.y,2), round(c1.radius,2))

                if tempq[0] == "R":  # Rotate
                    if len(tempq) == 2:
                        print(*c1.rotate(float(tempq[1])))
                        if verbose == 1:
                            c1.plot()

                    elif len(tempq) == 3:
                        print(*c1.rotate(float(tempq[1]), float(tempq[2]), float(tempq[2])))
                        if verbose == 1:
                            c1.plot()

                    elif len(tempq) == 4:
                        print(*c1.rotate(float(tempq[1]), float(tempq[2]), float(tempq[3])))
                        if verbose == 1:
                            c1.plot()


                elif tempq[0] == "T":  # Translate
                    if len(tempq) == 2:
                        print(*c1.translate(float(tempq[1]), float(tempq[1])))
                        if verbose == 1:
                            c1.plot()

                    elif len(tempq) == 3:

                        print(*c1.translate(float(tempq[1]), float(tempq[2])))
                        if verbose == 1:
                            c1.plot()

                elif tempq[0] == "S":  # Scale
                    print(*c1.scale(float(tempq[1])))
                    if verbose == 1:
                        c1.plot()

                elif tempq[0] == "P":
                    if j==0:
                        continue
                    c1.plot()
