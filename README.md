<h1 align="center">Voice Assistance Home Automation</h1>

<h3>Hardware</h3>
Raspberry Pi3 model B, Arduino UNO, LCD (16 x 2), Amazon Alexa, Google Home, Relay Module, IR sensor, PIR sensor, Gas sensor, Jumper wires, Lamp, Bulb, Fan, Switch, HDMI cable

<h3>Software</h3>
Raspbian Operating System, IFTTT, Adafruit MQTT, Arduino IDE, Pushetta

<h3>Steps to follow</h3>

- First we use the inbuilt **Python** in **Raspbian OS** to develop a programming
that helps us in linking the switching ON and OFF of the appliances used
using **adafruit**.
- We, in the dashboard of **Adafruit**, make switches for multiple appliances
using some keywords and use it in the programming too for stating that the
input for certain command will make the appliance ON or OFF.
![image](https://github.com/apuravsharma2702/Voice-Assistance-Home-Automation/assets/75594408/cccb95f8-78ff-486a-8f28-fc6cad8b9c3f)

- Using **IFTTT**, we link Google home assistant with Adafruit and give it
certain commands so that it can turn the appliance ON or OFF as per the
settings done on the site. Along with this we can also control the response
of Google home assistant.
![image](https://github.com/apuravsharma2702/Voice-Assistance-Home-Automation/assets/75594408/e5000ca8-b09c-46df-bcce-cdaa8821474b)

- This way with the help of developed python programming, inbuilt in the
raspbian OS, Adafruit MQTT and IFTTT we can control multiple
appliances using our voice command to the Google Home Assistant. Using
**Two channel relay** we can control 2 appliances at the same time.
![image](https://github.com/apuravsharma2702/Voice-Assistance-Home-Automation/assets/75594408/e95a35a8-2ba8-4a81-9347-0fc3950841e1)

- We also used **IR sensor** and **gas sensor** which has its output as the buzzer
- In IR sensor if any person enters the home IR sensor detects the person
and buzzer becomes on which acts as a bell . Also the person inside home
would get the message in their mobile that some person has entered inside
home. This we have done using pushetta.
- Gas sensor also works as IR that if gas is detected inside the house buzzer
becomes on.
- Also we are displaying time and date using Arduino Uno on LCD display
whose coding is done on **Ardino IDE**.
- We are contolling home appliances like bulb and fan which are connected
to raspberry pi through two channel relay by providing voice commands
on google assistant and are also controlled by two way switch.
