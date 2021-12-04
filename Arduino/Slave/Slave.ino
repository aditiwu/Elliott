#include <SoftwareSerial.h>
SoftwareSerial BTserial(A7, A6);
#include <AccelStepper.h>
#include <Servo.h>
Servo myservo;
// Initialize with pin sequence IN1-IN3-IN2-IN4 for using the AccelStepper with motorPin1BYJ-48
#define motorPin1  22     // IN1 on the ULN2003 driver 1
#define motorPin2  23     // IN2 on the ULN2003 driver 1
#define motorPin3  24     // IN3 on the ULN2003 driver 1
#define motorPin4  25   // IN4 on the ULN2003 driver 1
#define motorPin5  26     // IN1 on the ULN2003 driver 1
#define motorPin6  27     // IN2 on the ULN2003 driver 1
#define motorPin7  28     // IN3 on the ULN2003 driver 1
#define motorPin8  29
#define HALFSTEP 8
#define INPUT_SIZE 30
int timeDelay = 3000;
char k;
AccelStepper stepper1(HALFSTEP, motorPin1, motorPin3, motorPin2, motorPin4);
AccelStepper stepper2(HALFSTEP, motorPin5, motorPin6, motorPin7, motorPin8);
int state = 0;
#include <NewPing.h>

#define TRIGGER_PIN  A1
#define ECHO_PIN     A0
#define MAX_DISTANCE 200
char *p;
char *e;
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
  pinMode(9, OUTPUT);
  pinMode(50, OUTPUT);
  Serial.println("HII");
  myservo.attach(2);
  myservo.attach(3);
}

