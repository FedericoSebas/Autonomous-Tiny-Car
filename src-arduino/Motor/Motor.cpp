#include <Arduino.h>
#include "Motor.h"
void Motor::setSpeed(int speed){
  ledcWrite(pwmChannel,speed);
}

void Motor::forward(){
  digitalWrite(pin_1,HIGH);
  digitalWrite(pin_2,LOW);
}
void Motor::backward(){
  digitalWrite(pin_1,LOW);
  digitalWrite(pin_2,HIGH);
}

void Motor::stop(){
  digitalWrite(pin_1,LOW);
  digitalWrite(pin_2,LOW);
}

void Motors::Right(){
  left.backward();
  right.forward();
}
void Motors::Left(){
  left.forward();
  right.backward();
}
void Motors::Forward(){
  left.forward();
  right.forward();
}
void Motors::Backward(){
  left.backward();
  right.backward();
}
void Motors::Stop(){
  left.stop();
  right.stop();
}
void Motors::Move(double turn,int normal_speed,int t){
  turn=int(round(turn*50));
  leftSpeed = normal_speed - turn;
  rightSpeed = normal_speed + turn;
  if (leftSpeed > 255)leftSpeed = 255; 
  else if(leftSpeed < 155)leftSpeed = 155;
  if (rightSpeed > 255)rightSpeed = 255;
  else if(rightSpeed < 155)rightSpeed = 155;
  left.setSpeed(leftSpeed);
  right.setSpeed(rightSpeed);
  left.forward();
  right.forward();
  /* if(leftSpeed > normal_speed)left.forward();
  if(leftSpeed < normal_speed)left.backward();
  if(rightSpeed > normal_speed )right.forward();
  if(rightSpeed < normal_speed )right.backward(); */
  delay(t);
}

