# Smart Home Multiple Inheritance Example

## Overview
This Python script demonstrates the concept of multiple inheritance by creating a `SmartHome` class that inherits from both `SecuritySystem` and `LightingSystem` classes.

## Classes

### LightingSystem
- Manages the status of home lighting
- Methods:
  - `turn_on_lights()`: Activates home lights
  - `turn_off_lights()`: Deactivates home lights

### SecuritySystem
- Manages the home security system status
- Methods:
  - `arm_security()`: Arms the security system
  - `disarm_security()`: Disarms the security system

### SmartHome
- Inherits from both `SecuritySystem` and `LightingSystem`
- Additional method `display_status()` that demonstrates the inherited functionality
- Allows creation of a smart home object with lighting and security capabilities

## Key Concepts Demonstrated
- Multiple Inheritance
- Method Inheritance
- Super() Method Usage
- Object-Oriented Programming in Python

