#include <Arduino.h>
class Motor{
  public:
    int pin_1;
    int pin_2;
    int pwmChannel_1;
    int pwmChannel_2;
    int freq = 5000;
    int resolution = 7;
    int speed = 0;
    Motor(int pin_1 = 0,int pin_2 = 0,int pwmChannel_1 = 0,int pwmChannel_2 = 0){
        this->pin_1 = pin_1;
        this->pin_2 = pin_2;
        this->pwmChannel_1 = pwmChannel_1;
        this->pwmChannel_2 = pwmChannel_2;
        pinMode(pin_1,OUTPUT);
        pinMode(pin_2,OUTPUT);
        ledcSetup(pwmChannel_1,freq,resolution);
        ledcAttachPin(pin_1,pwmChannel_1);
        ledcSetup(pwmChannel_2,freq,resolution);
        ledcAttachPin(pin_2,pwmChannel_2);
    }
    Motor &setPwmChannel_1(int pwmChannel_1){
      this->pwmChannel_1 = pwmChannel_1;
      return *this;
    }
    Motor &setPwmChannel_2(int pwmChannel_2){
      this->pwmChannel_2 = pwmChannel_2;
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
    void setSpeed(int speed){
      this->speed = speed;
    }
    void forward();
    void backward();
    void stop();
};

class Motors{
  private:
    double prevError = 0;
    double integral = 0;
    String info;
enum SPEEDS{
    MIN,
    NORMAL,
    MAX
};
    int leftSpeed,rightSpeed;
    Motor left;
    Motor right;
  public:
    Motors(Motor &l,Motor &r){
      left.setPin1(l.pin_1).setPin2(l.pin_2).setPwmChannel_1(l.pwmChannel_1).setPwmChannel_2(l.pwmChannel_2);
      right.setPin1(r.pin_1).setPin2(r.pin_2).setPwmChannel_1(r.pwmChannel_1).setPwmChannel_2(r.pwmChannel_2);
    }
    void Forward();
    void Backward();
    void Stop();
    void Right();
    void Left();
String Move(double curve,int speeds[],int levelLeftMotor, int levelRightMotor,double Kp,double Ki,double Kd);
};
