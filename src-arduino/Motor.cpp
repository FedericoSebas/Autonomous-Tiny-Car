#include <Arduino.h>
#include "Motor.h"
void Motor::forward(){
  ledcWrite(pwmChannel_1,speed);
  ledcWrite(pwmChannel_2,0);
}
void Motor::backward(){
  ledcWrite(pwmChannel_1,0);
  ledcWrite(pwmChannel_2,speed);
}

void Motor::stop(){
  ledcWrite(pwmChannel_1,0);
  ledcWrite(pwmChannel_2,0);
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
