#include <Arduino.h>
class Motor{
  public:
    int pin_1;
    int pin_2;
    int pin_pwm;
    int pwmChannel;
    int freq = 5000;
    int resolution = 8;
    Motor(int pin_1 = 0,int pin_2 = 0,int pin_pwm = 0,int pwmChannel = 0){
      if(pin_1 && pin_2 && pin_pwm){
        this->pin_1 = pin_1;
        this->pin_2 = pin_2;
        this->pin_pwm = pin_pwm;
        this->pwmChannel = pwmChannel;
        pinMode(pin_1,OUTPUT);
        pinMode(pin_2,OUTPUT);
        pinMode(pin_pwm,OUTPUT);
        ledcSetup(pwmChannel,freq,resolution);
        ledcAttachPin(pin_pwm,pwmChannel);
        ledcAttachPin(pin_pwm,pwmChannel);
      }
    }
    Motor &setPwmchannel(int pwmChannel){
      this->pwmChannel = pwmChannel;
      return *this;
    }
    Motor &setPin1(int pin_1){
      this->pin_1 = pin_1;
      return *this;
    }
    Motor &setPin2(int pin_2){
      this->pin_2 = pin_2;
      return *this;
    }
    Motor &setPinPwm(int pin_pwm){
      this->pin_pwm = pin_pwm;
      return *this;
    }
    void setSpeed(int speed);
    void forward();
    void backward();
    void stop();
};

class Motors{
  private:
    int leftSpeed,rightSpeed;
    Motor left;
    Motor right;
  public:
    Motors(Motor &l,Motor &r){
      left.setPin1(l.pin_1).setPin2(l.pin_2).setPinPwm(l.pin_pwm).setPwmchannel(l.pwmChannel);
      right.setPin1(r.pin_1).setPin2(r.pin_2).setPinPwm(r.pin_pwm).setPwmchannel(r.pwmChannel);
    }
    void Forward();
    void Backward();
    void Stop();
    void Right();
    void Left();
    void Move(double turn,int normal_speed,int t);
};
