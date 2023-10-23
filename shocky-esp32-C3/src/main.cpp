#include <Arduino.h>
#include "network/network.h"

//#include <collar.h>
#include "shock.h"






// Set this to whichever pin has the 433MHz transmitter connected to it


// Either set this to the id of the original transmitter,
// or make a value up and re-pair



void setup() {
  Serial.begin(9600);
  Serial.print("haiii!!!");
  setup_shock();
  
  configAP();
  shock(1,1,1);
}

void loop() {
  // put your main code here, to run repeatedly:
  loopmdns();
}

//random(128,23785)


