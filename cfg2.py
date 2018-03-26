#Config File used for the MAE 198 RC Car Fetch Code

#Throttle Control
k_Throttle=5; #Proportional Value for Throttle
Throttle_Controller=[.025,.025] #Tustins Approximatinon for D=1/s at 20 Hz
PWMHigh_Throttle=385.0 #Max PWM Allowable
PWMLow_Throttle=382.0 #Low PWM
PWMOff_Throttle=378.0 #Assures off for Throttle
PWMDonuts_Throttle=384.0
MaxDistance=15.0 #Distance to Apply high PWM
MinDistance=1.0 #Distance to Apply Low PWM
Distance_Ref=0.0 #Desired Distance
Throttle_Channel=2

#Steering Control
Steering_Control_Option=False #True to apply steering control
k_Steering=10.0 #Proportional Value for Steering
Steering_Controller=[.025,.025] #Tustins Approximation for D=1/s at 20 Hz
PWMHigh_Steering=470.0; #PWM For Max Right Turn
PWMLow_Steering=260.0; #PWM For Max Left Turn
InnerWheelTheta=35.0; #Degrees From Straight of Inner Wheel on max Turn
OuterWheelTheta=25.0;#Degrees From Straight of Outer Wheel on max Turn
ThetaRef=0.0;
Steering_Channel=1

#Steering and Throttle Linear calculations that linearly interpolate the min/max
#PWM values to min/max steering angles or throttle values. 'm' is slope of line
# and 'y' is y-intercept of line
MaxThetaTurn=(InnerWheelTheta+OuterWheelTheta)/2; #Average of wheel angles taken as correct value
PWMMid_Steering=(PWMHigh_Steering+PWMLow_Steering)/2
m_Throttle=(PWMHigh_Throttle-PWMLow_Throttle)/(MaxDistance-MinDistance);
b_Throttle=PWMHigh_Throttle-m_Throttle*MaxDistance;
m_Steering=(PWMHigh_Steering-PWMLow_Steering)/(MaxThetaTurn-(-MaxThetaTurn)); #Slope of pwm=m*theta+b line equation
b_Steering=PWMHigh_Steering-m_Steering*MaxThetaTurn; 

#Ball Specs
Ball_Radius=1.375 #in
secondColor_lower=(0,145,127)
secondColor_upper=(17,255,255)
green_lower = (41, 25, 57)  
green_upper = (180, 255, 255)
currentColor_lower=(41, 25, 57)  
currentColor_upper=(180, 255, 255)

#Camera
Cam_Resolution=[720,480]
Cam_FrameRate=20

#Depth Distance Calculation
m_const=-51
b_const=65.5
inverse_const=30
linear_inverse_boundary=42

#Ball Search Conditions
min_Pixel_Radius=3 #Minimum pixels to Take Action
y_Limit=450 #Closeness of ball to stop Taking Action
y_Limit_Current=450
y_Limit2=350

#Time before Donuts
donutTime=2
