#include <Servo.h>
#include <AccelStepper.h>

int joyXVAL;
int joyVal3;  
// Initialize with pin sequence IN1-IN3-IN2-IN4 for using the AccelStepper with motorPin1BYJ-48


int joyVal2;
Servo myservo;
const int joyx = 0;
const int joyy = 1;

int timeDelay = 3000;

const int buzzer = 13;
const int ledPin = 11;
int joyVal;
int swval;
int pos; 







void setup()
{
 

  myservo.attach(6);

  pinMode(buzzer, OUTPUT);
  pinMode(ledPin, OUTPUT);

}

void loop()
{
  
  joyVal2 = analogRead(joyy);
  joyVal = analogRead(joyx);
  joyVal = map(joyVal, 0, 1023, 0, 180);
myservo.write(joyVal);
      

}



