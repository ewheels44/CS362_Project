/*
 * Team Name: Rouge Leader
 * Group Members: Ethan Wheeler & Khizer Shareef
 * SP 22 - CS362
 * 
 * Project title: Sailboat performance measurement
 * 
 * Refrence: https://github.com/bogde/HX711
 */

#include <HX711.h>
#include <LiquidCrystal.h>

// initialize the library by associating any needed LCD interface pin
// with the arduino pin number it is connected to

// 
const int rs = 7, en = 6, d4 = 2, d5 = 3, d6 = 4, d7 = 5;

//load cell pins
const int sck = 8;
const int dt = 9;

HX711 scale;
float cali_factor = -232779;

LiquidCrystal lcd(rs, en, d4, d5, d6, d7);

void setup() {
  // set up the LCD's number of columns and rows:
  lcd.begin(16, 2);
  // Print a message to the LCD.
  lcd.setCursor(0,0);
  lcd.print("Main Sheet :");
  Serial.begin(9600);

  // set the scale to proper pins
  scale.begin( dt, sck );
  scale.tare(); // setup the guage when nothing is loaded on it

//  long zero_factor = scale.read_average();
//  Serial.print("zero factor: ");
//  Serial.println(zero_factor);
}

void loop() {
  // set the scale to proper calibration
  scale.set_scale ( cali_factor );
  
  // get the weight being read by the gauge
  float weight = scale.get_units();
  Serial.println(weight);
  // print on the lcd
  lcd.setCursor ( 0,1 );
  // this condition is trivial as it doesn't
  // allow for "-0.0" case to be printed on lcd
  if ( weight < 0 && weight > -0.01 ) {
    weight = 0;
  }
  // print the readings on the lcd
  lcd.print ( weight, 2 );
  // this condition is trivial again as its 
  // purpose is to print "KG" properly on the lcd
  if ( weight < 0 ) {
    lcd.setCursor ( 5, 1 );
    lcd.print ( " KG " );
  }
  else{
    lcd.setCursor ( 4, 1 );
    lcd.print ( " KG " );
  }
  
}
