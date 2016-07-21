int LEDPIN = 4;
int BUTTON = 5;
void setup() {
  // put your setup code here, to run once
  pinMode(LEDPIN, OUTPUT);
  pinMode(BUTTON, INPUT_PULLUP);
}

void loop() {
  // put your main code here, to run repeatedly:
  if (digitalRead(BUTTON) == HIGH) {
    //waiting 
    digitalWrite(LEDPIN, LOW);
    delay(500);
    //line 1
    digitalWrite(LEDPIN, HIGH);
    digitalWrite(LEDPIN, LOW);
    delay(350);
    digitalWrite(LEDPIN, HIGH);
    digitalWrite(LEDPIN, LOW);
    delay(350);
    digitalWrite(LEDPIN, HIGH);
    digitalWrite(LEDPIN, LOW);
    delay(350);
    digitalWrite(LEDPIN, HIGH);
    digitalWrite(LEDPIN, LOW);
    delay(800);
    digitalWrite(LEDPIN, HIGH);
    digitalWrite(LEDPIN, LOW);
    delay(900);
    //line 2
    digitalWrite(LEDPIN, HIGH);
    digitalWrite(LEDPIN, LOW);
    delay(350);
    digitalWrite(LEDPIN, HIGH);
    digitalWrite(LEDPIN, LOW);
    delay(350);
    digitalWrite(LEDPIN, HIGH);
    digitalWrite(LEDPIN, LOW);
    delay(350);
    digitalWrite(LEDPIN, HIGH);
    digitalWrite(LEDPIN, LOW);
    delay(350);
    digitalWrite(LEDPIN, HIGH);
    digitalWrite(LEDPIN, LOW);
    delay(800);
    digitalWrite(LEDPIN, HIGH);
    digitalWrite(LEDPIN, LOW);
    delay(900);
    //pause
    digitalWrite(LEDPIN, LOW);
    delay(900);
  }
}
