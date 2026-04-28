import random

# -------------------------------
# Environment with Adversarial Noise
# -------------------------------
class FarmEnvironment:
    def __init__(self, noise=False):
        self.noise = noise  # if True → adversarial environment
        self.reset()

    def reset(self):
        self.real_moisture = random.randint(30, 70)
        self.temperature = random.randint(20, 35)
        self.plant_health = 100

    def get_sensor_data(self):
        """
        Returns possibly incorrect sensor readings
        """
        moisture = self.real_moisture

        if self.noise:
            # Add misleading noise (adversarial condition)
            if random.random() < 0.3:  # 30% chance of wrong reading
                moisture += random.randint(-20, 20)

        moisture = max(0, min(100, moisture))

        return moisture, self.temperature, self.plant_health

    def apply_action(self, action):
        """
        Apply agent action
        """
        if action == "WATER":
            self.real_moisture += 15

        # Natural changes
        self.real_moisture -= random.randint(3, 7)
        self.temperature += random.randint(-2, 2)

        # Keep valid
        self.real_moisture = max(0, min(100, self.real_moisture))

        # Update plant health
        if self.real_moisture < 25:
            self.plant_health -= 5
        elif self.real_moisture > 80:
            self.plant_health -= 2

        if self.temperature > 40 or self.temperature < 15:
            self.plant_health -= 3

        self.plant_health = max(0, min(100, self.plant_health))


# -------------------------------
# Intelligent Agent with Reasoning
# -------------------------------
class SmartAgent:
    def decide(self, moisture, temp, health):
        """
        Decision-making with uncertainty handling
        """

        # Rule 1: obvious dry soil
        if moisture < 25:
            return "WATER"

        # Rule 2: suspicious reading (possible noise)
        if 25 <= moisture <= 35 and temp < 25:
            return "DO_NOTHING"  # avoid overwatering

        # Rule 3: high temperature risk
        if temp > 38:
            return "WATER"

        # Rule 4: low health alert
        if health < 50:
            return "ALERT"

        return "DO_NOTHING"


# -------------------------------
# Simulation Runner
# -------------------------------
def run_simulation(noise=False, steps=20):
    env = FarmEnvironment(noise=noise)
    agent = SmartAgent()

    total_health = 0

    print("\n--- Simulation Start ---")
    print("Adversarial Noise:", noise)

    for step in range(steps):
        moisture, temp, health = env.get_sensor_data()

        action = agent.decide(moisture, temp, health)

        print(f"\nStep {step+1}")
        print(f"Sensor Moisture: {moisture}")
        print(f"Temperature: {temp}")
        print(f"Health: {health}")
        print(f"Action: {action}")

        env.apply_action(action)

        total_health += env.plant_health

    avg_health = total_health / steps
    print("\nAverage Plant Health:", avg_health)

    return avg_health


# -------------------------------
# Evaluation (IMPORTANT FOR REPORT)
# -------------------------------
def evaluate():
    normal = run_simulation(noise=False)
    noisy = run_simulation(noise=True)

    print("\n--- Evaluation Result ---")
    print(f"Normal Environment Health: {normal}")
    print(f"Noisy Environment Health: {noisy}")

    if noisy < normal:
        print("Performance decreased under adversarial conditions.")
    else:
        print("Agent handled noise effectively!")


# -------------------------------
# Run Project
# -------------------------------
if __name__ == "__main__":
    evaluate()