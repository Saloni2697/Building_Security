char x;

void setup() {
  // put your setup code here, to run once:
pinMode(13,OUTPUT);
pinMode(12,OUTPUT);
Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  while(Serial.available()>0){
    char x= Serial.read();
    delay(1000);
    Serial.print(x);
    if (x == 'O') {
      digitalWrite(13,HIGH);
      digitalWrite(12,HIGH);
      delay(5000);
      digitalWrite(13,LOW);
      digitalWrite(12,LOW);
      }
    }
  
}
