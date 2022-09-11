#include <WiFi.h>  
#include <Arduino.h>
#include <PubSubClient.h>
#include "Motor.h"
enum IncommingMessageMotors{
  DEG,
  SPD
};
enum ValuesMotors{
  LEFT,
  RIGHT
};
String incommingState;
double turn = 0;
String joyLeft[2] = {"                ","                     "};
String joyRight[2] = {"                ","                     "};
int speed[2];
const int normalize = 255/100;
int deg[2];
enum State{
  RC,
  AUTONOMY
};
int state = RC;

const char* topic_state = "motor/state";
const char*  topic_motor_turn = "motor/autonomy/turn";
const char*  topic_motor_left = "motor/rc/left";
const char*  topic_motor_right = "motor/rc/right";

const char* ssid = "wifiNade";
const char* password = "password";
const char* mqtt_server = "ip";
const int mqttPort = 1883;

WiFiClient espClient;
PubSubClient client(espClient);

Motor leftMotor(26,27,12,0);
Motor rightMotor(33,25,14,1);


Motors twoMotors(leftMotor,rightMotor);


int  connection = 0;

//-----------------------------------------------------------

void callback(char* topic, byte* payload, unsigned int length) {
  String incommingMessage = "";
  String Topic = String(topic);
  for (int i = 0; i < length; i++) incommingMessage+=(char)payload[i];
  
  Serial.println("Message arrived ["+Topic+"]"+incommingMessage);
  if(Topic == topic_motor_turn){
    turn = incommingMessage.toDouble();
  }
  if(Topic == topic_motor_left){
    joyLeft[DEG] = incommingMessage.substring(0,incommingMessage.indexOf(" "));
    joyLeft[SPD] = incommingMessage.substring(incommingMessage.indexOf(" "),incommingMessage.length());
    joyLeft[DEG].trim();
    joyLeft[SPD].trim();
    deg[LEFT] = joyLeft[DEG].toInt(); 
    speed[LEFT] = int(round(joyLeft[SPD].toInt()*normalize));
  }
  if(Topic == topic_motor_right){
    joyRight[DEG] = incommingMessage.substring(0,incommingMessage.indexOf(" "));
    joyRight[SPD] = incommingMessage.substring(incommingMessage.indexOf(" "),incommingMessage.length());
    joyRight[DEG].trim();
    joyRight[SPD].trim();
    deg[RIGHT] = joyRight[DEG].toInt(); 
    speed[RIGHT] = int(round(joyRight[SPD].toInt()*normalize));
  }
  if(Topic == topic_state){
    incommingState = incommingMessage;
  }
}
  
void setup() {
  Serial.begin(115200);
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED and connection <50)
  {
    ++connection;
    delay(500);
    Serial.print(".");
  }
  if (connection < 50)
  {
    Serial.println("");
    Serial.println("WiFi conectado");
    Serial.println(WiFi.localIP());
  }
  else
  {
    Serial.println("");
    Serial.println("Error de conexion");
  }
  client.setServer(mqtt_server, mqttPort);
  client.setCallback(callback);
}


//-----------------------------------------------------------

void reconnect(){
  while (!client.connected())
  {
    Serial.print("Connecting MQTT...");

    if (client.connect("CERTERO-MOTORS"))
    {
      Serial.println("Connected");
      client.subscribe(topic_motor_turn);
      client.subscribe(topic_motor_left);
      client.subscribe(topic_motor_right);
      client.subscribe(topic_state);
    }

    else
    {
      Serial.print("Connection error");
      Serial.print(client.state());
      delay(2000);
    }
  }
}

void loop(){
  if(!client.connected()){
    reconnect();
  }
  client.loop();
  if(incommingState == "rc" || incommingState == "RC"){
    state = RC;
  }
  if(incommingState == "autonomy" || incommingState == "AUTONOMY"){
    state = AUTONOMY;
  }
  if(state == RC){
    rightMotor.setSpeed(speed[RIGHT]);
    leftMotor.setSpeed(speed[LEFT]);
    if (deg[LEFT] >= 0 && deg[LEFT] <= 180 && deg[RIGHT] >= 0 && deg[RIGHT] <= 180)
    {
      twoMotors.Forward();
    }

    if (deg[LEFT] > 180 && deg[LEFT] <= 360 && deg[RIGHT] > 180 && deg[RIGHT] <= 360)
    {
      twoMotors.Backward();
    }
  }
  if(state == AUTONOMY)twoMotors.Move(turn,205,0);
}

