#imports
import time
#Making it a function
def rocket_calculator():
    #constants
    gravity=9.81 #m/s^2
    #inputs
    try:
        thrust=float(input('Enter rocket thrust(N):'))
        mass=float(input('Enter rocket mass(kg):'))
        b_time=float(input('Enter rocket burn time(s):'))
    except:
        print('Value Entered is not a number, try again')
        return
    #Count down
    print('Begin the Countdown')
    time.sleep(1)
    cd=5
    print(cd, '...')
    while cd>1:
        time.sleep(1)
        cd=cd-1
        print(cd, '...')
    time.sleep(1)
    print('BlastOff!')
    time.sleep(1)
    #calculations while the rocket is burning
    print('Rocket is burning...')
    time.sleep(1)
    net_force=thrust-(mass*gravity)
    acceleration=net_force/mass
    height=(1/2)*acceleration*(b_time**2)
    print('Rocket burning calculations made...')
    time.sleep(1)
    #after burn time
    print('Rocket has stopped burning...')
    time.sleep(1)
    velocity=acceleration*b_time
    time_stop=velocity/gravity
    e_height=(velocity**2)/(2*gravity)
    print('Finishing Calculations being completed...')
    time.sleep(1)
    max_altitude=height+e_height
    print('Your maximum altitude reached was:', round(max_altitude,3), 'm', 'and your final velocity at burnout was:', round(velocity,3), 'm/s')
rocket_calculator()
