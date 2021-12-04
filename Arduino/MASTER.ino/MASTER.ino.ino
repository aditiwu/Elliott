#include <SoftwareSerial.h>
#include <SPFD5408_Adafruit_GFX.h>    // Core graphics library
#include <SPFD5408_Adafruit_TFTLCD.h> // Hardware-specific library
#include <SPFD5408_TouchScreen.h>
// *** SPFD5408 change -- End
#define INPUT_SIZE 30
SoftwareSerial BTserial(A8, A9);
#if defined(__SAM3X8E__)
#undef __FlashStringHelper::F(string_literal)
#define F(string_literal) string_literal
#endif
static int q = 0;

#include <DS3231.h>

// Init the DS3231 using the hardware interface
DS3231  rtc(SDA, SCL);
double volts;
double bvolts;
double pmvolts;
#define MINPRESSURE 10
#define MAXPRESSURE 1000
#define YP A1  // must be an analog pin, use "An" notation!
#define XM A2  // must be an analog pin, use "An" notation!
#define YM 7   // can be a digital pin
#define XP 6   // can be a digital pin
#include <Servo.h>
Servo myservo;
int value;
// Original values
//#define TS_MINX 150
//#define TS_MINY 120
//#define TS_MAXX 920
//#define TS_MAXY 940
static int qb = 1;
// Calibrate values
#define TS_MINX 210
#define TS_MINY 905
#define TS_MAXX 877
#define TS_MAXY 128
boolean graph_1 = true;
boolean graph_2 = true;
boolean graph_3 = true;
boolean graph_4 = true;
boolean graph_5 = true;
boolean graph_6 = true;
boolean graph_7 = true;
int buttonPushCounter = 0;   // counter for the number of button presses
int buttonState = 0;         // current state of the button
int lastButtonState = 0;
//Define the pin to control the light
int ledPin = 53; // choose the pin for the LED
int inPin = 51;
char *p;
char *e;
int inPin2 = 22;// choose the input pin (for a pushbutton)
int val = 0;
static int val1 = 0;
const int joyx = A13;
const int joyy = A14;
#define YP A1  // must be an analog pin, use "An" notation!
#define XM A2  // must be an analog pin, use "An" notation!
#define YM 7   // can be a digital pin
#define XP 6   // can be a digital pin
#define TS_MINX 192
#define TS_MINY 130
#define TS_MAXX 870
#define TS_MAXY 870
TouchScreen ts = TouchScreen(XP, YP, XM, YM, 300);
int minVal = 265; int maxVal = 402;
#define LCD_CS A3
#define LCD_CD A2
#define LCD_WR A1
#define LCD_RD A0
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

extern uint8_t talking_bot[];
extern uint8_t car[];
extern uint8_t carup[];
extern uint8_t carright[];
extern uint8_t carleft[];
extern uint8_t cardown[];

void setup(void) {

  Serial.begin(9600);
  BTserial.begin(9600);
  pinMode(ledPin, OUTPUT);
  pinMode(inPin, INPUT);
  pinMode(inPin2, INPUT);
  myservo.attach(A11);

  tft.reset();

  rtc.begin();

  tft.begin(0x9341);

  tft.setRotation(0);
  tft.fillScreen(BLACK);
  drawBitmap(25, 75, car, 195, 146, RED);
  delay(2000);
  drawBitmap(25, 75, car, 195, 146, BLUE);
  delay(2000);
  for (int i = 0; i <= 1000; i++) {
    tft.setTextSize(4);
    tft.fillScreen(BLACK);
    tft.setTextColor(RED);
    tft.setCursor(10, 0);
    tft.println("CHOOSE AN OPTION");

    while (qb == 1) {
      tft.setTextSize(4);
      tft.fillScreen(BLACK);
      tft.setTextColor(RED);
      tft.setCursor(10, 120);
      tft.println("IMAGE CAR CONTROL");
      digitalWrite(13, HIGH);
      TSPoint p = ts.getPoint();
      digitalWrite(13, LOW);

      // if sharing pins, you'll need to fix the directions of the touchscreen pins
      //pinMode(XP, OUTPUT);
      pinMode(XM, OUTPUT);
      pinMode(YP, OUTPUT);
      if (p.z > 10 && p.z < 1000) {
        Serial.print("("); Serial.print(p.x);
        Serial.print(", "); Serial.print(p.y);
        Serial.println(")");
        if (p.x > 557) {
          q = 1;
          firstCase();
          return;
        }
        else if (p.x < 556) {
          Serial.println("YOU MADE IT HERE");
          caseOne();
          return;
        }
      }
    }




  }
}

