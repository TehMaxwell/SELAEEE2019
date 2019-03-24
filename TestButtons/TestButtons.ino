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
 //LED Definitions
 #define LED_PIN 2

 //Servo Definitions
 #define X_AXIS_SERVO 5
 #define Y_AXIS_SERVO 6

 //Button Definitions
 #define START 11
 #define RESET 12
 #define JOYXPLUS 7
 #define JOYXMINUS 10
 #define JOYYPLUS 9
 #define JOYYMINUS 8

 //FUNCTIONS
 //SWITCH FUNCTIONS
 //Function used to read the state of one of the game switches
 bool readSwitch(int pinNumber){
  bool switchState = digitalRead(pinNumber);
  return switchState;
 }

 //Function used to read the state of the start button
 bool readStartButton(){
  return readSwitch(START);
 }

 //Function used to read the state of the reset button
 bool readResetButton(){
  return readSwitch(RESET);
 }

 //Function used to read the state of the Joystick, returns value from 1 to 4 (1 = UP, 2 = RIGHT, 3 = DOWN, 4 = LEFT)
 int readJoystick(){
  int joyVal = 0;

  //If the Switch is Up
  if (!readSwitch(JOYYPLUS)){
    joyVal = 1;
  }

  //If the Switch is Down
  if (!readSwitch(JOYYMINUS)){
    joyVal = 3;
  }

  //If the Switch is Left
  if (!readSwitch(JOYXPLUS)){
    joyVal = 4;
  }

  //If the Switch is Right
  if (!readSwitch(JOYXMINUS)){
    joyVal = 2;
  }

  return joyVal;
 }

 //SERVO CONTROL FUNCTIONS
 
 //MAIN CODE
 void setup(){
  //Setting up digital pin settings
  pinMode(START, INPUT);
  pinMode(RESET, INPUT);
  pinMode(JOYXPLUS, INPUT);
  pinMode(JOYXMINUS, INPUT);
  pinMode(JOYYPLUS, INPUT);
  pinMode(JOYYMINUS, INPUT);

  //Setting up the Serial Monitor
  Serial.begin(9600);
  Serial.println("Program Starting");
 }

 void loop(){
  Serial.print("Start Button: ");
  Serial.println(readStartButton());
  Serial.print("Reset Button: ");
  Serial.println(readResetButton());
  Serial.print("Joystick: ");
  Serial.println(readJoystick());
 }
