#include <Servo.h>
Servo myservo;
int value;
int x;
void setup() {
x = analogRead(A11);
  Serial.begin(9600);
  Serial.println(x);
  

}

void loop() {
 x = analogRead(A11);
Serial.println(x);
}