void loop(void) {
}
void caseOne() {
  Serial.println("WELCOME");
  Serial.println(qb);
  while (qb == 1)
  {
    tft.setTextSize(4);
    Serial.println("WELCOME AGAIN");
    tft.fillScreen(BLACK);
    tft.setTextColor(RED);
    tft.setCursor(10, 120);
    tft.println("NORMAL CONTROL");
    digitalWrite(13, HIGH);
    TSPoint p = ts.getPoint();
    digitalWrite(13, LOW);

    // if sharing pins, you'll need to fix the directions of the touchscreen pins
    //pinMode(XP, OUTPUT);
    pinMode(XM, OUTPUT);
    pinMode(YP, OUTPUT);
    if (p.z > 10 && p.z < 1000) {
      Serial.print("("); Serial.print(p.x);
      Serial.print(", "); Serial.print(p.y);
      Serial.println(")");
      if (p.x > 557) {
        q = 2;
        secondCase();
        return;
      }
      else if (p.x < 556) {
        q = 1;
        caseThree();
        return;
      }
    }
  }
}
void caseThree() {

  while (qb == 1) {
    tft.setTextSize(4);
    tft.fillScreen(BLACK);
    tft.setTextColor(RED);
    tft.setCursor(10, 120);
    tft.println("GRAPH");
    digitalWrite(13, HIGH);
    TSPoint p = ts.getPoint();
    digitalWrite(13, LOW);

    // if sharing pins, you'll need to fix the directions of the touchscreen pins
    //pinMode(XP, OUTPUT);
    pinMode(XM, OUTPUT);
    pinMode(YP, OUTPUT);
    if (p.z > 10 && p.z < 1000) {
      Serial.print("("); Serial.print(p.x);
      Serial.print(", "); Serial.print(p.y);
      Serial.println(")");
      if (p.x > 557) {
        q = 1;
        thirdCase();
        return;
      }
      else if (p.x < 556) {
        q = 1;
        caseFour();
        return;
      }
    }
  }
}
void caseFour() {
  while (qb == 1) {
    tft.setTextSize(4);
    tft.fillScreen(BLACK);
    tft.setTextColor(RED);
    tft.setCursor(10, 120);
    tft.println("SERIAL   COMMUNICATION");
    digitalWrite(13, HIGH);
    TSPoint p = ts.getPoint();
    digitalWrite(13, LOW);

    // if sharing pins, you'll need to fix the directions of the touchscreen pins
    //pinMode(XP, OUTPUT);
    pinMode(XM, OUTPUT);
    pinMode(YP, OUTPUT);
    if (p.z > 10 && p.z < 1000) {
      Serial.print("("); Serial.print(p.x);
      Serial.print(", "); Serial.print(p.y);
      Serial.println(")");
      if (p.x > 557) {
        q = 1;
        fourthCase();
        return;
      }
    }
  }
}
int w;
int waitOneTouch() {

  // wait 1 touch to exit function

  TSPoint p;

  do {
    p = ts.getPoint();

    pinMode(XM, OUTPUT); //Pins configures again for TFT control
    pinMode(YP, OUTPUT);
    w = HIGH;

  } while ((p.z < 10 ) || (p.z > 1000) || (p.x < 556));

  return w;
}

