#include <OneWire.h>
#include <DallasTemperature.h>


#define ONE_WIRE_BUS 16
#define NUM_PINS 7

/* Set up a oneWire instance to communicate with any OneWire device*/
OneWire ourWire(ONE_WIRE_BUS);

/* Tell Dallas Temperature Library to use oneWire Library */
DallasTemperature sensors(&ourWire);

char serialInput;
double data;

int pins[] = {
  17, 18, 19, 20, 21, 0, 1
};


void setup()
{
  for (int i = 0; i < NUM_PINS; ++i) {
    pinMode(pins[i], OUTPUT);
  }

  delay(1000);
  Serial.begin(9600);
  delay(1000);

/* setup the DallasTemperature library */
sensors.begin();
}


void loop()
{
  sensors.requestTemperatures(); // Send the command to get temperatures
  if (Serial.available()) {
    serialInput = Serial.read();
    if (serialInput == 't') {
       //data = sensors.getTempCByIndex(0);
       Serial.print(sensors.getTempCByIndex(0));
       //Serial.println(" Degrees C");
       //Serial.print(sensors.getTempFByIndex(0));
       //Serial.println(" Degrees F");
    }

    if (serialInput == 'o') {
      //for (double p = -128.5; p < 128.0; p = p + 1.0 ) {
        blinky(11);
      //}
    }

    if (serialInput == 'f') {
      clearBlinky();
    }
  }
}

void blinky(double input)
{
  //byte num = Serial.read(); // Get num from somewhere
  byte num = (byte) input;
  Serial.print("Value of input: ");
  Serial.println(input);
  Serial.print("Bitwise value: ");
  for (byte i=0; i < NUM_PINS; i++) {
    byte state = bitRead(num, i);
    digitalWrite(pins[i], state);
    Serial.print(state);
  }
  Serial.println();
}

void clearBlinky()
{
  for (byte i=0; i < NUM_PINS; i++) {
    digitalWrite(pins[i], LOW);
  }
}

