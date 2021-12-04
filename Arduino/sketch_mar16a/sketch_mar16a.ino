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

int buttonPushCounter = 0;   // counter for the number of button presses
int buttonState = 0;         // current state of the button
int lastButtonState = 0;
//Define the pin to control the light
int ledPin = 53; // choose the pin for the LED
int inPin = 51;
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
  progmemPrintln(PSTR("TFT LCD test"));

#ifdef USE_ADAFRUIT_SHIELD_PINOUT
  progmemPrintln(PSTR("Using Adafruit 2.8\" TFT Arduino Shield Pinout"));
#else
  progmemPrintln(PSTR("Using Adafruit 2.8\" TFT Breakout Board Pinout"));
#endif

  tft.reset();



  tft.begin(0x9341);

  tft.setRotation(0);

  tft.fillScreen(BLACK);
  drawBitmap(25, 75, car, 195, 146, RED);
  delay(2000);
  drawBitmap(25, 75, car, 195, 146, BLUE);
  delay(2000);

  progmemPrintln(PSTR("Done!"));
  for (int i = 0; i <= 1000; i++) {
    tft.setTextSize(4);
    tft.fillScreen(BLACK);
    tft.setTextColor(RED);
    tft.setCursor(10, 0);
    tft.println("CHOOSE AN OPTION");
    buttonState = digitalRead(inPin2);
    if (buttonState != lastButtonState) {
      if (buttonState == HIGH) {
        buttonPushCounter++;
      } else {
        Serial.println("off");
      }
      delay(50);
    }

    lastButtonState = buttonState;
    while (buttonPushCounter == 1) {

      tft.setTextSize(4);
      tft.fillScreen(BLACK);
      tft.setTextColor(RED);
      tft.setCursor(80, 120);
      tft.println("IMAGE CAR CONTROL");
      delay(500);
      val = digitalRead(inPin);  // read input value
      if (val == HIGH) {
        q = 1;
        firstCase();
        return;
      }
      buttonState = digitalRead(inPin2);
      if (buttonState != lastButtonState) {
        if (buttonState == HIGH) {
          buttonPushCounter++;
        } else {
          Serial.println("off");
        }
        delay(50);
      }

      lastButtonState = buttonState;
    }

    while (buttonPushCounter == 2) {

      lastButtonState = buttonState;
      tft.setTextSize(4);
      tft.fillScreen(BLACK);
      tft.setTextColor(RED);
      tft.setCursor(80, 120);
      tft.println("Graph");
      delay(500);
      val = digitalRead(inPin);  // read input value
      if (val == HIGH) {
        q = 2;
        secondCase();
        return;
      }
      buttonState = digitalRead(inPin2);
      if (buttonState != lastButtonState) {
        if (buttonState == HIGH) {
          buttonPushCounter++;
        } else {
          Serial.println("off");
        }
        delay(50);
      }

      lastButtonState = buttonState;
    }
    while (buttonPushCounter == 3) {
      lastButtonState = buttonState;
      tft.setTextSize(4);
      tft.fillScreen(BLACK);
      tft.setTextColor(RED);
      tft.setCursor(80, 120);
      tft.println("Normal Control");
      delay(500);
      val = digitalRead(inPin);  // read input value
      if (val == HIGH) {
        q = 3;
        thirdCase();
        return;
      }
      buttonState = digitalRead(inPin2);
      if (buttonState != lastButtonState) {
        if (buttonState == HIGH) {
          buttonPushCounter++;
        } else {
          Serial.println("off");
        }
        delay(50);
      }
      lastButtonState = buttonState;
    }
    while (buttonPushCounter >= 4) {
      buttonPushCounter = 0;
    }
  }
}
void loop(void) {
}
TSPoint waitOneTouch() {

  // wait 1 touch to exit function

  TSPoint p;

  do {
    p = ts.getPoint();

    pinMode(XM, OUTPUT); //Pins configures again for TFT control
    pinMode(YP, OUTPUT);

  } while ((p.z < 10 ) || (p.z > 1000));

  return p;
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
void thirdCase() {
  while (q = 3) {
    tft.setTextSize(4);
    tft.fillScreen(BLACK);
    tft.setTextColor(RED);
    tft.setCursor(80, 120);
    tft.println("Welcome here");
    delay(2000);
    val = digitalRead(inPin);  // read input value
    if (val == HIGH) {         // check if the input is HIGH (button released)
      digitalWrite(ledPin, HIGH);
      BTserial.write('H');// turn LED OFF
    } else {
      digitalWrite(ledPin, LOW);  // turn LED ON
    }

  }
}

void secondCase() {
  while (q == 2) {
    tft.setTextSize(4);
    tft.fillScreen(BLACK);
    tft.setTextColor(RED);
    tft.setCursor(80, 120);
    tft.println("HIi");
    delay(2000);
    buttonState = digitalRead(inPin2);
    val = digitalRead(inPin);  // read input value
    if (val == HIGH) {         // check if the input is HIGH (button released)
      digitalWrite(ledPin, HIGH);
      BTserial.write('H');// turn LED OFF
    } else {
      digitalWrite(ledPin, LOW);  // turn LED ON
    }

  }
}

void firstCase() {
  while (q == 1) {
    tft.setTextSize(3);
    tft.setTextColor(RED);
    int joyX = analogRead(joyx);
    int joyY = analogRead(joyy);
    if (joyX > 600 && joyX != 0) {
      BTserial.write("Up");
      Serial.println("Up");
      tft.fillScreen(WHITE);
      drawBitmap(0, 0, carup, 240, 320, WHITE);
      delay(2000);
    }
    else if (joyX < 450 && joyX != 0) {
      BTserial.write("Down");
      Serial.println("Down");
      tft.fillScreen(BLACK);
      drawBitmap(0, 0, cardown, 240, 320, WHITE);
      delay(2000);
    }

    if (joyY > 600 && joyX != 0) {
      BTserial.write("Right");
      Serial.println("Right");
      tft.fillScreen(BLACK);
      drawBitmap(0, 0, carright, 240, 320, WHITE);
      delay(2000);
    }
    else if (joyY < 500 && joyX != 0) {
      BTserial.write("Left");
      Serial.println("Left");
      tft.fillScreen(BLACK);
      drawBitmap(0, 0, carleft, 240, 320, WHITE);
      delay(2000);
    }

    val = digitalRead(inPin);  // read input value
    if (val == HIGH) {         // check if the input is HIGH (button released)
      digitalWrite(ledPin, HIGH);
      BTserial.write('H');// turn LED OFF
    } else {
      digitalWrite(ledPin, LOW);  // turn LED ON
    }
  }
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

