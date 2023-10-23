#ifndef network_h_
#define network_h_

#include <FS.h>
#include "LITTLEFS.h"
#include <WiFi.h>
#include <ESPmDNS.h>
#include <WiFiClient.h>
#include <WiFiManager.h>

void configAP();
void loopmdns(void);
#endif