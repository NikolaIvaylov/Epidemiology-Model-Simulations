import numpy as np
import matplotlib.pyplot as plt

'''--- SEIRVS Simulation ---'''

#Variables you can play with:
#Population:
N = 100000 #total number of people
I0 = 5000 #total number of initially infectious people
#Time:
t_step = 0.01 #time step (in days)
days = 365 #for how many days the simulation should run?
#Other Constants:
a = 0.5 #recovery rate
b = 1 #infection rate
immunity = 30 #duration of immunity (in days)
vaccine = 275 #how many days it takes to make a vaccine?
vaccination_rate = 0.1 #how fast people get vaccinated?
infectious_time = 2 #how much time it takes for exposed people to become infectious? (in days)
lethality = 0.01 #death rate

#Variables you cannot play with:
#Population:
S0 = N - I0 #susceptible to the disease
time = np.arange(0, days+t_step, t_step) #generate values for the t_axis
#Immunity:
immunity_index = int(immunity/t_step) #an index value used to get the population that loses imunity
recovered = [0] #list of the number of newly recovered people for each time step
#Exposed:
exposed_index = int(infectious_time/t_step) #an index value used to get the population that becomes infectious
exposed = [0] #list of the number of newly exposed people for each time step
#Lists:
S_list = [S0] #list for all values of Susceptible
E_list = [0] #list for all values of Exposed
I_list = [I0] #list for all values of Infectious
R_list = [0] #list for all values of Recovered
V_list = [0] #list for all values of Vaccinated
D_list = [0] #list for all values of Deaths

#function that is later used to make sure that the values are in their limits:
def clamp(n, minn, maxn):
    return max(min(maxn, n), minn)

