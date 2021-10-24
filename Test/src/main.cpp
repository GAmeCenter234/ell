#include <Arduino.h>

int led = 13;
void setup() {                  // the setup() method is executed only once
  pinMode(led, OUTPUT);       // the led PIN is declared as digital output
}

void loop() {                   // the loop() method is repeated
  digitalWrite(led, HIGH);      // switching on the led 
  delay(500);    // switching on the led 

  digitalWrite(led, LOW);       // switching off the led 
  delay(2000);       // swithhching off the led 
}