void drawBitmap(int16_t x, int16_t y,
                const uint8_t *bitmap, int16_t w, int16_t h, uint16_t color) {

  int16_t i, j, byteWidth = (w + 7) / 8;
  uint8_t byte;

  for (j = 0; j < h; j++) {
    for (i = 0; i < w; i++) {
      if (i & 7) byte <<= 1;
      else      byte   = pgm_read_byte(bitmap + j * byteWidth + i / 8);
      if (byte & 0x80) tft.drawPixel(x + i, y + j, color);
    }
  }
}

void fourthCase() {
  tft.fillScreen(BLACK);
  drawBitmap(0, 0, talking_bot, 241, 320, WHITE);
  tft.fillRect(0, 100, 241, 220, WHITE);
  delay(2000);
  while (qb == 1) {
    int i = 0;
    char commandbuffer[100];
    if (Serial.available()) { // only send data back if data has been sent
      delay(100);
      tft.fillRect(0, 100, 241, 220, WHITE);
      while ( Serial.available() && i < 99) {
        commandbuffer[i++] = Serial.read();
      }
      commandbuffer[i++] = '\0';
    }
    myservo.write(120);

    if (i > 0)
    {
      String y = (char*)commandbuffer;
      char* f = commandbuffer;
      p = strtok_r(f, ": ", &e);
      String servoId = (char*)p;
      p = strtok_r(NULL, ":", &e);
      String command = (char*)p;
      if (servoId == "ELLIOT")
      {
        tft.setTextColor(RED);
        tft.setTextSize(2);
        tft.setRotation(1);
        tft.setCursor(110, 68);
        tft.println(command);
        tft.setRotation(0);
      }
      else if (servoId == "YOU")
      {
        tft.setTextColor(RED);
        tft.setTextSize(2);
        tft.setRotation(1);
        tft.setCursor(110, 165);
        tft.println(command);
        tft.setRotation(0);
      }
    }
    digitalWrite(13, HIGH);
    TSPoint p = ts.getPoint();
    digitalWrite(13, LOW);

    // if sharing pins, you'll need to fix the directions of the touchscreen pins
    //pinMode(XP, OUTPUT);
    pinMode(XM, OUTPUT);
    pinMode(YP, OUTPUT);
    if (p.z > 10 && p.z < 1000) {
      Serial.print("("); Serial.print(p.x);
      Serial.print(", "); Serial.print(p.y);
      Serial.println(")");
      if (p.x > 557) {
        Serial.println("HIGH");
        digitalWrite(ledPin, HIGH);
      }
      else if (p.x < 556) {
        Serial.println("LOW");
        digitalWrite(ledPin, HIGH);
      }

    }

  }
}

void thirdCase() {
  tft.setRotation(1);
  tft.setTextSize(4);
  tft.fillScreen(BLACK);
  //tft.setRotation(2);
  while (qb == 1) {
    int joyX = analogRead(joyx);
    int joyY = analogRead(joyy);
    Serial.println("ATLEAST YOU ARE HERE");
    DrawBarChartV(25,  200, 30, 140, 0, 1000 , 100, joyY , 4 , 0, BLUE, YELLOW, BLUE, WHITE, BLACK, "Bits", graph_1);
    DrawDial(225, 140, 100, 0, 1000, 200, 240, joyX, 4, 0, RED, WHITE, BLACK, "Volts", graph_7);

    if (joyX > 600 && joyX != 0) {
      BTserial.write("Up");
      Serial.println("Up");

    }
    else if (joyX < 450) {
      BTserial.write("Down");
      Serial.println("Down");
    }

    if (joyY > 600 && joyX != 0) {
      BTserial.write("Right");
      Serial.println("Right");

    }
    else if (joyY < 500 && joyX != 0) {
      BTserial.write("Left");
      Serial.println("Left");

    }
    digitalWrite(13, HIGH);
    TSPoint p = ts.getPoint();
    digitalWrite(13, LOW);

    // if sharing pins, you'll need to fix the directions of the touchscreen pins
    //pinMode(XP, OUTPUT);
    pinMode(XM, OUTPUT);
    pinMode(YP, OUTPUT);
    if (p.z > 10 && p.z < 1000) {
      Serial.print("("); Serial.print(p.x);
      Serial.print(", "); Serial.print(p.y);
      Serial.println(")");
      if (p.x > 557) {
        Serial.println("HIGH");
        digitalWrite(ledPin, HIGH);
      }
      else if (p.x < 556) {
        Serial.println("LOW");
        digitalWrite(ledPin, HIGH);
      }

    }
  }
}

