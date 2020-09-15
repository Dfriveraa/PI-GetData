#include <Arduino.h>
#include <WiFi.h>


const char* ssid = "drivera";
const char* password =  "fe63b4366c140";
const uint16_t port = 8090;
const char * host = "192.168.0.16";
int count=0;
float x,y,z,a,b,c;
unsigned long tiempo;
int frecuencia=40;
struct Data_to_be_sent {
  int16_t t;
  int16_t c;
  int16_t AcX;
  int16_t AcY;
  int16_t AcZ;
  int16_t GcX;
  int16_t GcY;
  int16_t GcZ;
} hola;

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

void loop() {

  if(millis()>tiempo+(1000/frecuencia)){
    tiempo+=1000/frecuencia;
    hola.t=millis();
    hola.c=count;
    hola.AcX=-2;
    hola.AcY=3;
    hola.AcZ=4;
    hola.GcX=5;
    hola.GcY=6;
    hola.GcZ=7;
    WiFiClient client;

    if (!client.connect(host, port)) {
        Serial.println("Connection to host failed");
        delay(500);
        return;
    }

    client.write((byte *) &hola,sizeof(Data_to_be_sent));
    count=count+1;
    Serial.println("SEND"); 
    client.stop();
  }
  else
  {
    delay(1);
  }
  
  

}