print('1) DRAG\n2) LIFT\n3) THRUST\n4) REYNOLDS NUMBER')
inp = input()

if (inp == '1'):
   coeff = int(input('Enter Drag Coefficient : '))
   density = int(input('Enter Density : '))
   velocity = int(input('Enter Velocity : '))
   area = int(input('Enter Area : '))

   
   drag = coeff*(density*velocity*velocity/2)*area
   print(drag)

elif(inp == '2'):
   coeff = int(input('Enter Lift Coefficient : '))
   density = int(input('Enter Density : '))
   velocity = int(input('Enter Velocity : '))
   area = int(input('Enter Area : '))

   lift = coeff*(density*velocity*velocity/2)*area
   print(lift)

elif(inp == '3'):
   velocity = int(input('Enter Velocity : '))
   changem = int(input('Enter Change in mass : '))
   changet = int(input('Enter Change in time : '))
   
   thrust = velocity*(changem/changet)
   print(thrust)


elif(inp == '4'):

   density = int(input('Enter Density : '))
   velocity = int(input('Enter Velocity : '))
   lindi = int(input('Enter Linear dimension  : '))
   viscosity = int(input('Enter Viscosity of fluid : '))
   
   Re = (density*velocity*lindi)/viscosity
   print(Re)

if (inp =='4' and Re <= 2300):
    print('Laminar Flow')
elif(Re>2300 and Re<4000):
    print('Transition Flow')
elif(Re>4000):
    print('Turbulent Flow')
   
