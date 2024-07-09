# projects

"Automatic Street Lights Control"
1. Components:
 - Solar Panel: Captures sunlight and converts it into electrical energy.
 - Battery: Stores the solar energy for nighttime use.
 - Arduino Uno: Microcontroller that controls the system.
 - LEDs: Light-emitting diodes used as street lights.
 - Motion Sensors: Detects movement in the vicinity.
 - LDR (Light Dependent Resistor): Measures ambient light levels.
 - Resistors: Used for current limiting and voltage division.

2. Functionality:
 -Daytime Operation:
 - When sunlight is available (detected by the LDR), the system remains inactive.
 - The solar panel charges the battery during the day.
 - LEDs are turned off to save energy.
 -Nighttime Operation:
 - As daylight decreases, the LDR detects low light levels.
 - LEDs turn on automatically to illuminate the street.
 - The system runs on stored solar energy from the battery.
 -Motion Sensor Activation:
 - When motion is detected (e.g., a person or vehicle passing by), specific LEDs are activated.
 - Only the required lights near the motion area turn on.
 - Other LEDs remain off to conserve energy.
 -Energy Efficiency:
 - By using motion sensors, the system optimizes energy usage.
 - Only the necessary lights are powered, reducing overall consumption.
 - Approximately 50-60% of solar power can be stored for other electrical applications.

3. Benefits:
 - Energy-efficient: Illuminates only when needed.
 - Reduces electricity bills.
 - Environmentally friendly due to solar power usage.
 - Enhances safety by activating lights near motion areas.
