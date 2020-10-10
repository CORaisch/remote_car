# General Installation
1. install Ubuntu Core or Ubuntu Mate on Raspberry Pi
2. install git build-essentials python-dev
3. install ROS using apt-get and setup .bashrc accordingly
4. install PCA9685 python library from Adafruit as described at <https://github.com/adafruit/Adafruit_Python_PCA9685>

# DS4 Installation
1. setup Bluetooth on Raspberry Pi according to <https://wiki.ubuntuusers.de/Bluetooth/Einrichten>
```bash
apt-get install bluetooth bluez bluez-tool libbluetooth3 libbluetooth-dev 
service bluetooth restart
```
2. install ROS joy package for arbitrary joystick inputs
```bash
apt-get install ros-melodic-joy
```
3. install ds4drv according to <https://github.com/chrippa/ds4drv>

# Project Setup
1. clone repositories
```bash
git clone https://github.com/CORaisch/remote_car
cd remote_car/src
git clone https://github.com/solbach/ps4-ros
```
2. follow "Installation" section in readme of ps4-ros to find out the dev the controller will be bind to and set /dev/jsX inside the ps4.launch script accordingly
3. build with catkin
```bash
cd ..
catkin_make
echo "source devel/setup.bash" >> ~/.bashrc
```

# Prepare Remote Control
1. connect PCA9685 shield via i2c with Raspberry Pi as described at <https://learn.adafruit.com/adafruit-16-channel-servo-driver-with-raspberry-pi/overview>
2. plug in steering servo at channel 0 of the shield
3. from the ESC only plug in Signal (white) and GND at channel 1 of the shield. Do not connect the VCC of the ESC with VCC of PCA9685 since most ESCs provide 5V at VCC to power the receiver. The ESC will normally be powered directly from the battery.

# Control the Car using Keyboard
launch nodes in the following order to control the car with the keyboard:
```bash
roscore
rosrun keyboard_controller keyboard_input_gui.py
rosrun car_controller control.py
```
**** the user who runs the scripts needs to be in the i2c group so that the control.py script can access /dev/i2c-1
***** # usermod -a -G i2c <username>
**** ensure that all python scripts are executable
***** $ chmod +x src/keyboard_controller/scripts/keyboard_input_gui.py
***** $ chmod +x src/keyboard_controller/scripts/keyboard_input_pynput.py
***** $ chmod +x src/car_controller/scripts/control.py
**** ensure that devel/setup.bash is sourced in all terminals or added to .bashrc
** focus the GUI to capture the keyboard inputs
** control the car using arrow keys

# Control the Car using PS4 Controller
1. start PS4 ROS-node. This node will pack the commands of the DS4 driver into ROS-messages.
```bash
roscore
roslaunch ps4_ros ps4.launch
```
2. hold down SHARE and PS-BUTTON for ~5 seconds to bring controller into pairing mode
3. wait until ros_ps4 prompts you to calibrate the controller
4. hold down L2 and R2 till controller is calibrated
5. run the remote control node for the ds4 controller and the car controller node. The first will convert the DS4 commands into commands for controling the remote car. The latter will generate the physical signals for the ESC and steering servo.
```bash
rosrun ds4_controller ds4_input.py
rosrun car_controller control.py
```

# Notes
* the user who runs the scripts needs to be in the i2c group so that the control.py script can access /dev/i2c-1
```bash
usermod -a -G i2c <username>
```
* ensure that all python scripts are executable
```bash
chmod +x src/car_controller/scripts/control.py
chmod +x src/ds4_controller/scripts/ds4_input.py
```
* ensure that devel/setup.bash is sourced in all terminals, or add it to .bashrc/.zshrc