void loop() {

  int i = 0;
  char commandbuffer[100];

  if (BTserial.available()) {
    delay(100);
    while ( BTserial.available() && i < 99) {
      commandbuffer[i++] = BTserial.read();
    }
    commandbuffer[i++] = '\0';
  }

  if (i > 0)
  {
    String y = (char*)commandbuffer;
    Serial.println(y);
    if (y == "Down") {
      for (int i = 0; i < 150; i++) {
        digitalWrite(motorPin6, LOW);
        digitalWrite(motorPin8, HIGH);
        delayMicroseconds(timeDelay);
        digitalWrite(motorPin5, HIGH);
        digitalWrite(motorPin7, LOW);
        delayMicroseconds(timeDelay);
        digitalWrite(motorPin8, LOW);
        digitalWrite(motorPin6, HIGH);
        delayMicroseconds(timeDelay);
        digitalWrite(motorPin7, HIGH);
        digitalWrite(motorPin5, LOW);
        delayMicroseconds(timeDelay);


        digitalWrite(motorPin4, LOW);
        digitalWrite(motorPin2, HIGH);
        delayMicroseconds(timeDelay);
        digitalWrite(motorPin3, LOW);
        digitalWrite(motorPin1, HIGH);
        delayMicroseconds(timeDelay);
        digitalWrite(motorPin2, LOW);
        digitalWrite(motorPin4, HIGH);
        delayMicroseconds(timeDelay);
        digitalWrite(motorPin1, LOW);
        digitalWrite(motorPin3, HIGH);
        delayMicroseconds(timeDelay);
      }
    }
    else if (y == "SERVOUP") {
      myservo.write(150);
    }
    else if (y == "SERVOD") {
      myservo.write(90);
    }
    else if (y == "Up") {
      for (int i = 0; i < 150; i++) {

        digitalWrite(motorPin2, LOW);
        digitalWrite(motorPin4, HIGH);
        delayMicroseconds(timeDelay);
        digitalWrite(motorPin1, HIGH);
        digitalWrite(motorPin3, LOW);
        delayMicroseconds(timeDelay);
        digitalWrite(motorPin4, LOW);
        digitalWrite(motorPin2, HIGH);
        delayMicroseconds(timeDelay);
        digitalWrite(motorPin3, HIGH);
        digitalWrite(motorPin1, LOW);
        delayMicroseconds(timeDelay);


        digitalWrite(motorPin8, LOW);
        digitalWrite(motorPin6, HIGH);
        delayMicroseconds(timeDelay);
        digitalWrite(motorPin7, LOW);
        digitalWrite(motorPin5, HIGH);
        delayMicroseconds(timeDelay);
        digitalWrite(motorPin6, LOW);
        digitalWrite(motorPin8, HIGH);
        delayMicroseconds(timeDelay);
        digitalWrite(motorPin5, LOW);
        digitalWrite(motorPin7, HIGH);
        delayMicroseconds(timeDelay);
      }
    }
    else if (y == "Right") {
      for (int i = 0; i < 75; i++) {

        digitalWrite(motorPin2, LOW);
        digitalWrite(motorPin4, HIGH);
        delayMicroseconds(timeDelay);
        digitalWrite(motorPin1, LOW);
        digitalWrite(motorPin3, HIGH);
        delayMicroseconds(timeDelay);
        digitalWrite(motorPin4, LOW);
        digitalWrite(motorPin2, HIGH);
        delayMicroseconds(timeDelay);
        digitalWrite(motorPin3, LOW);
        digitalWrite(motorPin1, HIGH);
        delayMicroseconds(timeDelay);


        digitalWrite(motorPin6, LOW);
        digitalWrite(motorPin8, HIGH);
        delayMicroseconds(timeDelay);
        digitalWrite(motorPin5, LOW);
        digitalWrite(motorPin7, HIGH);
        delayMicroseconds(timeDelay);
        digitalWrite(motorPin8, LOW);
        digitalWrite(motorPin6, HIGH);
        delayMicroseconds(timeDelay);
        digitalWrite(motorPin7, LOW);
        digitalWrite(motorPin5, HIGH);
        delayMicroseconds(timeDelay);
      }
    }
    else if (y == "Left") {
      for (int i = 0; i < 75; i++) {

        digitalWrite(motorPin2, LOW);
        digitalWrite(motorPin4, HIGH);
        delayMicroseconds(timeDelay);
        digitalWrite(motorPin1, HIGH);
        digitalWrite(motorPin3, LOW);
        delayMicroseconds(timeDelay);
        digitalWrite(motorPin4, LOW);
        digitalWrite(motorPin2, HIGH);
        delayMicroseconds(timeDelay);
        digitalWrite(motorPin3, HIGH);
        digitalWrite(motorPin1, LOW);
        delayMicroseconds(timeDelay);


        digitalWrite(motorPin6, LOW);
        digitalWrite(motorPin8, HIGH);
        delayMicroseconds(timeDelay);
        digitalWrite(motorPin5, HIGH);
        digitalWrite(motorPin7, LOW);
        delayMicroseconds(timeDelay);
        digitalWrite(motorPin8, LOW);
        digitalWrite(motorPin6, HIGH);
        delayMicroseconds(timeDelay);
        digitalWrite(motorPin7, HIGH);
        digitalWrite(motorPin5, LOW);
        delayMicroseconds(timeDelay);
      }

    }
    else if (y == "H") {
      digitalWrite(13, HIGH);
    }
    else {
      Serial.write((char*)commandbuffer);
      char* f = commandbuffer;
      p = strtok_r(f, ":", &e);
      Serial.print(p);
      Serial.print(" = ");
      String servoId = (char*)p;
      //  Second strtok iteration
      p = strtok_r(NULL, ":", &e);
      Serial.print(p);
      Serial.println("");
      int position = atoi(p);

      if (servoId == "Down") {
        for (int i = 0; i < position; i++) {
          digitalWrite(motorPin6, LOW);
          digitalWrite(motorPin8, HIGH);
          delayMicroseconds(timeDelay);
          digitalWrite(motorPin5, HIGH);
          digitalWrite(motorPin7, LOW);
          delayMicroseconds(timeDelay);
          digitalWrite(motorPin8, LOW);
          digitalWrite(motorPin6, HIGH);
          delayMicroseconds(timeDelay);
          digitalWrite(motorPin7, HIGH);
          digitalWrite(motorPin5, LOW);
          delayMicroseconds(timeDelay);


          digitalWrite(motorPin4, LOW);
          digitalWrite(motorPin2, HIGH);
          delayMicroseconds(timeDelay);
          digitalWrite(motorPin3, LOW);
          digitalWrite(motorPin1, HIGH);
          delayMicroseconds(timeDelay);
          digitalWrite(motorPin2, LOW);
          digitalWrite(motorPin4, HIGH);
          delayMicroseconds(timeDelay);
          digitalWrite(motorPin1, LOW);
          digitalWrite(motorPin3, HIGH);
          delayMicroseconds(timeDelay);
        }
      }
      else if (servoId == "Up") {
        for (int i = 0; i < position; i++) {

          digitalWrite(motorPin2, LOW);
          digitalWrite(motorPin4, HIGH);
          delayMicroseconds(timeDelay);
          digitalWrite(motorPin1, HIGH);
          digitalWrite(motorPin3, LOW);
          delayMicroseconds(timeDelay);
          digitalWrite(motorPin4, LOW);
          digitalWrite(motorPin2, HIGH);
          delayMicroseconds(timeDelay);
          digitalWrite(motorPin3, HIGH);
          digitalWrite(motorPin1, LOW);
          delayMicroseconds(timeDelay);


          digitalWrite(motorPin8, LOW);
          digitalWrite(motorPin6, HIGH);
          delayMicroseconds(timeDelay);
          digitalWrite(motorPin7, LOW);
          digitalWrite(motorPin5, HIGH);
          delayMicroseconds(timeDelay);
          digitalWrite(motorPin6, LOW);
          digitalWrite(motorPin8, HIGH);
          delayMicroseconds(timeDelay);
          digitalWrite(motorPin5, LOW);
          digitalWrite(motorPin7, HIGH);
          delayMicroseconds(timeDelay);
        }
      }
      else if (servoId == "Right") {
        for (int i = 0; i < position; i++) {

          digitalWrite(motorPin2, LOW);
          digitalWrite(motorPin4, HIGH);
          delayMicroseconds(timeDelay);
          digitalWrite(motorPin1, LOW);
          digitalWrite(motorPin3, HIGH);
          delayMicroseconds(timeDelay);
          digitalWrite(motorPin4, LOW);
          digitalWrite(motorPin2, HIGH);
          delayMicroseconds(timeDelay);
          digitalWrite(motorPin3, LOW);
          digitalWrite(motorPin1, HIGH);
          delayMicroseconds(timeDelay);


          digitalWrite(motorPin6, LOW);
          digitalWrite(motorPin8, HIGH);
          delayMicroseconds(timeDelay);
          digitalWrite(motorPin5, LOW);
          digitalWrite(motorPin7, HIGH);
          delayMicroseconds(timeDelay);
          digitalWrite(motorPin8, LOW);
          digitalWrite(motorPin6, HIGH);
          delayMicroseconds(timeDelay);
          digitalWrite(motorPin7, LOW);
          digitalWrite(motorPin5, HIGH);
          delayMicroseconds(timeDelay);
        }
      }
      else if (servoId == "Left") {
        for (int i = 0; i < position; i++) {

          digitalWrite(motorPin2, LOW);
          digitalWrite(motorPin4, HIGH);
          delayMicroseconds(timeDelay);
          digitalWrite(motorPin1, HIGH);
          digitalWrite(motorPin3, LOW);
          delayMicroseconds(timeDelay);
          digitalWrite(motorPin4, LOW);
          digitalWrite(motorPin2, HIGH);
          delayMicroseconds(timeDelay);
          digitalWrite(motorPin3, HIGH);
          digitalWrite(motorPin1, LOW);
          delayMicroseconds(timeDelay);


          digitalWrite(motorPin6, LOW);
          digitalWrite(motorPin8, HIGH);
          delayMicroseconds(timeDelay);
          digitalWrite(motorPin5, HIGH);
          digitalWrite(motorPin7, LOW);
          delayMicroseconds(timeDelay);
          digitalWrite(motorPin8, LOW);
          digitalWrite(motorPin6, HIGH);
          delayMicroseconds(timeDelay);
          digitalWrite(motorPin7, HIGH);
          digitalWrite(motorPin5, LOW);
          delayMicroseconds(timeDelay);
        }

      }
    }


  }











  int x = sonar.ping_cm();
  
  if (x < 10 && x != 0) {
    Serial.println("CUUL ASF");
    digitalWrite(50, LOW);

  }
  else {
    digitalWrite(50, LOW);
  }


}
