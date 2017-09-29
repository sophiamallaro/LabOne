#include <OneWire.h>
#include <DallasTemperature.h>


#define ONE_WIRE_BUS 18
#define NUM_PINS 7

/* Set up a oneWire instance to communicate with any OneWire device*/
OneWire ourWire(ONE_WIRE_BUS);

/* Tell Dallas Temperature Library to use oneWire Library */
DallasTemperature sensors(&ourWire);

char serialInput;
double data;
const int switchPin = 2;
const int buttonPin = 3;
volatile byte buttonState = 0;
bool swich = true;

int pins[] = {
  10, 9, 8, 7, 6, 5, 4 //change to actual pin values
};


void setup()
{
  for (int i = 0; i < NUM_PINS; ++i) {
    pinMode(pins[i], OUTPUT);
  }

  pinMode(switchPin, INPUT);
  pinMode(buttonPin, INPUT);

  attachInterrupt(digitalPinToInterrupt(switchPin), switchChange_ISR, CHANGE);
  attachInterrupt(digitalPinToInterrupt(buttonPin), buttonPress_ISR, CHANGE);

  delay(1000);
  Serial.begin(9600);
  delay(5000);

  /* setup the DallasTemperature library */
  sensors.begin();
}


void loop()
{
  sensors.requestTemperatures(); // Send the command to get temperatures
  //int buttonState = digitalRead(buttonPin);
  if (Serial.available()) {
    serialInput = Serial.read();
    if (serialInput == 't') {
      if(swich) {
         //data = sensors.getTempCByIndex(0);
         Serial.print(sensors.getTempCByIndex(0));
         //Serial.print(9);
         //Serial.print(sensors.getTempFByIndex(0));
      }
    }

    if (serialInput == 'o') {
        if (swich) {
          //otherBlinky(11);
          blinky();
        }
    }

    if (serialInput == 'f') {
      if (swich) {
        clearBlinky();
      }
    }

    
    if (serialInput == 's') {
      if (swich) {
        Serial.print("y");
      } else {
        Serial.print("n");
      }
    }
    
    //delay(1);
  }
}

void blinky()
{
  //https://forum.arduino.cc/index.php?topic=119261.0 -- need to test against negative numbers
  //byte num = Serial.read(); // Get num from somewhere
  //sensors.getTempCByIndex(0)
  byte num = (byte) sensors.getTempCByIndex(0);
  //Serial.print("Value of temp: ");
  Serial.println(num);
  //Serial.print("Bitwise value: ");
  for (byte i=0; i < NUM_PINS; i++) {
    byte state = bitRead(num, i);
    digitalWrite(pins[i], state);
    //Serial.print(state);
  }
  //Serial.println();
}

void otherBlinky(double input)
{
  //https://forum.arduino.cc/index.php?topic=119261.0 -- need to test against negative numbers
  //byte num = Serial.read(); // Get num from somewhere
  //sensors.getTempCByIndex(0)
  byte num = (byte) input;
  //Serial.print("Value of temp: ");
  //Serial.println(num);
  //Serial.print("Bitwise value: ");
  for (byte i=0; i < NUM_PINS; i++) {
    byte state = bitRead(num, i);
    digitalWrite(pins[i], state);
    //Serial.print(state);
  }
  //Serial.println();
}

void clearBlinky()
{
  for (byte i=0; i < NUM_PINS; i++) {
    digitalWrite(pins[i], LOW);
  }
}

void buttonPress_ISR() 
{
  //Serial.println("FIRED ISR");
  if (swich) {
    buttonState = digitalRead(buttonPin);
    if(buttonState == LOW) {
      clearBlinky();
    } else {
      //otherBlinky(11);
      blinky();
    }
  }
}

void switchChange_ISR() {
  //Serial.println("Swich ISR");
  swich = !swich;
}

