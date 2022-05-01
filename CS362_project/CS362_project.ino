#include "HX711.h"

//Pins 
#define forestay_DOUT_PIN 3       //Data pin from forestay 
#define forestay_SCK_PIN  2        //Clock pin from forestay

#define backstay_DOUT_PIN 5       //Data pin from backstay
#define backstay_SCK_PIN  4       //Clock pin from backstay 

#define calibration_factor_forestay -445806 // works for 5kg load cell
#define calibration_factor_backstay -132173 // works for 5kg load cell

HX711 forestay;
HX711 backstay;

long int values = 0; 

void setup() {
  Serial.begin(9600); 
  /* Serial.println("Sailing Preformance Limited"); */
  /* Serial.println("Welcome"); */
  /* Serial.println("Starting up..."); */
  forestay.begin(forestay_DOUT_PIN, forestay_SCK_PIN);
  backstay.begin(backstay_DOUT_PIN, backstay_SCK_PIN);

  /* forestay.tare();                // sets scale to 0 */
  backstay.tare();                // sets scale to 0

  /* long zero_factor = forestay.read_average(); */
  /* Serial.print("zero factor forestay: "); */
  /* Serial.println(zero_factor); */

  /* long zero_factor_back = backstay.read_average(); */
  /* Serial.print("zero factor backstay: "); */
  /* Serial.println(zero_factor_back); */
}
 
void loop() {


 if (Serial.available()) { 
    String cmd = Serial.readString();
    cmd.trim();
    Serial.print(cmd);

    if (cmd == "read_tension"){
      /* Serial.print("here in read"); */
      forestay.set_scale(calibration_factor_forestay);
      backstay.set_scale(calibration_factor_backstay);
      read_tension();
    }
    else{
      Serial.print("Bad input");
    }
 }

}


//
// reading both the backstay and the forestay
//
void read_tension(){

    /* Serial.print("forestay load: "); */
    /* Serial.print(forestay.get_units(), 1); */
    /* Serial.print(" lbs"); */
    /* Serial.println(); */
    /* delay(500); */

    /* Serial.print("backstay load: "); */
    /* Serial.print(backstay.get_units(), 1); */
    /* Serial.print(" lbs"); */
    /* Serial.println(); */
    /* delay(500); */

  while (true) {
    Serial.print(forestay.get_units(), 1);
    Serial.print(",");
    Serial.print(backstay.get_units(), 1);
    Serial.print("\n");
    delay(500);

  }

}