for t in time:
    if t > 0:
        #take the last values of S, E, I, R, V, and D:
        S = float(S_list[-1])
        E = float(E_list[-1])
        I = float(I_list[-1])
        R = float(R_list[-1])
        V = float(V_list[-1])
        D = float(D_list[-1])
        
        '''--- All Scenarious ---'''
        if t > immunity and t > vaccine and t > infectious_time:
            #apply SEIRVS formulas with people losing their
            #imunity, vaccinating and becoming infectious at the same time:
            immunity_loss = recovered[(-1-immunity_index)] #get the number of people that lose their immunity
            infectious = exposed[(-1-exposed_index)] #get the number of people that become infectious
            dS = -(b * S * I) / N + immunity_loss - (vaccination_rate*S)
            dE = (b * S * I) / N - infectious - (vaccination_rate*E)
            dI = 0 + infectious - a * I - lethality * I
            dR = a * I - immunity_loss
            dV = (vaccination_rate*S) + (vaccination_rate*E)
            dD = lethality * I
            exposed.append((b * S * I) / N) #add the newly exposed people
            recovered.append(a * I) #add the newly recovered people
        elif t > immunity and t > vaccine:
            #apply SEIRVS formulas with people losing their
            #imunity, and vaccinating at the same time:
            immunity_loss = recovered[(-1-immunity_index)] #get the number of people that lose their immunity
            infectious = exposed[(-1-exposed_index)] #get the number of people that become infectious
            dS = -(b * S * I) / N + immunity_loss - (vaccination_rate*S)
            dE = (b * S * I) / N - (vaccination_rate*E)
            dI = 0 - a * I - lethality * I
            dR = a * I - immunity_loss
            dV = (vaccination_rate*S) + (vaccination_rate*E)
            dD = lethality * I
            exposed.append((b * S * I) / N) #add the newly exposed people
            recovered.append(a * I) #add the newly recovered people
        elif t > vaccine and t > infectious_time:
            #apply SEIRVS formulas with people vaccinating
            #and becoming infectious at the same time:
            infectious = exposed[(-1-exposed_index)] #get the number of people that become infectious
            dS = -(b * S * I) / N - (vaccination_rate*S)
            dE = (b * S * I) / N - infectious - (vaccination_rate*E)
            dI = 0 + infectious - a * I - lethality * I
            dR = a * I
            dV = (vaccination_rate*S) + (vaccination_rate*E)
            dD = lethality * I
            exposed.append((b * S * I) / N) #add the newly exposed people
            recovered.append(a * I) #add the newly recovered people
        elif t > immunity and t > infectious_time:
            #apply SEIRVS formulas with people losing their
            #imunity, and becoming infectious at the same time:
            immunity_loss = recovered[(-1-immunity_index)] #get the number of people that lose their immunity
            infectious = exposed[(-1-exposed_index)] #get the number of people that become infectious
            dS = -(b * S * I) / N + immunity_loss
            dE = (b * S * I) / N - infectious
            dI = 0 + infectious - a * I - lethality * I
            dR = a * I - immunity_loss
            dV = 0
            dD = lethality * I
            exposed.append((b * S * I) / N) #add the newly exposed people
            recovered.append(a * I) #add the newly recovered people
        elif t > infectious_time:
            #apply SEIRVS formulas with people becoming infectious:
            infectious = exposed[(-1-exposed_index)] #get the number of people that become infectious
            dS = -(b * S * I) / N
            dE = (b * S * I) / N - infectious
            dI = 0 + infectious - a * I - lethality * I
            dR = a * I
            dV = 0
            dD = lethality * I
            exposed.append((b * S * I) / N) #add the newly exposed people
            recovered.append(a * I) #add the newly recovered people
        elif t > vaccine:
            #apply SEIRVS formulas with people vaccinating:
            dS = -(b * S * I) / N - (vaccination_rate*S)
            dE = (b * S * I) / N - (vaccination_rate*E)
            dI = 0 - a * I - lethality * I
            dR = a * I
            dV = (vaccination_rate*S) + (vaccination_rate*E)
            dD = lethality * I
            exposed.append((b * S * I) / N) #add the newly exposed people
            recovered.append(a * I) #add the newly recovered people
        elif t > immunity:
            #apply SEIRVS formulas with people losing their immunity:
            immunity_loss = recovered[(-1-immunity_index)] #get the number of people that lose their immunity
            dS = -(b * S * I) / N + immunity_loss
            dE = (b * S * I) / N
            dI = 0 - a * I - lethality * I
            dR = a * I - immunity_loss
            dV = 0
            dD = lethality * I
            exposed.append((b * S * I) / N) #add the newly exposed people
            recovered.append(a * I) #add the newly recovered people
        else:
            #apply SEIRVS formulas:
            dS = -(b * S * I) / N
            dE = (b * S * I) / N
            dI = 0 - a * I - lethality * I
            dR = a * I
            dV = 0
            dD = lethality * I
            exposed.append((b * S * I) / N) #add the newly exposed people
            recovered.append(a * I) #add the newly recovered people
    
        #calculate the new values of S, E, I, R, V, and D using the clamp() function:
        new_S = clamp((S + dS * t_step), 0, N)
        new_E = clamp((E + dE * t_step), 0, N)
        new_I = clamp((I + dI * t_step), 0, N)
        new_R = clamp((R + dR * t_step), 0, N)
        new_V = clamp((V + dV * t_step), 0, N)
        new_D = clamp((D + dD * t_step), 0, N)
        
        #add the new values of S, E, I, R, V, and D to the lists:
        S_list.append(new_S)
        E_list.append(new_E)
        I_list.append(new_I)
        R_list.append(new_R)
        V_list.append(new_V)
        D_list.append(new_D)

#output logic:
def output():
    #options of the graph:
    plt.figure(dpi=350) 
    plt.title(f"a={a}, b={b}, lethality = {lethality}, immunity for {immunity} days, infectious after {infectious_time} days")
    plt.xlabel("Time (days)")
    plt.ylabel("Population")
    #display the vaccinated line:
    plt.plot(time, V_list, color="green", label="Vaccinated")
    #display the recovered line:
    plt.plot(time, R_list, color="blue", label="Recovered")
    #display the susceptible line:
    plt.plot(time, S_list, color="yellow", label="Susceptible")
    #display the exposed line:
    plt.plot(time, E_list, color="orange", label="Exposed")
    #display the infectious line:
    plt.plot(time, I_list, color="red", label="Infectious")
    #display the dead line:
    plt.plot(time, D_list, color="black", label="Dead")

    plt.legend(bbox_to_anchor=(1.05, 1))
    plt.show()

output()







    