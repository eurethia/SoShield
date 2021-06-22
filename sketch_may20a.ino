/***************************************************
  Microwave sensor
  <http://www.dfrobot.com.cn/goods-1231.html>

 ***************************************************
  This example reads temperature and humidity from SHT1x Humidity and Temperature Sensor.

  Created 2015-7-30
  By Loan <Loan.he@dfrobot.com>

  GNU Lesser General Public License.
  See <http://www.gnu.org/licenses/> for details.
  All above must be included in any redistribution
 ****************************************************/

/***********Notice and Trouble shooting***************
  1.Connection and Diagram can be found here
  <http://wiki.dfrobot.com.cn/index.php?title=%28SKU:SEN0192%29_Microwave_sensor%E5%BE%AE%E6%B3%A2%E4%BC%A0%E6%84%9F%E5%99%A8%E6%A8%A1%E5%9D%97>
  2.This code is tested on Arduino Uno, Leonardo, Mega boards.
  3.arduino Timer library is created by jonoxer.
  See <http://www.dfrobot.com.cn/images/upload/File/SEN0192/20160112134309yy5nus.zip arduino Timer library> for details.
 ****************************************************/
#include <MsTimer2.h>           //Timer interrupt function
#include <Wire.h>
int pbIn = 0;                   // Define the interrupt PIN is 0, that is, digital pins 2
int ledOut = 13;
int count = 0;
volatile int state = LOW;       //Define ledOut, default is off
static char flag = 'N'; 
void setup()
{
  Serial.begin(9600);
   Wire.begin(8);                /* join i2c bus with address 8 */
   Wire.onReceive(receiveEvent); /* register receive event */
   Wire.onRequest(requestEvent); /* register request event */

  pinMode(ledOut, OUTPUT);
  attachInterrupt(pbIn, stateChange, FALLING); // Sets the interrupt function, falling edge triggered interrupts.
  MsTimer2::set(1000, process); // Set the timer interrupt time 1000ms
  MsTimer2::start();//Timer interrupt start

}

void loop()
{
  //Serial.println(count); // Printing times of 1000ms suspension
  delay(1);
  if (state == HIGH) //When moving objects are detected later, 2s shut down automatically after the ledout light is convenient.
  {
    delay(2000);
    state = LOW;
    digitalWrite(ledOut, state);    //Turn off led
  }

}


void stateChange()  //Interrupt function
{
  count++;

}

void process()   //Timer handler
{
  if (count > 5) //1000ms interrupt number greater than 1 is considered detected a moving object (this value can be adjusted according to the actual situation, equivalent to adjust the detection threshold of the speed of a moving object)
  {
    state = HIGH;
    digitalWrite(ledOut, state);    //Lighting led
    Serial.print('Y');
    flag = 'Y';
    count = 0; //Count zero

  }
  else{
    count = 0; //In 1000ms, interrupts does not reach set threshold value is considered not detect moving objects, interrupt the count number is cleared to zero.
    Serial.print('N');
    flag = 'N';/*send string on request */
  }
}
void receiveEvent(int howMany) {
 while (0 <Wire.available()) {
    char c = Wire.read();      /* receive byte as a character */
    Serial.print(c);           /* print the character */
  }
 Serial.println();             /* to newline */
}
// function that executes whenever data is requested from master
void requestEvent() {
 Wire.write(flag);  /*send string on request */
}
