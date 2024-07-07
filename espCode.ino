#include <ESP8266WiFi.h>
#include <ESP8266WebServer.h>
#include <Servo.h>
#include <FastLED.h>

// WiFi credentials
const char* ssid = "hlo12foratk";
const char* password = "1231231234";

// Define servo pins
const int servoPins[] = {D1, D2, D3, D4, D5};
const int numServos = 5;

// Define LED settings
#define LED_PIN     D6
#define NUM_LEDS    20
CRGB leds[NUM_LEDS];

Servo servos[numServos];

ESP8266WebServer server(80);

void handleRoot() {
  server.send(200, "text/plain", String(analogRead(A0)));
}

void moveServosToPosition(int targetPositions[], int speed) {
  int currentPosition[numServos];
  
  // Read current positions of all servos
  for (int i = 0; i < numServos; i++) {
    currentPosition[i] = servos[i].read();
  }

  // Move servos gradually to target positions
  boolean allReached = false;
  while (!allReached) {
    allReached = true;
    for (int i = 0; i < numServos; i++) {
      if (currentPosition[i] != targetPositions[i]) {
        allReached = false;
        int direction = (targetPositions[i] > currentPosition[i]) ? 1 : -1;
        int newPosition = currentPosition[i] + direction * speed;
        newPosition = constrain(newPosition, 0, 180); // Ensure position is within valid range
        servos[i].write(newPosition);
        currentPosition[i] = newPosition;
      }
    }
    delay(10); // Adjust delay as needed for smoother movement
  }
}
void handleServo() {



 if (server.hasArg("led")) {
    String ledData = server.arg("led");
    int commaIndex1 = ledData.indexOf(',');
    int commaIndex2 = ledData.indexOf(',', commaIndex1 + 1);
    if (commaIndex1 == -1 || commaIndex2 == -1 || commaIndex2 >= ledData.length() - 1) {
      server.send(400, "text/plain", "Error: Invalid LED data");
      return;
    }
    String rStr = ledData.substring(0, commaIndex1);
    String gStr = ledData.substring(commaIndex1 + 1, commaIndex2);
    String bStr = ledData.substring(commaIndex2 + 1);
    int r = rStr.toInt();
    int g = gStr.toInt();
    int b = bStr.toInt();
    if (r < 0 || r > 255 || g < 0 || g > 255 || b < 0 || b > 255) {
      server.send(400, "text/plain", "Error: Invalid LED color values");
      return;
    }
    for (int i = 0; i < NUM_LEDS; i++) {
      leds[i] = CRGB(r, g, b);
    }
    FastLED.show();
    server.send(200, "text/plain", "Servo positions set and LED color updated");
  } else {
    server.send(400, "text/plain", "Error: Missing LED data");
  }



  
  if (server.hasArg("servo") && server.hasArg("speed")) {
    // Parse servo positions and speed
    String servoData = server.arg("servo");
    int speed = server.arg("speed").toInt();

    int servoPositions[numServos];
    int servoIndex = 0;
    int startPos = 0;
    for (int i = 0; i < servoData.length(); i++) {
      if (servoData.charAt(i) == ',') {
        servoPositions[servoIndex++] = servoData.substring(startPos, i).toInt();
        startPos = i + 1;
      }
    }
    servoPositions[servoIndex] = servoData.substring(startPos).toInt();

    if (servoIndex + 1 == numServos) {
      // Move servos to target positions gradually
      moveServosToPosition(servoPositions, speed);
      
      // Send response
      server.send(200, "text/plain", "Servo positions set gradually");
    } else {
      server.send(400, "text/plain", "Error: Incorrect number of servo positions");
      return;
    }
  } else {
    server.send(400, "text/plain", "Error: Missing servo data");
    return;
  }

  // LED data processing
 
}


void setup() {
  Serial.begin(9600); // Set baud rate

  // Connect to WiFi
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.println("Connecting to WiFi...");
  }
  Serial.println("Connected to WiFi");

  // Attach servos to pins
  for (int i = 0; i < numServos; i++) {
    servos[i].attach(servoPins[i], 500, 2400);
  }

  // Initialize LEDs
  FastLED.addLeds<WS2812B, LED_PIN, GRB>(leds, NUM_LEDS);
  FastLED.clear();
  FastLED.show();

  // Initialize web server routes
  server.on("/", handleRoot);
  server.on("/control", HTTP_GET, handleServo);

  server.begin();
  Serial.println("HTTP server started");
}

void loop() {
  server.handleClient();
      FastLED.show();

}
