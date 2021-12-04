#include <SoftwareSerial.h>
SoftwareSerial BTserial(A0, A1);
#include <AccelStepper.h>
// Initialize with pin sequence IN1-IN3-IN2-IN4 for using the AccelStepper with motorPin1BYJ-48
#define motorPin1  2     // IN1 on the ULN2003 driver 1
#define motorPin2  3     // IN2 on the ULN2003 driver 1
#define motorPin3  4     // IN3 on the ULN2003 driver 1
#define motorPin4  5    // IN4 on the ULN2003 driver 1
#define motorPin5  6     // IN1 on the ULN2003 driver 1
#define motorPin6  8     // IN2 on the ULN2003 driver 1
#define motorPin7  9     // IN3 on the ULN2003 driver 1
#define motorPin8  10 
#define HALFSTEP 8
#define INPUT_SIZE 30
int timeDelay = 3000;
AccelStepper stepper1(HALFSTEP, motorPin1, motorPin3, motorPin2, motorPin4);
AccelStepper stepper2(HALFSTEP, motorPin5, motorPin6, motorPin7, motorPin8);
int state = 0;
#include <NewPing.h>
 
#define TRIGGER_PIN  A4
#define ECHO_PIN     A3
#define MAX_DISTANCE 200
 
NewPing sonar(TRIGGER_PIN, ECHO_PIN, MAX_DISTANCE);


void setup() {
  // initialize digital pin 8 as an output.

  Serial.begin(9600);
  BTserial.begin(9600);
  stepper1.setMaxSpeed(1000.0);
  stepper1.setAcceleration(300.0);
  stepper1.setSpeed(250);
  stepper1.moveTo(20000);
  stepper2.setMaxSpeed(1000.0);
  stepper2.setAcceleration(300.0);
  stepper2.setSpeed(250);
  stepper2.moveTo(20000);
  pinMode(11, OUTPUT);

}

void loop() {

  
          for(int i=0; i<75; i++){
            
          digitalWrite(motorPin2,LOW);
    digitalWrite(motorPin4,HIGH);
    delayMicroseconds(timeDelay);
    digitalWrite(motorPin1,HIGH);
    digitalWrite(motorPin3, LOW);
    delayMicroseconds(timeDelay);
    digitalWrite(motorPin4,LOW);
    digitalWrite(motorPin2,HIGH);
    delayMicroseconds(timeDelay);
    digitalWrite(motorPin3,HIGH);
    digitalWrite(motorPin1, LOW);
    delayMicroseconds(timeDelay);


    digitalWrite(motorPin6, LOW);
    digitalWrite(motorPin8, HIGH);
    delayMicroseconds(timeDelay);
    digitalWrite(motorPin5,HIGH);
    digitalWrite(motorPin7, LOW);
    delayMicroseconds(timeDelay);
    digitalWrite(motorPin8, LOW);
    digitalWrite(motorPin6, HIGH);
    delayMicroseconds(timeDelay);
    digitalWrite(motorPin7,HIGH);
    digitalWrite(motorPin5, LOW);
    delayMicroseconds(timeDelay);
          }

}
