import numpy as np
import scipy.integrate as spIn
import matplotlib.pyplot as plt

def my_ode(y,t,a,b):
    y0, y1 = y
    dydt = [a*(y0 - y0*y1),b*(-y1+y0*y1)]
    return dydt

if __name__ == "__main__":

    # Part 1
    # To get the initial value for y0 and y1 and value for a and b
    a = 1.0
    b = 0.2
    init_y0 = 0.1
    init_y1 = 1.0
    init_y = [init_y0,init_y1]
    
    # Partition the time from t = 0 to 5 into 100 uniform partition
    t = np.linspace(0, 5, 101)
    
    # Solve the nonlinear ODE system
    sol = spIn.odeint(my_ode,init_y,t,args=(a,b))

    # Plot the graph of y0 and y1 against t
    plt.plot(t, sol[:, 0], 'g', label='Prey y0 against t')
    plt.plot(t, sol[:, 1], 'r', label='Predator y1 against t')
    plt.title('Graph of y against t with initial_y0 = 0.1')
    plt.legend(loc='best')
    plt.xlabel('Year t')
    plt.ylabel('y')
    plt.grid()
    plt.savefig('Graph_of_y0_and_y1_(1).png')
    plt.show()
    
    
    # Plot the graph of y1 against y0
    plt.plot(sol[:, 0],sol[:,1], 'r', label='Predator y1 against Prey y0')
    plt.title('Graph of Predator y1 against Prey y0 with initial_y0 = 0.1')
    plt.legend(loc='best')
    plt.xlabel('Prey y0')
    plt.ylabel('Predator y1')
    plt.grid()
    plt.savefig('Graph_of_y1_against_y0_(1).png')
    plt.show()
    
    
    #***************************************************************************

    # Part 2 
    # Initial value for y0 and y1
    # Value for a and b
    a = 1.0
    b = 0.2
    
    # Different initial value for initial_y0
    init_y0 = 0.11
    init_y1 = 1.0
    init_y = [init_y0,init_y1]
    
    # Partition the time from t = 0 to 5 into 100 uniform partition
    t = np.linspace(0, 5, 101)
    
    # Solve the nonlinear ODE system
    sol = spIn.odeint(my_ode,init_y,t,args=(a,b))

    # Plot the graph of y0 and y1 against t
    plt.plot(t, sol[:, 0], 'b', label='Prey y0 against t')
    plt.plot(t, sol[:, 1], 'r', label='Predator y1 against t')
    plt.title('Graph of y against t with initial_y0 = 0.11')
    plt.legend(loc='best')
    plt.xlabel('Year t')
    plt.ylabel('y')
    plt.grid()
    plt.savefig('Graph_of_y0_and_y1_(2).png')
    plt.show()
    
    
    # Plot the graph of y1 against y0
    plt.plot(sol[:, 0],sol[:,1], 'r', label='Predator y1 against Prey y0')
    plt.title('Graph of Predator y1 against Prey y0 with initial_y0 = 0.11')
    plt.legend(loc='best')
    plt.xlabel('Prey y0')
    plt.ylabel('Predator y1')
    plt.grid()
    plt.savefig('Graph_of_y1_against_y0_(2).png')
    plt.show()
    