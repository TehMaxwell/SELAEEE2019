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

 //OBJECTS
 Servo xAxisServo;
 Servo yAxisServo;
 
 //DEFINITIONS
 //LED Definitions
 #define NUM_LEDS 110
 #define LED_PIN 2
 #define LED_TYPE    WS2811
 #define COLOR_ORDER GRB
 #define MAX_BRIGHTNESS  100

 //Servo Definitions
 #define X_AXIS_SERVO 5
 #define Y_AXIS_SERVO 6
 #define X_AXIS_MIN 78
 #define X_AXIS_MAX 105
 #define Y_AXIS_MIN 120
 #define Y_AXIS_MAX 150

 //Button Definitions
 #define START 11
 #define RESET 12
 #define JOYXPLUS 7
 #define JOYXMINUS 10
 #define JOYYPLUS 9
 #define JOYYMINUS 8

 //Game Definitions
 #define TARGET_X_VAL 80
 #define TARGET_Y_VAL 141

 //VARIABLES
 //Servo Variables
 int xAxisServoPosition = int((X_AXIS_MAX - X_AXIS_MIN) / 2);
 int yAxisServoPosition = int((Y_AXIS_MAX - Y_AXIS_MIN) / 2);

 //LED Variables
 CRGB ledArray[NUM_LEDS];
 CRGBPalette16 currentPalette;
 TBlendType currentBlending;

 //Game Variables
 bool gameFinished = false;
 bool gameReset = false;

 //FUNCTIONS
 //SWITCH FUNCTIONS
 //Function used to read the state of one of the game switches
 bool readSwitch(int pinNumber){
  bool switchState = digitalRead(pinNumber);
  return switchState;
 }

 //Function used to read the state of the start button
 bool readStartButton(){
  return !readSwitch(START);
 }

 //Function used to read the state of the reset button
 bool readResetButton(){
  return !readSwitch(RESET);
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

 //Function to decode the Joystick value to a Servo Position Increase or Decrease
 void decodeJoystickVal(int joyVal){
  switch(joyVal){
    case 3:
      if(yAxisServoPosition < Y_AXIS_MAX){
        yAxisServoPosition += 1;
      }
      break;
    case 2:
      if(xAxisServoPosition > X_AXIS_MIN){
        xAxisServoPosition -= 1; 
      }
      break;
    case 1:
      if(yAxisServoPosition > Y_AXIS_MIN){
        yAxisServoPosition -= 1;
      }
      break;
    case 4:
      if(xAxisServoPosition < X_AXIS_MAX){
        xAxisServoPosition += 1;
      }
      break;
    default:
      break;
  }
 }

 //LED CONTROL FUNCTIONS
 //Function used to fill LEDs a Specific Colour
 void fillLEDsFromColour(CRGB::HTMLColorCode ledColour){
  for(int ledIndex = 0; ledIndex < NUM_LEDS; ledIndex++){
    ledArray[ledIndex] = ledColour;
  }

  FastLED.show();
 }
 
 //Function used to fill the current LED Colours from the currently selected Colour Pallete
 void fillLEDsFromPaletteColors(int colorIndex){
    for(int ledIndex = 0; ledIndex < NUM_LEDS; ledIndex++) {
        ledArray[ledIndex] = ColorFromPalette(currentPalette, colorIndex, MAX_BRIGHTNESS, currentBlending);
        colorIndex += 3;
    }
 }

 //Function used to fill the current LEDs Blue
 void fillLEDsBlue(){
    fillLEDsFromColour(CRGB::Blue);
 }

 //Function used to fill the current LEDs Green
 void fillLEDsGreen(){
    fillLEDsFromColour(CRGB::Green);
 }

 //GAME FUNCTIONS
 bool satelliteAlligned(){
  bool satelliteAllignedCorrectly = false;
  
  if(xAxisServoPosition == TARGET_X_VAL && yAxisServoPosition == TARGET_Y_VAL){
    satelliteAllignedCorrectly = true;
  }
  
  return satelliteAllignedCorrectly;
 }
 
 //MAIN CODE
 void setup(){
  //Power Up Safety Delay
  delay(2000);
  
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

  //Setting up the LED String
  FastLED.addLeds<LED_TYPE, LED_PIN, COLOR_ORDER>(ledArray, NUM_LEDS).setCorrection( TypicalLEDStrip );
  FastLED.setBrightness(MAX_BRIGHTNESS);

  //Setting up the Servo Controls
  xAxisServo.attach(X_AXIS_SERVO);
  yAxisServo.attach(Y_AXIS_SERVO);

  //Centering the Servos
  xAxisServo.write(int((X_AXIS_MAX - X_AXIS_MIN) / 2 + X_AXIS_MIN));
  yAxisServo.write(int((Y_AXIS_MAX - Y_AXIS_MIN) / 2 + Y_AXIS_MIN));

  delay(1000);
 }

 void loop(){
  //ATTRACTION MODE
  fillLEDsFromColour(CRGB::Red);
  
  //Waiting until User wants to start game
  while(readStartButton() == false){
  }

  //GAME START
  //Resetting the Game State
  gameFinished = false;
  gameReset = false;
  
  //Recentering the Game Servos
  xAxisServoPosition = int((X_AXIS_MAX - X_AXIS_MIN) / 2 + X_AXIS_MIN);
  yAxisServoPosition = int((Y_AXIS_MAX - Y_AXIS_MIN) / 2 + Y_AXIS_MIN);
  xAxisServo.write(xAxisServoPosition);
  yAxisServo.write(yAxisServoPosition);

  //Setting the LEDs to bright Blue
  fillLEDsBlue();

  //Beginning the main game loop
  while(gameFinished == false && gameReset == false){
    //Reading the value of the Joystick
    int joyVal = readJoystick();

    //Decoding the value of the Joystick into a change in Servo Value
    decodeJoystickVal(joyVal);
    delay(100);

    //Setting the new position of the Servos
    xAxisServo.write(xAxisServoPosition);
    yAxisServo.write(yAxisServoPosition);

    //Checking if the current servo position is correct
    gameFinished = satelliteAlligned();

    //Checking if the game needs to be Reset
    if(readResetButton()){
      gameReset = true;
    }

    //Printing the current position
    Serial.print("X Axis Position: ");
    Serial.println(xAxisServoPosition);
    Serial.print("Y Axis Position: ");
    Serial.println(yAxisServoPosition);
  }

  //Showing the user has won, if they have
  if(gameFinished){
    fillLEDsGreen();
    delay(3000);
  }
 }