void secondCase() {
  while (qb == 1) {
    tft.setTextSize(4);
    tft.fillScreen(BLACK);
    int joyX = analogRead(joyx);
    int joyY = analogRead(joyy);
    tft.setTextColor(RED);
    tft.setTextSize(4);
    tft.setCursor(50, 50);
    tft.println(rtc.getDOWStr());
    tft.setCursor(0, 120);
    tft.println(rtc.getDateStr());
    tft.setCursor(10, 200);
    tft.println(rtc.getTimeStr());
   





  }
}

void firstCase() {
  while (qb == 1) {
    tft.setTextSize(3);
    tft.setTextColor(RED);
    int joyX = analogRead(joyx);
    int joyY = analogRead(joyy);
    if (joyX > 800 && joyX != 0) {
      BTserial.write("Down");
      Serial.println("Down");
      tft.fillScreen(BLACK);
      drawBitmap(0, 0, cardown, 240, 320, WHITE);
      delay(2000);
    }
    else if (joyX < 300) {
      BTserial.write("Up");
      Serial.println("Up");
      tft.fillScreen(BLACK);
      drawBitmap(0, 0, carup, 240, 320, WHITE);
      delay(2000);
    }

    if (joyY > 800 && joyX != 0) {
      BTserial.write("Left");
      Serial.println("Left");
      tft.fillScreen(BLACK);
      drawBitmap(0, 0, carleft, 240, 320, WHITE);
      delay(2000);
    }
    else if (joyY < 30 && joyX != 0) {
      BTserial.write("Right");
      Serial.println("Right");
      tft.fillScreen(BLACK);
      drawBitmap(0, 0, carright, 240, 320, WHITE);
      delay(2000);
    }
    digitalWrite(13, HIGH);
    TSPoint p = ts.getPoint();
    digitalWrite(13, LOW);

    // if sharing pins, you'll need to fix the directions of the touchscreen pins
    //pinMode(XP, OUTPUT);
    pinMode(XM, OUTPUT);
    pinMode(YP, OUTPUT);
    if (p.z > 10 && p.z < 1000) {
      Serial.print("("); Serial.print(p.x);
      Serial.print(", "); Serial.print(p.y);
      Serial.println(")");
      if (p.x > 557) {
        Serial.println("HIGH");
        digitalWrite(ledPin, HIGH);
      }
      else if (p.x < 556) {
        Serial.println("LOW");
        digitalWrite(ledPin, HIGH);
      }

    }

  }
}
//tft.
//drawPixel(xpos, ypos,color);
//drawLine(starxpos, startypos, endxpos, endypos, color);
//drawFastVLine(startxpos, startypos, lenght, color);
//drawFastHLine(startxpos, startypos, lenght, color);
//drawRect(startxpos, startypos, w, h, color);
//fillRect(startxpos, startypos, w, h, color);
//drawRoundRect(startxpos, startypos, w, h, rounding rad, color);
//fillRoundRect(startxpos, startypos, w, h, rounding rad, color);
//drawCircle(centrex, centrey, rad, color);
//fillCircle(centrex, centrey, rad, color);
//drawTriangle(point0x, point0y, point1x, point1y, point2x, point2y, color)
//fillTriangle(point0x, point0y, point1x, point1y, point2x, point2y, color)


