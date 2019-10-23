  
/* Mia-1 Open Source Humanoid Robot */

/*
Mia-1 the advanced open source humanoid robot.
author: Ashraf Minhaj
mail  : ashraf_minhaj@yahoo.com
blog  : ashrafminhajfb.blogspot.com
        http://youtube.com/fusebatti
*/

#include <Servo.h>

Servo servo1;  // create servo object to control a servo
Servo servo2;
Servo servo3;
Servo servo4;

Servo left1;
Servo left2;
Servo left3;
Servo left4;

Servo komor;    //waist servo
Servo rFinger;
Servo lFinger;

Servo headPan;
Servo headTilt;

int laser = 13; //laser on pin13

int i = 0;

int pos = 0;    // variable to store the servo position

byte val;

//_________________________________________________________________________________________________
//********* HI ***************
int Hi()
{
 //make it up (servo2)
  for (pos = 0; pos <= 90; pos += 1) 
  {
    servo2.write(pos);             
    delay(5);                       
  }
  
//rotate joint (servo3)
servo3.write(170);
delay(10);


   //hi up
    for (pos = 90; pos >= 30; pos -= 1) 
    { 
    servo4.write(pos);   
    delay(15); 
    }

  //hi down
   for (pos = 30; pos <= 50; pos += 1) 
   { 
    servo4.write(pos);  
    delay(15);  
  }

  //hi up
    for (pos = 50; pos >= 30; pos -= 1) 
    { 
    servo4.write(pos);   
    delay(15);  
  }

  for (pos = 30; pos <= 90; pos += 1) 
   {
    servo4.write(pos);  
    delay(15);           
  }

  for (pos = 90; pos >= 0; pos -= 1) 
  {
    servo2.write(pos);       
    delay(15);  
}
}
//___________________________________________________________________________________________________

void rightStandBy()
{
    // back to default joint position
//************* Right Hand ********************
 servo1.write(55);
  
  /*keep hand down (servo2)
  for (pos = 90; pos >= 0; pos -= 1) 
  {
    servo2.write(pos);              // tell servo to go to position in variable '/pos'
    delay(15);                       // waits 15ms for the servo to reach the position
  } */

  servo2.write(0);

  servo3.write(90);
 
  //default servo4
  servo4.write(90);
/*
  for (pos = 30; pos <= 90; pos += 1) 
  {
    servo4.write(pos);              // tell servo to go to position in variable '/pos'
    delay(20);                       // waits 15ms for the servo to reach the position
  }
*/

  for(pos = 150; pos>=0; pos -= 1)
  {
    rFinger.write(0);
  }
  digitalWrite(laser, LOW);

}

//__________________________________________________________________________________________________
void leftStandBy()
{
  //************** Left Hand ******************
  
  left2.write(0);
  left1.write(120);
/*
  //keep hand down (left1)
  for (pos = 0; pos <= 120; pos += 1) 
  {
    left1.write(pos);              // tell servo to go to position in variable '/pos'
    delay(15);                       // waits 15ms for the servo to reach the position
  }
*/

  left3.write(120); //120
  delay(600);

  left4.write(100);
  delay(600);
  
  clawOpen();

}

//__________________________________________________________________________________________________________
void show_off()
{

  //Now only left hand
// left2
  for(i = 10; i <= 100; i++)
  {
    left2.write(i);
    delay(15);
  }
 
  delay(1000);
  
  //make it down slowly(left2)
    for (pos = 100; pos >= 0; pos -= 1) 
  {
    left2.write(pos);          
    delay(70);          
  }
  
  //servo3
  for(i = 120; i <= 0; i--)
  {
    left3.write(i);
    delay(10);
  }

  for(i = 10; i >= 120; i++)
  {
    left3.write(i);
    delay(10);
  }

  delay(100);

 for (pos = 110; pos <= 170; pos += 1) 
  { // goes from 0 degrees to 180 degrees
    // in steps of 1 degree
    left4.write(pos);      
    delay(15);  
  }
  delay(100);

//Claw
  clawClose();
  delay(100);
  clawOpen();
  
    
  for(pos = 170; pos <= 100; i-= 1)
  {
    left4.write(pos);
    delay(100);
  }

}

