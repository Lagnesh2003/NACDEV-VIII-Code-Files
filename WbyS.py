import math

MaxMach = 2
tempat16 = 216.7  
gamma = 1.4
# Specific Gas Constant
R_specific = 287.4  # J/(kg·K)
rhocruise = 0.186
Speed = MaxMach * (math.sqrt(gamma * R_specific * tempat16))

Vstall = 36.0111
CLmax = 3.5
rho = 1.225

WbySstall = (0.5)*(Vstall*Vstall)*(CLmax)*(rho)
print(WbySstall)

sigma = 1
MaxLandindDist = 2000
Endtobeginfraction = 0.71
factor = 24.384
WbySLanding = ((MaxLandindDist*(CLmax))/factor)*(1/Endtobeginfraction)
print(WbySLanding)

CLtakeoff = CLmax/1.21
TbyW = 0.5668
TOP = 300
lbft2tokgm2 = 4.88243
WbySTakeoff = (TOP)*(CLtakeoff)*(TbyW)*(lbft2tokgm2)
print(WbySTakeoff)


Cdo = 0.015
e = 0.6
AR = 2.5
qcruise = (0.5)*(rhocruise)*(Speed**2)
WbyScruise = qcruise*(math.sqrt(((e*Cdo*AR)*(math.pi/3))))
print(WbyScruise)

SpeedLoiter = 70
rholoiter = 0.4292
qloiter = (0.5)*(SpeedLoiter**2)*(rholoiter)
WbySloiter = qloiter*(math.sqrt(((e*Cdo*AR)*(math.pi))))
print(WbySloiter)


