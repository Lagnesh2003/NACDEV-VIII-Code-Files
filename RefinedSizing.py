import math

# Needs to be asked
Payload_weight = 2000  # in kg


CruiseMach = 2.0

# Takeoff Weight Fraction - includes engine start, taxi and takeoff
Takeoff_fraction = 0.98

# Climb Weight Fraction - assuming accelarating from Mach 0.1 to 2
Climb_fraction = 0.991 - 0.007*CruiseMach - 0.01*(CruiseMach*CruiseMach)
print(Climb_fraction)

#Descent weight fraction
Descent_fraction = 0.9925


# Landing Weight Fraction - Includes Landing and taxi-back
Landing_fraction = 0.995

# Loiter Time as per requirements
Loiter_time = 2 * 60 * 60  # 2 hours in seconds
# SFC for Turbojet in Cruise
SFC_cruise = 0.9 / 3600.0
# SFC for Turbojet in Loiter
SFC_loiter = 0.8 / 3600.0

# L/D max
LbyDmax = 10
# L/D in cruise
LbyDcruise = 0.866 * LbyDmax
# L/D in Loiter
LbyDloiter = LbyDmax

# Range Requirements
Range = 1000 * 1000  # in meters

# Max Mach number
MaxMach = 2.0
# Temeperature at 16 km according to ISA
tempat16 = 216.7  # Temperature at 16 km in Kelvin (ISA)
# Adiabatic Constant of air
gamma = 1.4
# Specific Gas Constant
R_specific = 287.4  # J/(kg·K)

# Velocity During Cruise
Speed = MaxMach * (math.sqrt(gamma * R_specific * tempat16))

# Weight Fractions by Breguet Equations
# Compute weight fractions for cruise and loiter phases
Cruise_weight_fraction = math.exp(((-Range) * SFC_cruise) / (Speed * LbyDcruise))
Loiter_weight_fraction = math.exp(((-Loiter_time) * SFC_loiter) / (LbyDloiter))

# End-to-begin weight fraction: product of individual flight segments
Endtobegin_weight_fraction = (Takeoff_fraction * Climb_fraction * Cruise_weight_fraction *
                                Loiter_weight_fraction * Descent_fraction * Landing_fraction)


# Fuel fraction (additional factor of 1.06 is applied
# as per suggestion in Raymer for trapped and unused fuel)
Fuel_fraction = 1.06 * (1 - Endtobegin_weight_fraction)

# Solving the nonlinear equation for Wo using fixed-point iteration:
#   Wo = Payload_weight / (1 - Fuel_fraction - a*(Wo)^c)
tol = 1e-2
max_iter = 10000

Wo = 11000.0  # initial guess for takeoff weight (in kg)

AR = 2.0
TbyW = 0.5
WbyS = 404.3288603009131/4.0

a = -0.02
b = 2.16
C1 = -0.1
C2 = 0.2
C3 = 0.04
C4 = -0.1
C5 = 0.08


print((a + ((MaxMach**C5)*(AR**C2)*(TbyW**C3)*(WbyS**C4)*(b)*(Wo**C1))))
for i in range(max_iter):
    empty_weight_fraction = (a + ((MaxMach**C5)*(AR**C2)*(TbyW**C3)*(WbyS**C4)*(b)*(Wo**C1)))
    new_Wo = Payload_weight / (1 - Fuel_fraction - empty_weight_fraction)
    if abs(new_Wo - Wo) < tol:
        Wo = new_Wo
        print("Convergence reached after", i + 1, "iterations")
        break
    Wo = new_Wo
else:
    print("Did not converge after", max_iter, "iterations")

print("Final Takeoff Weight (Wo): {:.4f} kg".format(Wo))
print(Endtobegin_weight_fraction)