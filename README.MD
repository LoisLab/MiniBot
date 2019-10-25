# LoisLab AI Robotics Design & Construction
This repo has plans & software for the LoisLab MiniBot. The MiniBot is a tiny sensor-free rover, controlled by commands issued using http over a local-area network. Onboard the MiniBot, a RaspberryPi/Zero-W receives and executes commands by listening on port 80.

For example, if a MiniBot were logged into a wifi router at local address 192.168.0.103, accessing the following URLs would cause the MiniBot to execute various actions (like moving forward or turning):

<code>192.168.0.103/action=0</code><br>
<code>192.168.0.103/action=1</code><br>
<code>192.168.0.103/action=2</code><br>
<code>192.168.0.103/action=3</code><br>
<code>192.168.0.103/action=4</code><br>
<code>192.168.0.103/action=5</code><br>
<code>192.168.0.103/action=6</code><br>
<code>192.168.0.103/action=7</code><br>
<code>192.168.0.103/speed=0.40</code><br>

To start the robot's web service, access to pi via ssh and use: <code>sudo python3 webbot</code>.

A companion library uses OpenCV to observe one or more MiniBots, and attempt code challenges, like playing capture the flag.

Please read the included pdf, "Assembling the Mini Bot", for a guide on putting one together.
