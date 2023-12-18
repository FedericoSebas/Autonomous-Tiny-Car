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
String Motors::Move(double curve, int speeds[],int levelLeftMotor, int levelRightMotor, double Kp, double Ki,double Kd){
  // Calculate the turning value
  double offSet = 0; // Offset value
  double error = curve-offSet; // Error value
  double turn = 0; // Turning value
  // double prevError = 0; // Last error value
  // double integral = 0; // Integral value
  double derivative = 0;
  // double Kp = (speeds[NORMAL] - speeds[MIN]) / (0 + 1); // Proportional gain
 integral += error; // Add the error to the integral

  if(Ki < 0){
    Ki = -Ki;
    if((prevError > 0 && error < 0) || (prevError < 0 && error > 0) || error == 0){
    integral = 0; // Reset the integral if the error changes sign or is zero
  }
  }

  derivative = error - prevError;

  turn = round((Kp * error) + (Ki * integral )+ (Kd * derivative)); // Calculate the turning value
  

  // Calculate the left and right motor speeds
  leftSpeed = speeds[NORMAL] + turn - levelLeftMotor;
  rightSpeed = speeds[NORMAL] - turn - levelRightMotor;

  // Ensure speeds are within valid range
  leftSpeed = constrain(leftSpeed, speeds[MIN], speeds[MAX]);
  rightSpeed = constrain(rightSpeed, speeds[MIN], speeds[MAX]);

  // Set the motor speeds
  left.setSpeed(leftSpeed);
  right.setSpeed(rightSpeed);

  // Move the motors
  left.forward();
  right.forward();

  delayMicroseconds(1);

  // Return curve and turn values and then time
  info =  ", " + String(curve) + ", " + String(turn);

  return info;
}
