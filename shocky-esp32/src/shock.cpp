#include "shock.h"
#include <ZapMe.h>
// Preferences preferences;


//setup collar
const uint16_t tx_pin = 13;
CH8803 collar = CH8803(tx_pin, 0);



void setup_shock() {
    // preferences.begin("storage", true); 
    // const uint16_t transmitter_id = preferences.getUInt("keya", 0);
    const uint16_t transmitter_id = 0x1234;
  
    // preferences.end();
    // put your setup code here, to run once:
    
    collar.setId(13, 37);
}

void shock(int mode_raw,float duration_raw, uint8_t power_raw) {

  
  // Mode
  switch (mode_raw)
  {
    case 1:
      collar.sendShock(power_raw, duration_raw);
      break;

    case 2:
      collar.sendVibration(power_raw, duration_raw);
      break;

    case 3:
      collar.sendAudio(power_raw, duration_raw);
      break;

    default:
      Serial.println("Unexpected mode");
      return;
  }
}

// void pairing_button1() {
//     preferences.begin("storage", false); 
//     preferences.putUInt("keya", uint16_t(random(128,23785)));
//     preferences.end();
// }