#include <Servo.h>

Servo servoRight;
Servo servoLeft;

int SENSOR_R = 7;
int SENSOR_L = 8;
void setup() {
  // put your setup code here, to run once:
  pinMode(SENSOR_R, INPUT_PULLUP);
  pinMode(SENSOR_L, INPUT_PULLUP);
  Serial.begin(9600);
  servoLeft.attach(12);
  servoRight.attach(11);
  servoLeft.writeMicroseconds(1500);
  servoRight.writeMicroseconds(1500);
}
  void forward() {
  servoLeft.writeMicroseconds(1700);
  servoRight.writeMicroseconds(1300);
  }
  void backward() {
    servoLeft.writeMicroseconds(1300);
    servoRight.writeMicroseconds(1700);
  }
  void left() {
    servoLeft.writeMicroseconds(1300);
    servoRight.writeMicroseconds(1300);
  }
  void right() {
    servoLeft.writeMicroseconds(1700);
    servoRight.writeMicroseconds(1700);
  }
void loop() {
  // put your main code here, to run repeatedly:
  forward();
  if(digitalRead(SENSOR_R) == 0) {
    backward();
    delay(800);
    left();
    delay(500);
    //Serial.print("right touching");
  }
  if(digitalRead(SENSOR_L) == 0) {
    backward();
    delay(800);
    right();
    delay(500);
    //Serial.print("left touching");
  }
  if(digitalRead(SENSOR_R) == 0 && digitalRead(SENSOR_L == 0)) {
    backward();
    delay(1000);
    right();
    delay(500);
    //Serial.print("both touching");
  }
  else {
    forward();
    //Serial.print("not touching");
  }
}      