unsigned long testLines(uint16_t color) {
  unsigned long start, t;
  int           x1, y1, x2, y2,
                w = tft.width(),
                h = tft.height();

  tft.fillScreen(BLACK);

  x1 = y1 = 0;
  y2    = h - 1;
  start = micros();
  for (x2 = 0; x2 < w; x2 += 6) tft.drawLine(x1, y1, x2, y2, color);
  x2    = w - 1;
  for (y2 = 0; y2 < h; y2 += 6) tft.drawLine(x1, y1, x2, y2, color);
  t     = micros() - start; // fillScreen doesn't count against timing

  tft.fillScreen(BLACK);

  x1    = w - 1;
  y1    = 0;
  y2    = h - 1;
  start = micros();
  for (x2 = 0; x2 < w; x2 += 6) tft.drawLine(x1, y1, x2, y2, color);
  x2    = 0;
  for (y2 = 0; y2 < h; y2 += 6) tft.drawLine(x1, y1, x2, y2, color);
  t    += micros() - start;

  tft.fillScreen(BLACK);

  x1    = 0;
  y1    = h - 1;
  y2    = 0;
  start = micros();
  for (x2 = 0; x2 < w; x2 += 6) tft.drawLine(x1, y1, x2, y2, color);
  x2    = w - 1;
  for (y2 = 0; y2 < h; y2 += 6) tft.drawLine(x1, y1, x2, y2, color);
  t    += micros() - start;

  tft.fillScreen(BLACK);

  x1    = w - 1;
  y1    = h - 1;
  y2    = 0;
  start = micros();
  for (x2 = 0; x2 < w; x2 += 6) tft.drawLine(x1, y1, x2, y2, color);
  x2    = 0;
  for (y2 = 0; y2 < h; y2 += 6) tft.drawLine(x1, y1, x2, y2, color);

  return micros() - start;
}

unsigned long testFastLines(uint16_t color1, uint16_t color2) {
  unsigned long start;
  int           x, y, w = tft.width(), h = tft.height();

  tft.fillScreen(BLACK);
  start = micros();
  for (y = 0; y < h; y += 5) tft.drawFastHLine(0, y, w, color1);
  for (x = 0; x < w; x += 5) tft.drawFastVLine(x, 0, h, color2);

  return micros() - start;
}

unsigned long testRects(uint16_t color) {
  unsigned long start;
  int           n, i, i2,
                cx = tft.width()  / 2,
                cy = tft.height() / 2;

  tft.fillScreen(BLACK);
  n     = min(tft.width(), tft.height());
  start = micros();
  for (i = 2; i < n; i += 6) {
    i2 = i / 2;
    tft.drawRect(cx - i2, cy - i2, i, i, color);
  }

  return micros() - start;
}

unsigned long testFilledRects(uint16_t color1, uint16_t color2) {
  unsigned long start, t = 0;
  int           n, i, i2,
                cx = tft.width()  / 2 - 1,
                cy = tft.height() / 2 - 1;

  tft.fillScreen(BLACK);
  n = min(tft.width(), tft.height());
  for (i = n; i > 0; i -= 6) {
    i2    = i / 2;
    start = micros();
    tft.fillRect(cx - i2, cy - i2, i, i, color1);
    t    += micros() - start;
    // Outlines are not included in timing results
    tft.drawRect(cx - i2, cy - i2, i, i, color2);
  }

  return t;
}

unsigned long testFilledCircles(uint8_t radius, uint16_t color) {
  unsigned long start;
  int x, y, w = tft.width(), h = tft.height(), r2 = radius * 2;

  tft.fillScreen(BLACK);
  start = micros();
  for (x = radius; x < w; x += r2) {
    for (y = radius; y < h; y += r2) {
      tft.fillCircle(x, y, radius, color);
    }
  }

  return micros() - start;
}

unsigned long testCircles(uint8_t radius, uint16_t color) {
  unsigned long start;
  int           x, y, r2 = radius * 2,
                      w = tft.width()  + radius,
                      h = tft.height() + radius;

  // Screen is not cleared for this one -- this is
  // intentional and does not affect the reported time.
  start = micros();
  for (x = 0; x < w; x += r2) {
    for (y = 0; y < h; y += r2) {
      tft.drawCircle(x, y, radius, color);
    }
  }

  return micros() - start;
}

