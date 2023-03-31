int LightSensorPin = A5;
int LightIntensity = 0;

void setup() {
    
  pinMode(LightSensorPin, INPUT);
  
}

void loop() {
    
    LightIntensity = analogRead(LightSensorPin);
    
    Particle.publish("Light_Intensity", String(LightIntensity), PRIVATE);
    
    delay(30000);
}