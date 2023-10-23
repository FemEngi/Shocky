#include "network.h"
#include "shock.h"
const uint ServerPort = 80;
WiFiServer server(ServerPort);


int i=0;

// TCP server at port 80 will respond to HTTP requests
// WiFiServer server(80);

void configAP(void)
{  
    WiFiManager wm;
    bool res;
    // Connect to WiFi network
    res = wm.autoConnect("pishk1","password");
    Serial.println("");

    if(!res) {
    Serial.println("Failed to connect or hit timeout");
    // ESP.restart();
    } 
    else {
        //if you get here you have connected to the WiFi    
        Serial.println("connected...yeey :)");
    }

    if (!MDNS.begin("esp32")) {
        Serial.println("Error setting up MDNS responder!");
        while(1) {
            delay(1000);
        }
    }

    server.begin();
    MDNS.addService("http", "tcp", 80);
    Serial.print(WiFi.localIP());

    // // Set up mDNS responder:
    // // - first argument is the domain name, in this example
    // //   the fully-qualified domain name is "esp32.local"
    // // - second argument is the IP address to advertise
    // //   we send our IP address on the WiFi network
    // if (!MDNS.begin("esp32")) {
    //     Serial.println("Error setting up MDNS responder!");
    //     while(1) {
    //         delay(1000);
    //     }
    // }
    // Serial.println("mDNS responder started");

    // // Start TCP (HTTP) server
    // Serial.println("TCP server started");

    // // Add service to MDNS-SD
    // MDNS.addService("http", "tcp", 80);
}

void loopmdns(void)
{
    
    WiFiClient client = server.available();
    if (!client) {
        return;
    }

    while(client.connected() && !client.available()){
        delay(1);
    }
    Serial.println("haiii123");
    String req = client.readStringUntil('\r');

    int addr_start = req.indexOf(' ');
    int addr_end = req.indexOf(' ', addr_start + 1);
    if (addr_start == -1 || addr_end == -1) {
        Serial.print("Invalid request: ");
        Serial.println(req);
        return;
    }
    
    req = req.substring(addr_start + 1, addr_end);
    Serial.print("Request: ");
    Serial.println(req);
    int count=0;
    String stringarray[5];
    for(i=1; i<32; i++){ 
        if (req.charAt(i) == '/') {
            count++;
        } else {
            stringarray[count] += req.charAt(i);

        }
    }

    Serial.println(stringarray[0]);
    Serial.println(stringarray[1]);
    Serial.println(stringarray[2]);
    shock(stringarray[0].toInt(),stringarray[1].toFloat(),stringarray[2].toInt());
    
    client.print("HTTP/1.1 gay\r\n\r\n");
    client.stop();
    
}