unsigned long testTriangles() {
  unsigned long start;
  int           n, i, cx = tft.width()  / 2 - 1,
                      cy = tft.height() / 2 - 1;

  tft.fillScreen(BLACK);
  n     = min(cx, cy);
  start = micros();
  for (i = 0; i < n; i += 5) {
    tft.drawTriangle(
      cx    , cy - i, // peak
      cx - i, cy + i, // bottom left
      cx + i, cy + i, // bottom right
      tft.color565(0, 0, i));
  }

  return micros() - start;
}

unsigned long testFilledTriangles() {
  unsigned long start, t = 0;
  int           i, cx = tft.width()  / 2 - 1,
                   cy = tft.height() / 2 - 1;

  tft.fillScreen(BLACK);
  start = micros();
  for (i = min(cx, cy); i > 10; i -= 5) {
    start = micros();
    tft.fillTriangle(cx, cy - i, cx - i, cy + i, cx + i, cy + i,
                     tft.color565(0, i, i));
    t += micros() - start;
    tft.drawTriangle(cx, cy - i, cx - i, cy + i, cx + i, cy + i,
                     tft.color565(i, i, 0));
  }

  return t;
}

unsigned long testRoundRects() {
  unsigned long start;
  int           w, i, i2,
                cx = tft.width()  / 2 - 1,
                cy = tft.height() / 2 - 1;

  tft.fillScreen(BLACK);
  w     = min(tft.width(), tft.height());
  start = micros();
  for (i = 0; i < w; i += 6) {
    i2 = i / 2;
    tft.drawRoundRect(cx - i2, cy - i2, i, i, i / 8, tft.color565(i, 0, 0));
  }

  return micros() - start;
}

unsigned long testFilledRoundRects() {
  unsigned long start;
  int           i, i2,
                cx = tft.width()  / 2 - 1,
                cy = tft.height() / 2 - 1;

  tft.fillScreen(BLACK);
  start = micros();
  for (i = min(tft.width(), tft.height()); i > 20; i -= 6) {
    i2 = i / 2;
    tft.fillRoundRect(cx - i2, cy - i2, i, i, i / 8, tft.color565(0, i, 0));
  }

  return micros() - start;
}

// Copy string from flash to serial port
// Source string MUST be inside a PSTR() declaration!
void progmemPrint(const char *str) {
  char c;
  while (c = pgm_read_byte(str++)) Serial.print(c);
}

// Same as above, with trailing newline
void progmemPrintln(const char *str) {
  progmemPrint(str);
  Serial.println();
}
void DrawBarChartV(double x , double y , double w, double h , double loval , double hival , double inc , double curval ,  int dig , int dec, unsigned int barcolor, unsigned int voidcolor, unsigned int bordercolor, unsigned int textcolor, unsigned int backcolor, String label, boolean & redraw)
{

  double stepval, range;
  double my, level;
  double i, data;
  // draw the border, scale, and label once
  // avoid doing this on every update to minimize flicker
  if (redraw == true) {
    redraw = false;

    tft.drawRect(x - 1, y - h - 1, w + 2, h + 2, bordercolor);
    tft.setTextColor(textcolor, backcolor);
    tft.setTextSize(2);
    tft.setCursor(x , y + 10);
    tft.println(label);
    // step val basically scales the hival and low val to the height
    // deducting a small value to eliminate round off errors
    // this val may need to be adjusted
    stepval = ( inc) * (double (h) / (double (hival - loval))) - .001;
    for (i = 0; i <= h; i += stepval) {
      my =  y - h + i;
      tft.drawFastHLine(x + w + 1, my,  5, textcolor);
      // draw lables
      tft.setTextSize(1);
      tft.setTextColor(textcolor, backcolor);
      tft.setCursor(x + w + 12, my - 3 );
      data = hival - ( i * (inc / stepval));
      tft.println(Format(data, dig, dec));
    }
  }
  // compute level of bar graph that is scaled to the  height and the hi and low vals
  // this is needed to accompdate for +/- range
  level = (h * (((curval - loval) / (hival - loval))));
  // draw the bar graph
  // write a upper and lower bar to minimize flicker cause by blanking out bar and redraw on update
  tft.fillRect(x, y - h, w, h - level,  voidcolor);
  tft.fillRect(x, y - level, w,  level, barcolor);
  // write the current value
  tft.setTextColor(textcolor, backcolor);
  tft.setTextSize(2);
  tft.setCursor(x , y - h - 23);
  tft.println(Format(curval, dig, dec));

}

