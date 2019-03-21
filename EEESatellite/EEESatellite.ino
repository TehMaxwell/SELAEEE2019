/*
 * This is the firmware for the EEE Satellite Dish arcade game for the 2019 SELA exhibition at GUTS. This game lets users control
 * the positioning of a Satellite Dish and align it with a Satellite dish on the moon inside the game cabinet to produce the best
 * signal strength. This game is partnered with the EEE Sine Waves game that has users match a set of AM Double Sideband Signals.
 * 
 * AUTHOR: Sam Maxwell
 * DATE: 21/03/2019
 */

 //LIBRARIES
 #include <Servo.h>
 #include <FastLED.h>

 //DEFINITIONS
 #define LED_PIN 4
 #define X_AXIS_SERVO 5
 #define Y_AXIS_SERVO 6
 #define START 7
 #define RESET 8
 #define JOYX+ 9
 #define JOYX- 10
 #define JOYY+ 11
 #define JOYY- 12

 //FUNCTIONS
 //SWITCH FUNCTIONS
 //Function used to read the state of one of the game switches
 bool readSwitch(pinNumber){
  bool switchState = digitalRead(pinNumber);
  return switchState;
 }

 //Function used to read the state of the start button
 bool readStartButton(){
  return readSwitch(START);
 }

 //Function used to read the state of the reset button
 bool readResetButton(){
  return readResetButton(RESET);
 }

 //Function used to read the state of the Joystick, returns value from 1 to 4 (1 = UP, 2 = RIGHT, 3 = DOWN, 4 = LEFT)
 int readJoystick(){
  int joyVal = 0;

  //If the Switch is Up
  if (readSwitch(JOYY+)){
    joyVal = 1;
  }

  //If the Switch is Down
  else if (readSwitch(JOYY-)){
    joyVal = 3;
  }

  //If the Switch is Left
  else if (readSwitch(JOYX+)){
    joyVal = 4;
  }

  //If the Switch is Right
  else if (readSwitch(JOYX-)){
    joyVal = 2;
  }

  return joyVal;
 }

 //MAIN CODE
 void setup(){
  
 }

 void loop(){
  
 }
