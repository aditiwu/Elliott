#include <SoftwareSerial.h>

#define INPUT_SIZE 30
SoftwareSerial BTserial(A1, A2);
int timeDelay = 3000;
char k;
int state = 0;

void setup() {
  // initialize digital pin 8 as an output.

  Serial.begin(9600);
  BTserial.begin(9600);
  
  Serial.println("HII");
  pinMode(13, OUTPUT);  // declare LED as output




}

void loop() {

    

int i=0;
  char commandbuffer[100];

  if(BTserial.available()){
     delay(100);
     while( BTserial.available() && i< 99) {
        commandbuffer[i++] = BTserial.read();
     }
     commandbuffer[i++]='\0';
  }

  if(i>0)
{
    String y = (char*)commandbuffer;
     Serial.println(y);
     
}

}