//___________________________________________________________________________________________________


//____________________________________________________________________________________________________


void handShake()
{

  for (pos = 55; pos <= 80; pos += 1) 
  { 
    servo1.write(pos);  
    delay(15);         
  }

  for(pos = 90; pos >= 45; pos -= 1)
      {
        servo4.write(pos);
        delay(15);
      }

    headTilt.write(160);
    delay(3000);

    headTilt.write(140);

    for (pos = 45; pos <= 90; pos += 1) 
   {
    servo4.write(pos);            
    delay(15);           
   }
   for (pos = 80; pos >= 55; pos -= 1)
   { 
    servo1.write(pos);       
    delay(15);            
  }
}

//__________________________________________________________________________________
void downHandShake()
{ /*down handshake for kids*/

  for (pos = 55; pos <= 80; pos += 1) 
  { 
    servo1.write(pos);  
    delay(15);         
  }

  for(pos = 90; pos >= 60; pos -= 1)
  {
    servo4.write(pos);
    delay(15);
   }

   headTilt.write(130);
   delay(3000);
   
   headTilt.write(140);

   for (pos = 60; pos <= 90; pos += 1) 
   {
    servo4.write(pos);            
    delay(15);           
   }
   
   for (pos = 80; pos >= 55; pos -= 1)
   { 
    servo1.write(pos);       
    delay(15);            
  }
}

//___________________________________________________________________________________
void bow()
{
  for (pos = 55; pos <= 85; pos += 1) 
  { 
    servo1.write(pos); 
    delay(15);         
  }

  servo3.write(10);
  delay(100);
  
  for(pos = 90; pos >= 30; pos -= 1)
      {
        servo4.write(pos);
        delay(15);
      }

  for (pos = 120; pos <= 160; pos += 1) 
    { 
    left1.write(pos);        
    delay(15);
    }

 //-----------
 for (pos = 4; pos <= 11; pos += 1) 
 {
    komor.write(pos);         
    delay(150);      
  }
  delay(1000);
  for (pos = 12; pos >= 4; pos -= 1) 
  { 
    komor.write(pos);    
    delay(110);          
  }

  for (pos = 160; pos >= 120; pos -= 1) 
  { 
    left1.write(pos);   
    delay(15);      
  }
  
  servo3.write(90);
  delay(100);

    for (pos = 30; pos <= 90; pos += 1) 
   {
    servo4.write(pos);     
    delay(15);        
   }
   for (pos = 85; pos >= 55; pos -= 1)
   { // goes from 180 degrees to 0 degrees
    servo1.write(pos);              // tell servo to go to position in variable 'pos'
    delay(15);                       // waits 15ms for the servo to reach the position
  }
}

//______________________________________________________________________________________________

void clawClose()
{
  for (pos = 60; pos <= 110; pos += 1) 
  { 
    // in steps of 1 degree
    lFinger.write(pos); 
    delay(15);                       
  }
}

//_____________________________________________________________________________________________

void clawOpen()
{
  for (pos = 110; pos >= 60; pos -= 1) 
  { 
    lFinger.write(pos);             
    delay(15);
  }
}

//_____________________________________________________________________________________________

void clawShow()
{
   for (pos = 110; pos <= 170; pos += 1) { // goes from 0 degrees to 180 degrees
    // in steps of 1 degree
    left4.write(pos);              // tell servo to go to position in variable 'pos'
    delay(15);                       // waits 15ms for the servo to reach the position
  }
  delay(100);

  //Claw
  clawClose();
  delay(100);
  clawOpen();
  delay(100);
  clawClose();
  delay(100);
  clawOpen();
    
  for(pos = 170; pos >= 110; pos -= 1)
  {
    left4.write(pos);
    delay(10);
  }

}
//_______________________________________________________________________________________