/*
  This method will draw a dial-type graph for single input
  it has a rather large arguement list and is as follows

  &d = display object name
  cx = center position of dial
  cy = center position of dial
  r = radius of the dial
  loval = lower value of the scale (can be negative)
  hival = upper value of the scale
  inc = scale division between loval and hival
  sa = sweep angle for the dials scale
  curval = date to graph (must be between loval and hival)
  dig = format control to set number of digits to display (not includeing the decimal)
  dec = format control to set number of decimals to display (not includeing the decimal)
  needlecolor = color of the needle
  dialcolor = color of the dial
  textcolor = color of all text (background is dialcolor)
  label = bottom lable text for the graph
  redraw = flag to redraw display only on first pass (to reduce flickering)
*/

void DrawDial(int cx, int cy, int r, double loval , double hival , double inc, double sa, double curval,  int dig , int dec, unsigned int needlecolor, unsigned int dialcolor, unsigned int  textcolor, String label, boolean & redraw) {

  double ix, iy, ox, oy, tx, ty, lx, rx, ly, ry, i, offset, stepval, data, angle;
  double degtorad = .0174532778;
  static double px = cx, py = cy, pix = cx, piy = cy, plx = cx, ply = cy, prx = cx, pry = cy;

  // draw the dial only one time--this will minimize flicker
  if ( redraw == true) {
    redraw = false;
    tft.fillCircle(cx, cy, r - 2, dialcolor);
    tft.drawCircle(cx, cy, r, needlecolor);
    tft.drawCircle(cx, cy, r - 1, needlecolor);
    tft.setTextColor(textcolor, dialcolor);
    tft.setTextSize(2);
    tft.setCursor(cx - 25, cy + 40);
    tft.println(label);

  }
  // draw the current value
  tft.setTextSize(2);
  tft.setTextColor(textcolor, dialcolor);
  tft.setCursor(cx - 25, cy + 20 );
  tft.println(Format(curval, dig, dec));
  // center the scale about the vertical axis--and use this to offset the needle, and scale text
  offset = (270 +  sa / 2) * degtorad;
  // find hte scale step value based on the hival low val and the scale sweep angle
  // deducting a small value to eliminate round off errors
  // this val may need to be adjusted
  stepval = ( inc) * (double (sa) / (double (hival - loval))) + .00;
  // draw the scale and numbers
  // note draw this each time to repaint where the needle was
  for (i = 0; i <= sa; i += stepval) {
    angle = ( i  * degtorad);
    angle = offset - angle ;
    ox =  (r - 2) * cos(angle) + cx;
    oy =  (r - 2) * sin(angle) + cy;
    ix =  (r - 10) * cos(angle) + cx;
    iy =  (r - 10) * sin(angle) + cy;
    tx =  (r - 30) * cos(angle) + cx;
    ty =  (r - 30) * sin(angle) + cy;
    tft.drawLine(ox, oy, ix, iy, textcolor);
    tft.setTextSize(1.5);
    tft.setTextColor(textcolor, dialcolor);
    tft.setCursor(tx - 10, ty );
    data = hival - ( i * (inc / stepval)) ;
    tft.println(Format(data, dig, dec));
  }
  // compute and draw the needle
  angle = (sa * (1 - (((curval - loval) / (hival - loval)))));
  angle = angle * degtorad;
  angle = offset - angle  ;
  ix =  (r - 10) * cos(angle) + cx;
  iy =  (r - 10) * sin(angle) + cy;
  // draw a triangle for the needle (compute and store 3 vertiticies)
  lx =  5 * cos(angle - 90 * degtorad) + cx;
  ly =  5 * sin(angle - 90 * degtorad) + cy;
  rx =  5 * cos(angle + 90 * degtorad) + cx;
  ry =  5 * sin(angle + 90 * degtorad) + cy;
  // first draw the previous needle in dial color to hide it
  // note draw performance for triangle is pretty batft...

  //tft.fillTriangle (pix, piy, plx, ply, prx, pry, dialcolor);
  //tft.fillTriangle (pix, piy, plx, ply, prx, pry, dialcolor);

  //tft.fillTriangle (pix, piy, plx, ply, prx - 20, pry - 20, dialcolor);
  //tft.fillTriangle (pix, piy, prx, pry, prx + 20, pry + 20, dialcolor);

  tft.fillTriangle (pix, piy, plx, ply, prx, pry, dialcolor);
  tft.drawTriangle (pix, piy, plx, ply, prx, pry, dialcolor);

  // then draw the old needle in need color to display it
  tft.fillTriangle (ix, iy, lx, ly, rx, ry, needlecolor);
  tft.drawTriangle (ix, iy, lx, ly, rx, ry, textcolor);

  // draw a cute little dial center
  tft.fillCircle(cx, cy, 8, textcolor);
  //save all current to old so the previous dial can be hidden
  pix = ix;
  piy = iy;
  plx = lx;
  ply = ly;
  prx = rx;
  pry = ry;

}


