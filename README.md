# 3D Scanner
## Antara, Jackson, Liam

### Introduction

For this project, we were tasked with creating a 3d scanner to project a virtual image of a 3d object. To do this, we used an infrared sensor to detect distance to the object, alongside a pan-and-tilt mechanism using two VS-2 Servos to move across the space the object is in. This allows us to map the objects surface and upload the distances to a computer, where the object is virtually reconstructed.

### Initial setup and Calibration
To test the sensor, we first connected it to the arduino and had code to read and print out the reading. This revealed a few things about the sensor, such as the fact that it is inaccurate to distances under 20 cm. Then we placed the sensor on one end of a ruler and moved a box along different distance values, printing out 10 readings per second. We did this for intervals of 2 cm from 20 to 40. This data was used to calibrate the sensor.
This indicates that IR = -10.7*d + 731, so to convert the other way we get an equation of distance = -0.0924*IR + 67.8. These have Pearson's product coefficients of 0.99 with the data.

The calibration function we used was a linear function. While this is not accurate for very large distances from the scanner, as shown later, for all the distances we were using it was acceptable.

The standard deviation of the data is 78.5
We then extrapolated from our data to points 50 cm and 60 cm away. Using the equations above, we compared the experimental data from these distances to the predicted data, shown in figure 3. As we can see, the predicted data is close to or within one standard deviation for both data points. Given the circumstances, we find this to be an acceptable error. Firstly, we are only scanning objects within the range of 20 - 40 cm anyway, and as the r^2 value is so high (0.99), this equation is applicable in this case. Secondly, because we are extrapolating, with 50-60 cm not being within the original data set, the response is prone to error and should not be assumed reliable anyway.

### Design
#### Calibration
To calibrate the IR Sensor, we simply read the input from the IR sensor and print it out on the serial monitor. Then we waited 0.1 seconds before recording again. A button is integrated into the circuit, which prints ‘NEXT’ in the serial monitor when pressed. This helped keep track of which readings are for which distance. The data taken from the serial monitor was plotted for calibration. This code was very simple, which made it easy to iterate and run multiple tests. However, it came with the downside of making some of the data points difficult to distinguish. Maybe instead of saying ‘NEXT’ we could code button presses to say the current distance we are measuring from.

Scanning and controlling the motion of the scanner:
The arduino code to control the Servos essentially runs in two for loops, with all the angles being tilted through at a single pan angle. At each tilt angle, the sensor takes in 3 readings and returns the average. This average is then printed out to later be used for processing. 

#### Data Processing
The serial monitor read out from the Arduino code was then extracted and turned into a csv file using a Python script. As the scanner completes the same path every time we run it, we can pre-write the angle data in MATLAB. Then we can do math to find what point in space the sensor is looking at. Knowing the angles, we do some simple trigonometry to find out the exact coordinates of the point the sensor is looking at. 

Using the angles labeled thetax and thetay, we can calculate the x, y and z components of the point we are looking at.

This point is then plotted using MATLAB. A heatmap is generated to more easily distinguish the near points from the far points. This worked well in matlab, however the resolution is rather poor and it can be difficult to get a real grasp on the 3d graph. A more robust 3d plotting tool could be used to improve visuals.
#### Electrical:
The circuitry for calibration is very simple. Firstly, the IR sensor is wired to 5v and ground on a breadboard and directly to the A0 analog input pin on the arduino. Then, a button is connected to the digital 12 pin. It connects a wire from five volts and a pull down resistor to ground. This button, when pressed, makes the digital 12 pin read high. This is used to track which step of the calibration we are on, mentioned above. 
The arduino is connected to two servos and the IR sensor. To add more aesthetic and functional elements, we added a push button to switch it on and a red LED to indicate it was off and a green LED to indicate scanning is in progress. The panning servo is attached to pin 9 and the tilting servo is attached to pin 10. Both these pins are PWM pins since the servo motor is essentially a potentiometer and can receive power in increments. Since the infrared sensor returns analog input, it is attached to pin A0. The push button is attached to pin 7, and the red and green LEDs attach to pins 3 and 4 respectively. 

#### Mechanical
The mechanical aspect of this project was a simple pan and tilt mechanism. The challenges associated with this are: adapting the fixture around the servos and the sensor, 
gearing up the output of the servo, keeping the sensor as close to the axis of rotation as possible for accurate results, and ensuring there are no interferences.  
The first of these challenges was relatively easy since the data sheets for the servos and the sensor had all the relevant dimensions. 

The next design consideration was keeping the sensor close to the axis of rotation in order to easily make out where the sensor was pointing. This was also easy to account for though it made the design slightly more complex. 

Gearing up the servo’s rotation was considered because it would give more precise control of the sensor. This was abandoned because the gear ratio would be a needless variable to account for and wouldn’t make a great difference in the quality of the measurement. The gears became a vestigial mechanism in the final design with a gear ratio of 1:1.

One thing that was not anticipated was managing the interferences that wires cause. In the original design the sensor was too close to the servo which stopped the servo from utilizing its full range of rotation. This was fixed by changing the angle at which the gears interacted and flipping the servo on its side to increase the distance. 	

If there was more time to develop the mechanism, another round of laser cutting would help improve the look of the device. The box at the bottom of the device, intended to hold all the components, could also be finished. 

### Reflection
Overall, this project was a fun and challenging combination of software, mechanical and electrical engineering. A common challenge was integrating disciplines, such as the mechanical need to adapt to wires and the software need to adapt to the output of hardware. The rudimentary 3d scanner we made serves its purpose well, however leaves room for improvement in precision. A more precise scanner combined with more robust modelling software would lead to much higher quality images. Another challenge was the fact that the mechanical housing was needed to test the scanner and its performance. Since all the elements needed to be iterated multiple times, sometimes there were testing delays. In future projects this can be made more efficient through communication and planning.