void laserPoint()
{
   for (pos = 55; pos <= 130; pos += 1) 
    {
    servo1.write(pos);              
    delay(10);                       
    }
    servo3.write(10);
    delay(100);

    delay(1000);
    rFinger.write(70);
    delay(60);
    
    digitalWrite(laser, HIGH);
    delay(3000);
    digitalWrite(laser, LOW);
    rFinger.write(0);

    servo3.write(90);
    delay(100);

    for (pos = 130; pos >= 55; pos -= 1) 
    {
    servo1.write(pos);              
    delay(15);                       
    }
}


//________________________________________________________________________________________
void speech()
{
  // ** I am (buke haat) [point to chest]
    for (pos = 55; pos <= 85; pos += 1) 
    {
    servo1.write(pos);              
    delay(5);                       
    }

    servo3.write(20);
    delay(100);
  
    for(pos = 90; pos >= 30; pos -= 1)
     {
       servo4.write(pos);
       delay(15);
     }

     delay(1000);
    //buke haat ends

    rightStandBy();
    
    //an advanced humanoid robot of BU

   for (pos = 85; pos >= 55; pos -= 1) 
    {
    servo1.write(pos);              
    delay(5);                       
    }
    
  //make it up (servo2)
  for (pos = 0; pos <= 90; pos += 1) 
  {
    servo2.write(pos);             
    delay(5);                       
  }
    
   //rotate joint (servo3)
   servo3.write(170);
   delay(10);


   //hi up
    for (pos = 90; pos >= 60; pos -= 1) 
    { 
    servo4.write(pos);   
    delay(15); 
    }

    delay(2500);
    
  for (pos = 90; pos >= 0; pos -= 1) 
  {
    servo2.write(pos);             
    delay(10); 

   /* if(pos == 60)
    {
      rightStandBy();
    } 
    */
  }

   rightStandBy();
   delay(900);

//Britannia University (Say and UP both hands)
  for (pos = 0; pos <= 70; pos += 1) 
  {
    left2.write(pos);  
    servo2.write(pos);           
    delay(5);                       
  }

  delay(1000);
  
  for (pos = 70; pos >= 0; pos -= 1) 
  {
    left2.write(pos);  
    servo2.write(pos);           
    delay(15);                       
  }

  delay(1500);

  // ** I have (buke haat) [point to chest]
    for (pos = 55; pos <= 85; pos += 1) 
    {
    servo1.write(pos);              
    delay(10);                       
    }

    left2.write(30);
    
    servo3.write(20);
    delay(100);
  
    for(pos = 90; pos >= 30; pos -= 1)
     {
       servo4.write(pos);
       delay(15);
     }
    left2.write(10);
    delay(200);
    
    servo3.write(90);
    delay(100);
    for (pos = 85; pos >= 55; pos -= 1) 
    {
    servo1.write(pos);              
    delay(5);                       
    }
    rightStandBy();
    //buke haat ends

    //hand Down
    
     delay(3000);
     clawShow();
     for (pos = 134; pos <= 140; pos += 1) 
     {
       headTilt.write(pos);              
       delay(15);   
     }
     for (pos = 140; pos >= 134; pos -= 1) 
     {
      headTilt.write(pos);              
      delay(5);   
     }

     leftStandBy();
     rightStandBy();

     delay(1000);

      for (pos = 90; pos <= 150; pos += 1) 
      {
       headPan.write(pos);              
       delay(20);   
       }
      for (pos = 150; pos >= 30; pos -= 1) 
      {
       headPan.write(pos);              
       delay(20);   
      }

     for (pos = 30; pos <= 90; pos += 1) 
      {
       headPan.write(pos);              
       delay(20);   
      }
     
}


