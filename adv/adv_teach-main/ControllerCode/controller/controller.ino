
#include <Servo.h>

Servo myservo;  // create servo object to control a servo
// twelve servo objects can be created on most boards

int pos = 90;    // variable to store the servo position

void setup() {
  
  Serial.begin(115200);
  Serial.setTimeout(1);
  myservo.attach(9);  // attaches the servo on pin 9 to the servo object
  myservo.write(pos); 
  }

void loop() {
 if (Serial.available())
 {
  int error = Serial.readString().toInt();
  myservo.write(90 - (error/50));
  delay(15);
  }
}
