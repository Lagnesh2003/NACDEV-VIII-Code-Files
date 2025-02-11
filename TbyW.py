import math

# Given constants
a = 0.514  # Empirical coefficient for T/W calculation
C = 0.141  # Exponent for Mach number effect
Machmax = 2.0  # Maximum Mach number

# Calculate the thrust-to-weight ratio using the empirical formula
TbyWstatistic = a * (pow(Machmax, C))
print(f"Thrust-to-weight ratio based on statistics: {TbyWstatistic:.4f}")

# Given lift-to-drag ratio values
LbyDmax = 8  # Maximum lift-to-drag ratio
LbyDcruise = 0.866 * LbyDmax  # Lift-to-drag ratio during cruise

# Calculate thrust-to-weight ratio during cruise
TbyWcruise = 1 / LbyDcruise

# Given ratios for cruise and takeoff conditions
Tcruisebytakeoff = 15 / 47  # Ratio of thrust in cruise to thrust at takeoff
Wcruisebytakeoff = 0.95545  # Ratio of weight in cruise to weight at takeoff

# Calculate thrust-to-weight ratio based on thrust matching conditions
TbyWthrustmatch = TbyWcruise * (Wcruisebytakeoff / Tcruisebytakeoff)
print(f"Thrust-to-weight ratio based on thrust matching: {TbyWthrustmatch:.10f}")
