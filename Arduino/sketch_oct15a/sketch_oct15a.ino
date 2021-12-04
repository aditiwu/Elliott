/* ===============================================================
      Project: 4 Channel 5V Relay Module
       Author: Scott C
      Created: 7th Sept 2014
  Arduino IDE: 1.0.5
      Website: http://arduinobasics.blogspot.com.au
  Description: Explore the difference between NC and NO terminals.
================================================================== */

 /* 
  Connect 5V on Arduino to VCC on Relay Module
  Connect GND on Arduino to GND on Relay Module 
  Connect GND on Arduino to the Common Terminal (middle terminal) on Relay Module. */
 
 #define relay1 10   // Connect Digital Pin 8 on Arduino to relay1 on Relay Module
 #define relay2 9   // Connect Digital Pin 7 on Arduino to relay2 on Relay Module
 #define LEDgreen 12 //Connect Digital Pin 4 on Arduino to Green LED (+ 330 ohm resistor) and then to "NO" terminal on relay module
 #define LEDyellow 12 //Connect Di4ital Pin 12 on Arduino to Yellow LED (+ 330 ohm resistor) and then to "NC" terminal on relay module
 #include <Servo.h>
Servo myservo;
int val;
 void setup(){
   //Setup all the Arduino Pins
   pinMode(relay1, OUTPUT);
   pinMode(relay2, OUTPUT);
   pinMode(LEDgreen, OUTPUT);
   digitalWrite(LEDgreen, HIGH);
   //Turn OFF any power to the Relay channels
   delay(2000); //Wait 2 seconds before starting sequence
 }
 
 void loop(){
 digitalWrite(LEDgreen, HIGH);
   digitalWrite(relay1, HIGH);  //Relay 3 switches to NO
   delay(1000);
   digitalWrite(relay1,LOW);    //Relay 3 switches to NC
   delay(1000);
   digitalWrite(relay2, HIGH);  //Relay 3 switches to NO
   delay(1000);
   digitalWrite(relay2,LOW);    //Relay 3 switches to NC
   delay(1000);
 }
