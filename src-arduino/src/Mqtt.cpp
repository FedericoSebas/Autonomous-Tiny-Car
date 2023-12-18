#include "Mqtt.h"

subscribeCallback Mqtt::savedCallback = nullptr;

// Default configurai
void Mqtt::setCallbackSubscribe(subscribeCallback callback)
{
  savedCallback = callback;
}
void Mqtt::callCallbackSubscribe()
{
  if (savedCallback != nullptr)
  {
    savedCallback();
  }
}

void Mqtt::reconnect()
{
  while (!this->connected())
  {
    Serial.print("Attempting MQTT connection...");
    rand = random(1000);
    sprintf(clientId, "clientId-%ld", rand);
    if (this->connect(clientId, mqttUser, mqttPassword))
    {
      Serial.print(clientId);
      Serial.println(" connected");
    
      callCallbackSubscribe();
    }
    else
    {
      Serial.print("failed, rc=");
      Serial.print(this->state());
      Serial.println(" try again in 5 seconds");
      delay(5000);
      continue;
    }
  }
}

