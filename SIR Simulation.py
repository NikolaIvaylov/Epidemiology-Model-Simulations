import numpy as np
import matplotlib.pyplot as plt

'''--- SIR Simulation ---'''

#Variables you can play with:
#Population:
N = 10000 #total number of people
I0 = 100 #total number of initially infected people
#Time:
t_step = 0.01 #time step (in days)
days = 30 #for how many days the simulation should run?
#Other Constants:
a = 0.5 #recovery rate
b = 2 #infection rate

#Variables you cannot play with:
#Population:
S0 = N - I0 #susceptible to the disease
time = np.arange(0, days+t_step, t_step) #generate values for the t_axis
#Lists:
S_list = [S0] #list for all values of S
I_list = [I0] #list for all values of I
R_list = [0] #list for all values of R

for t in time:
    if t > 0:
        #take the last values of S, I, R, and V:
        S = float(S_list[-1])
        I = float(I_list[-1])
        R = float(R_list[-1])
        
        #apply SIR formulas:
        dS = -(b * S * I) / N
        dI = (b * S * I) / N - a * I
        dR = a * I
    
        #calculate the new values of S, I, R, and V:
        new_S = S + dS * t_step
        new_I = I + dI * t_step
        new_R = R + dR * t_step
    
        #add the new values of S, I, R, and V to the lists:
        S_list.append(new_S)
        I_list.append(new_I)
        R_list.append(new_R)

#output logic:
def output():
    #options of the graph:
    plt.figure(dpi=300) 
    plt.title(f"SIR Simulation (a={a}, b={b})")
    plt.xlabel("Time (days)")
    plt.ylabel("Population")
    #display the susceptible line:
    plt.plot(time, S_list, color="yellow", label="Susceptible")
    #display the infected line:
    plt.plot(time, I_list, color="red", label="Infected")
    #display the recovered line:
    plt.plot(time, R_list, color="blue", label="Recovered")

    plt.legend()
    plt.show()

output()







    
