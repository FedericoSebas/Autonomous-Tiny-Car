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

void Motors::Left(){
  left.backward();
  right.forward();
}
void Motors::Right(){
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
void Motors::Move(double turn,int normal_speed){
  Motors twoMotors(left,right);
  factor = maxSpeed - normal_speed;
  turn=int(round(turn*factor));
  minSpeed = normal_speed - factor;
  leftSpeed = normal_speed - turn;
  rightSpeed = normal_speed + turn;
  if (leftSpeed > maxSpeed)leftSpeed = maxSpeed; 
  else if(leftSpeed < minSpeed)leftSpeed = minSpeed;
  if (rightSpeed > maxSpeed)rightSpeed = maxSpeed;
  else if(rightSpeed < minSpeed)rightSpeed = minSpeed;
  left.setSpeed(leftSpeed);
  right.setSpeed(rightSpeed);
  if(leftSpeed > normal_speed)left.backward();
  if(leftSpeed < normal_speed)left.forward();
  if(rightSpeed > normal_speed )right.backward();
  if(rightSpeed < normal_speed )right.forward();
  if(leftSpeed == normal_speed && rightSpeed == normal_speed)twoMotors.Forward();
}

