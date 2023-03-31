const int ledPin = D7;
const int switchPin = D2;
volatile int state = LOW;

void setup()
{
  pinMode(ledPin, OUTPUT);
  pinMode(switchPin, INPUT_PULLUP);
  attachInterrupt(switchPin, blink, FALLING);
}

void dot()
{
  digitalWrite(ledPin, HIGH);
  delay(333.33);
  digitalWrite(ledPin, LOW);
  delay(1000);
}

void dash()
{
  digitalWrite(ledPin, HIGH);
  delay(1000);
  digitalWrite(ledPin, LOW);
  delay(1000);
}

void loop()
{
  if (state == HIGH)
  {
    // Mustafa
    // M
    dash();
    dash();
    delay(3000);

    // U
    dot();
    dot();
    dash();
    delay(3000);

    // S
    dot();
    dot();
    dot();
    delay(3000);

    // T
    dash();
    delay(3000);

    // A
    dot();
    dash();
    delay(3000);

    // F
    dot();
    dot();
    dash();
    dot();
    delay(3000);

    // A
    dot();
    dash();
    delay(3000);

    // Arsala
    delay(3500);
    // A
    dot();
    dash();
    delay(3000);

    // R
    dot();
    dash();
    dot();
    delay(3000);

    // S
    dot();
    dot();
    dot();
    delay(3000);

    // A
    dot();
    dash();
    delay(3000);

    // L
    dot();
    dash();
    dot();
    dot();
    delay(3000);

    // A
    dot();
    dash();
  }
}

void blink()
{
  state = !state;
}