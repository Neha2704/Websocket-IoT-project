#include <dht.h>
int room;

void setup()
{
  Serial.begin(9600);
}

void loop()
{
  //Serial.println(analogRead(A0));
  room = analogRead(A0);
  int chk = DHT.read11(DHT11_PIN);
  Serial.print((int)DHT.temperature);
  Serial.print((int)DHT.humidity);
  Serial.println((int)room);
  delay(1000);
}
