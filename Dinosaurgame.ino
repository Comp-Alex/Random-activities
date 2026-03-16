#include <Wire.h>
#include <LiquidCrystal_I2C.h>

// Set the LCD address to 0x27 for a 16 chars and 2 line display
LiquidCrystal_I2C lcd(0x27, 16, 2);

// Pin definitions
const int jumpButton = 2;  // Button for jumping
const int buzzer = 3;      // Buzzer for sound (optional)

// Game variables
int dinoPos = 0;           // Dino position (0 = ground, 1 = jumping)
int obstaclePos = 15;      // Obstacle position (starts from right)
bool jumping = false;
int jumpHeight = 0;
int score = 0;
bool gameOver = false;

// Timing variables
unsigned long lastGameUpdate = 0;
unsigned long lastButtonPress = 0;
const unsigned long gameUpdateInterval = 200;  // Game speed
const unsigned long debounceDelay = 50;       // Button debounce

// Custom characters for dino and cactus
byte dino[8] = {
  B00000,
  B00110,
  B00110,
  B10110,
  B10110,
  B11110,
  B01100,
  B00000
};

byte cactus[8] = {
  B00000,
  B00100,
  B00100,
  B10101,
  B10101,
  B10101,
  B01110,
  B00000
};

void setup() {
  pinMode(jumpButton, INPUT_PULLUP);
  pinMode(buzzer, OUTPUT);

  lcd.init();
  lcd.backlight();
  lcd.createChar(0, dino);
  lcd.createChar(1, cactus);

  // Start screen
  lcd.setCursor(0, 0);
  lcd.print("Dino Game!");
  lcd.setCursor(0, 1);
  lcd.print("Press jump to start");
  while (digitalRead(jumpButton) == HIGH) {
    // Non-blocking wait
  }

  // Initialize game
  resetGame();
}

void loop() {
  if (!gameOver) {
    unsigned long currentMillis = millis();

    if (currentMillis - lastGameUpdate >= gameUpdateInterval) {
      lastGameUpdate = currentMillis;

      // Handle jump
      if (digitalRead(jumpButton) == LOW && !jumping && (currentMillis - lastButtonPress >= debounceDelay)) {
        jumping = true;
        jumpHeight = 4;
        tone(buzzer, 1000, 100);  // Jump sound
        lastButtonPress = currentMillis;
      }

      // Update jump
      if (jumping) {
        jumpHeight--;
        if (jumpHeight <= 0) {
          jumping = false;
          dinoPos = 0;
        } else {
          dinoPos = 1;
        }
      }

      // Move obstacle
      obstaclePos--;
      if (obstaclePos < 0) {
        obstaclePos = 15;
        score++;
      }

      // Check collision
      if (obstaclePos == 1 && dinoPos == 0) {
        gameOver = true;
        tone(buzzer, 500, 500);  // Game over sound
      }

      // Draw game
      drawGame();
    }
  } else {
    // Game over screen with lyrics
    displayGameOver();
  }
}

void drawGame() {
  lcd.clear();

  // Draw dino
  if (dinoPos == 0) {
    lcd.setCursor(1, 1);
  } else {
    lcd.setCursor(1, 0);
  }
  lcd.write(byte(0));

  // Draw obstacle
  if (obstaclePos >= 0 && obstaclePos < 16) {
    if (dinoPos == 0) {
      lcd.setCursor(obstaclePos, 1);
    } else {
      lcd.setCursor(obstaclePos, 1);
    }
    lcd.write(byte(1));
  }

  // Draw ground
  for (int i = 0; i < 16; i++) {
    lcd.setCursor(i, 1);
    if (i != 1 && i != obstaclePos) {  // Don't overwrite dino or obstacle
      lcd.print("_");
    }
  }

  // Display score
  lcd.setCursor(8, 0);
  lcd.print("Score:");
  lcd.print(score);
}

void resetGame() {
  dinoPos = 0;
  obstaclePos = 15;
  jumping = false;
  jumpHeight = 0;
  score = 0;
  gameOver = false;
  lastGameUpdate = millis();
  lastButtonPress = 0;
  lcd.clear();
}

void displayGameOver() {
  static unsigned long lastScroll = 0;
  static int scrollPos = 0;
  const unsigned long scrollInterval = 300;
  const String scrollText = "It was over long ago you just can't let go    ";

  unsigned long currentMillis = millis();

  if (currentMillis - lastScroll >= scrollInterval) {
    lastScroll = currentMillis;
    scrollPos++;
    if (scrollPos >= scrollText.length()) {
      scrollPos = 0;
    }

    // Build a 16-character window to display
    String window = "";
    for (int i = 0; i < 16; i++) {
      int idx = (scrollPos + i) % scrollText.length();
      window += scrollText[idx];
    }

    lcd.clear();
    lcd.setCursor(0, 0);
    lcd.print("Game Over!");
    lcd.setCursor(0, 1);
    lcd.print(window);
  }

  // Check for restart
  if (digitalRead(jumpButton) == LOW && (currentMillis - lastButtonPress >= debounceDelay)) {
    lastButtonPress = currentMillis;
    resetGame();
  }
}