void DrawBarChartH(double x , double y , double w, double h , double loval , double hival , double inc , double curval ,  int dig , int dec, unsigned int barcolor, unsigned int voidcolor, unsigned int bordercolor, unsigned int textcolor, unsigned int backcolor, String label, boolean & redraw)
{
  double stepval, range;
  double mx, level;
  double i, data;

  // draw the border, scale, and label once
  // avoid doing this on every update to minimize flicker
  // draw the border and scale
  if (redraw == true) {
    redraw = false;
    tft.drawRect(x , y , w, h, bordercolor);
    tft.setTextColor(textcolor, backcolor);
    tft.setTextSize(2);
    tft.setCursor(x , y - 20);
    tft.println(label);
    // step val basically scales the hival and low val to the width
    stepval =  inc * (double (w) / (double (hival - loval))) - .00001;
    // draw the text
    for (i = 0; i <= w; i += stepval) {
      tft.drawFastVLine(i + x , y + h + 1,  5, textcolor);
      // draw lables
      tft.setTextSize(1);
      tft.setTextColor(textcolor, backcolor);
      tft.setCursor(i + x , y + h + 10);
      // addling a small value to eliminate round off errors
      // this val may need to be adjusted
      data =  ( i * (inc / stepval)) + loval + 0.00001;
      tft.println(Format(data, dig, dec));
    }
  }
  // compute level of bar graph that is scaled to the width and the hi and low vals
  // this is needed to accompdate for +/- range capability
  // draw the bar graph
  // write a upper and lower bar to minimize flicker cause by blanking out bar and redraw on update
  level = (w * (((curval - loval) / (hival - loval))));
  tft.fillRect(x + level + 1, y + 1, w - level - 2, h - 2,  voidcolor);
  tft.fillRect(x + 1, y + 1 , level - 1,  h - 2, barcolor);
  // write the current value
  tft.setTextColor(textcolor, backcolor);
  tft.setTextSize(2);
  tft.setCursor(x + w + 10 , y + 5);
  tft.println(Format(curval, dig, dec));
}


String Format(double val, int dec, int dig ) {
  int addpad = 0;
  char sbuf[20];
  String condata = (dtostrf(val, dec, dig, sbuf));


  int slen = condata.length();
  for ( addpad = 1; addpad <= dec + dig - slen; addpad++) {
    condata = " " + condata;
  }
  return (condata);

}
#define MINPRESSURE 10
#define MAXPRESSURE 1000

