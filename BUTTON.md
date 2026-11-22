# Home-Made "Easy" Button

## Materials
- [ ] cardboard
- [ ] conductive tape (copper foil)
- [ ] two jumper wires
- ~~3D-printed components~~
- ~~compression springs~~
- ~~foam~~
- ~~non-conductive tape (painter's)~~

## Assembly
1. Cut a rectangular strip of cardboard.
2. Loosely fold the cardboard in half, forming a V shape.
3. Apply copper foil tape to both inside surfaces, aligning the contacts.
4. Fold the edge of each copper strip around a jumper pin and pinch firmly to secure it.

## Testing
Upload the following sketch to an Arduino, adjusting the pins as necessary.
```
#define BUTTON_PIN 2

void setup() {
	Serial.begin(115200);
	pinMode(BUTTON_PIN, INPUT_PULLUP);
}

<<<<<<< HEAD
void loop() {
	if (digitalRead(BUTTON_PIN) == LOW) {
		Serial.println("Button pressed!");

		while (digitalRead(BUTTON_PIN) == LOW) {
			delay(10);
		}

		delay(50);
	}
}
```
Connect one jumper wire to a digital input pin and the other to GND.

Each button press should produce the following output in the serial monitor:
```
Button pressed!
```

❤️🧡💛 **HOORAY! YOU MADE A BUTTON!** 💚💙💜