void buke_haat()
{
    // ** I am (buke haat) [point to chest]
    for (pos = 55; pos <= 95; pos += 1) 
    {
    servo1.write(pos);              
    delay(5);                       
    }

    servo3.write(20);
    delay(100);
  
    for(pos = 90; pos >= 30; pos -= 1)
     {
       servo4.write(pos);
       delay(15);
     }

     delay(1000);
    //buke haat ends

    rightStandBy();
}

void heads()
{
  
}

//______________________________________________________----------

//**********Setup things ****************************************************************************************

void setup() 
{
  servo1.attach(8);  // attach the right servo motors to pins 
  servo2.attach(9);
  servo3.attach(10);
  servo4.attach(11);
  rFinger.attach(12);
 
  left1.attach(6);   // attach the left servo motors to pins
  left2.attach(5);
  left3.attach(4);
  left4.attach(3);
  lFinger.attach(2);

  komor.attach(7);      //attach the motor on 

  headTilt.attach(31);  //head servos
  headPan.attach(33);

  pinMode(laser, OUTPUT);  //define laser pin as output
  
  /*default/standby position of servos*/
  komor.write(4);     
  left1.write(120);
  rFinger.write(0);
  servo1.write(55);
  
  clawOpen();
  rightStandBy();
  leftStandBy();
  
  headTilt.write(134);
  headPan.write(90);

  Serial.begin(9600);    //initialize serial communication to pc
}


void loop() 
{

  while(Serial.available() > 0)  //look for serial data available or not
  {
    val = Serial.read();        //read the serial value

    if(val == 'h')   //hi
    {
      Hi();
/*      delay(1000);
      rFinger.write(70);
      delay(600);
      rFinger.write(0);
      delay(600);  */
      rightStandBy();
      //leftStandBy();
    }

    else if(val == 's')   //show off your skills
    {
      show_off();
      rightStandBy();
      leftStandBy();
    }

    else if(val == 'M')   //hand shake to adult / tallers
    {
      handShake();
      rightStandBy();
    }

    else if(val == 'm')   //hand shake to little person
    { 
      downHandShake();
      rightStandBy();
    }

    else if(val == 'b')  //bow
    {
      bow();
      delay(100);
      rightStandBy();
    }

    else if(val == 'A')  //speech code
    {
      Hi();
      delay(100);
      speech();
      delay(100);
      rightStandBy();
    }

    else if(val == 'l')  //laser show
    {
     //Point Laer
     laserPoint();
     delay(100);
      rightStandBy();
    }

    else if(val == 'c')  //left claw show
    {
      clawShow();
      for (pos = 130; pos <= 150; pos += 1) 
      {
       headTilt.write(pos);              
       delay(15);   
       }
      for (pos = 150; pos <= 130; pos -= 1) 
      {
       headTilt.write(pos);              
       delay(5);   
       }
      leftStandBy();
    }

    else if(val == 'B')
    {
      buke_haat();
      rightStandBy();
    }

    
    val = "";           //clear the value
    //rightStandBy();
    //leftStandBy();
  }

  

  /*
  Hi();
  StandBy();
  for (pos = 0; pos <= 150; pos += 1) { // goes from 0 degrees to 180 degrees
    // in steps of 1 degree
    rFinger.write(pos);              // tell servo to go to position in variable 'pos'
    delay(15);                       // waits 15ms for the servo to reach the position
  }
  for (pos = 150; pos >= 0; pos -= 1) { // goes from 180 degrees to 0 degrees
    rFinger.write(pos);              // tell servo to go to position in variable 'pos'
    delay(15);                       // waits 15ms for the servo to reach the position
  }
  delay(2000);

  show_off();

  for(i = 10; i <= 25; i ++)
  {
    komor.write(i);
    delay(100);
  }
  delay(100);
  for(i = 25; i >= 10; i--)
  {
    komor.write(i);
    delay(150);
  }
  delay(1000);

  */
  
}
