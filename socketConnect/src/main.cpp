#include <Arduino.h>
#include <WiFi.h>
#include <WiFiUdp.h>


const char* ssid = "drivera";
const char* password =  "fe63b4366c140";
const uint16_t port = 8090;
const char * host = "192.168.0.13";
int count=0;
float x,y,z,a,b,c;
unsigned long tiempo;
int frecuencia=60;
WiFiUDP Udp;


struct Data_to_be_sent {
  int16_t t;
  int16_t c;
  int16_t AcX;
  int16_t AcY;
  int16_t AcZ;
  int16_t GcX;
  int16_t GcY;
  int16_t GcZ;
} to_sent;

void setup() {
  
  Serial.begin(115200);

  WiFi.begin(ssid, password);

  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.println("...");
  }
 
  Serial.print("WiFi connected with IP: ");
  Serial.println(WiFi.localIP());
  tiempo=millis();
}

void dummy_data(){

  to_sent.AcX=random(20000);
  to_sent.AcY=random(20000);
  to_sent.AcZ=random(20000);
  to_sent.GcX=random(20000);
  to_sent.GcY=random(20000);
  to_sent.GcZ=-random(20000)  ;
}
void loop() {

  if(millis()>tiempo+(1000/frecuencia)){

    to_sent.c=count;
    tiempo+=1000/frecuencia;
    count = (count+1)%65535;
    to_sent.t=millis()%65535;
    dummy_data();
    Udp.beginPacket(host, port);    
    Udp.write((byte *) &to_sent,sizeof(Data_to_be_sent));
    Udp.endPacket();
    Serial.println("SEND"); 
  }
  else
  {
    delay(1);
  }
  
  

}