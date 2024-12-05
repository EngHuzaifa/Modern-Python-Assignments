# Multiple Inheritance

class LightingSystem:
    def __init__(self, light_status: str):
        self.light_status = light_status
    
    def turn_on_lights(self):
        self.light_status = "On"
        print("Turning on lights...")
    
    def turn_off_lights(self):
        self.light_status = "Off"
        print("Turning off lights...")

class SecuritySystem:
    def __init__(self, security_status: str):
        self.security_status = security_status  
    
    def arm_security(self):
        self.security_status = "Armed"
        print("Arming security system...")
    
    def disarm_security(self):
        self.security_status = "Disarmed"
        print("Disarming security system...")

class SmartHome(SecuritySystem, LightingSystem):
    def __init__(self, light_status: str, security_status: str, home_name: str):
        # Properly initialize both parent classes
        SecuritySystem.__init__(self, security_status)
        LightingSystem.__init__(self, light_status)
        self.home_name = home_name
    
    def display_status(self):
        print(f"Smart Home: {self.home_name}")
        print(f"Current Light Status: {self.light_status}")
        print(f"Current Security Status: {self.security_status}")
        
        self.arm_security()
        self.turn_on_lights()
        
        self.disarm_security()
        self.turn_off_lights()

# Create object
smart_home = SmartHome("Off", "Disarmed", "My Home")
smart_home.display_status()