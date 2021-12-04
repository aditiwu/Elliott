#include <SoftwareSerial.h>
#include <SPFD5408_Adafruit_GFX.h>    // Core graphics library
#include <SPFD5408_Adafruit_TFTLCD.h> // Hardware-specific library
#include <SPFD5408_TouchScreen.h>
#define INPUT_SIZE 30
SoftwareSerial BTserial(A8, A9);
int timeDelay = 3000;
char k;
int state = 0;
#if defined(__SAM3X8E__)
#undef __FlashStringHelper::F(string_literal)
#define F(string_literal) string_literal
#endif
const int ledPin = 53;
const int inPin = 51;
#define YP A1  // must be an analog pin, use "An" notation!
#define XM A2  // must be an analog pin, use "An" notation!
#define YM 7   // can be a digital pin
#define XP 6   // can be a digital pin
#define TS_MINX 192
#define TS_MINY 130
#define TS_MAXX 870
#define TS_MAXY 870
TouchScreen ts = TouchScreen(XP, YP, XM, YM, 300);
#define LCD_CS A3
#define LCD_CD A2
#define LCD_WR A1
#define LCD_RD A0
// optional
#define LCD_RESET A4
#define  BLACK   0x0000
#define BLUE    0x001F
#define RED     0xF800
#define GREEN   0x07E0
#define CYAN    0x07FF
#define MAGENTA 0xF81F
#define YELLOW  0xFFE0
#define WHITE   0xFFFF
Adafruit_TFTLCD tft(LCD_CS, LCD_CD, LCD_WR, LCD_RD, LCD_RESET);
#define BOXSIZE 40
#define PENRADIUS 3
int oldcolor, currentcolor;
void setup() {
  // initialize digital pin 8 as an output.

  Serial.begin(9600);
  BTserial.begin(9600);
  
  Serial.println("HII");
  pinMode(ledPin, OUTPUT);  // declare LED as output
  pinMode(inPin, INPUT);
  Serial.println(F("Paint!"));
  tft.reset();
  tft.begin(0x9341); // SDFP5408
  pinMode(45, OUTPUT);
  tft.setRotation(0); // Need for the Mega, please changed for your choice or rotation initial

  // Border


  // Initial screen

  tft.setCursor (55, 50);
  tft.setTextSize (3);
  tft.setTextColor(RED);
  tft.println("SPFD5408");
  tft.setCursor (65, 85);
  tft.println("Library");
  tft.setCursor (55, 150);
  tft.setTextSize (2);
  tft.setTextColor(BLACK);
  tft.println("TFT Paint");

  tft.setCursor (80, 250);
  tft.setTextSize (1);
  tft.setTextColor(BLACK);
  tft.println("Touch to proceed");

  // Wait touch

  waitOneTouch();
  drawBorder();


}
int MINPRESSURE = 10;
int MAXPRESSURE = 1000;
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
     Serial.println((char*)commandbuffer);
     tft.setTextSize(5);
        tft.setTextColor(BLACK);
        tft.setCursor(120, 160);
        tft.print((char*)commandbuffer);;
        delay(1000);
        tft.fillScreen(WHITE);
     
}

}
TSPoint waitOneTouch() {

  // wait 1 touch to exit function

  TSPoint p;

  do {
    p = ts.getPoint();

    pinMode(XM, OUTPUT); //Pins configures again for TFT control
    pinMode(YP, OUTPUT);

  } while ((p.z < MINPRESSURE ) || (p.z > MAXPRESSURE));

  return p;
}
void drawBorder () {

  // Draw a border

  uint16_t width = tft.width() - 1;
  uint16_t height = tft.height() - 1;
  uint8_t border = 10;

  tft.fillScreen(RED);
  tft.fillRect(border, border, (width - border * 2), (height - border * 2), WHITE);

}
