class AgriculturalExpertSystem:
    def __init__(self):
        self.attributes = {
            "soil_type": None,
            "rainfall": None,
            "planted_crop": None,
            "temperature": None,
        }
        self.recommendations = []

    def get_user_inputs(self):
        print("Welcome to AgriAdvisor: Comprehensive Farming Guidance!")
        print("Please provide the following details for recommendations:\n")
        self.attributes["soil_type"] = input("Enter soil type (sandy, loamy, clay): ").strip().lower()
        self.attributes["rainfall"] = input("Enter rainfall level (low/medium/high): ").strip().lower()
        self.attributes["planted_crop"] = input("Enter the crop type (wheat/corn/rice/none): ").strip().lower()
        self.attributes["temperature"] = int(input("Enter current temperature (°C): "))

    def apply_rules(self):
        # Rule 1
        if self.attributes["planted_crop"] == "wheat":
            if self.attributes["soil_type"] == "loamy" and self.attributes["rainfall"] == "medium":
                self.recommendations.append("Rule 1: Wheat thrives in loamy soil with medium rainfall.")
            # Rule 2
            if self.attributes["temperature"] < 10:
                self.recommendations.append("Rule 2: Wheat requires temperatures above 10°C for optimal growth.")
            # Rule 3
            if self.attributes["rainfall"] == "low":
                self.recommendations.append("Rule 3: Wheat needs supplemental irrigation in low rainfall areas.")
        
        # Rule 4
        if self.attributes["planted_crop"] == "corn":
            if self.attributes["soil_type"] in ["loamy", "clay"] and self.attributes["rainfall"] == "high":
                self.recommendations.append("Rule 4: Corn grows best in loamy or clay soils with high rainfall.")
            # Rule 5
            if self.attributes["temperature"] > 30:
                self.recommendations.append("Rule 5: Corn requires regular watering in temperatures above 30°C.")
            # Rule 6
            if self.attributes["rainfall"] == "medium":
                self.recommendations.append("Rule 6: Corn can also grow well in medium rainfall areas with proper irrigation.")
        
        # Rule 7
        if self.attributes["planted_crop"] == "rice":
            if self.attributes["soil_type"] == "clay" and self.attributes["rainfall"] == "high":
                self.recommendations.append("Rule 7: Rice requires clay soil and high rainfall.")
            # Rule 8
            if self.attributes["temperature"] > 25:
                self.recommendations.append("Rule 8: Rice thrives in temperatures above 25°C.")
            # Rule 9
            if self.attributes["rainfall"] == "medium":
                self.recommendations.append("Rule 9: Rice can be grown in medium rainfall areas with controlled irrigation.")
        
        # Rule 10
        if self.attributes["temperature"] > 35:
            self.recommendations.append("Rule 10: Use shade nets and increase irrigation to prevent heat stress on crops.")
        
        # Rule 11
        if self.attributes["soil_type"] == "sandy" and self.attributes["rainfall"] == "low":
            self.recommendations.append("Rule 11: Sandy soil with low rainfall is suitable for drought-resistant crops.")
            self.recommendations.append("Rule 12: Consider planting crops like millet or sorghum in sandy soil with low rainfall.")
        
        # Rule 13
        if self.attributes["soil_type"] == "clay" and self.attributes["rainfall"] == "low":
            self.recommendations.append("Rule 13: Clay soil with low rainfall requires efficient drainage systems.")
            self.recommendations.append("Rule 14: Consider planting crops like chickpeas or lentils in clay soil with low rainfall.")
        
        # Rule 15
        if self.attributes["soil_type"] == "loamy" and self.attributes["rainfall"] == "high":
            self.recommendations.append("Rule 15: Loamy soil with high rainfall is ideal for most crops.")
            self.recommendations.append("Rule 16: Consider planting crops like tomatoes or peppers in loamy soil with high rainfall.")
        
        # Rule 17
        if self.attributes["temperature"] < 5:
            self.recommendations.append("Rule 17: Protect crops from frost in temperatures below 5°C.")
            self.recommendations.append("Rule 18: Consider using frost cloths or heaters to protect crops from frost.")
        
        # Rule 19
        if self.attributes["rainfall"] == "medium" and self.attributes["temperature"] > 20:
            self.recommendations.append("Rule 19: Medium rainfall and temperatures above 20°C are ideal for vegetable crops.")
            self.recommendations.append("Rule 20: Consider planting crops like carrots or lettuce in medium rainfall and warm temperatures.")
        
        # Rule 21
        if self.attributes["rainfall"] == "high" and self.attributes["temperature"] < 15:
            self.recommendations.append("Rule 21: High rainfall and temperatures below 15°C are suitable for leafy greens.")
            self.recommendations.append("Rule 22: Consider planting crops like spinach or kale in high rainfall and cool temperatures.")
        
        # Rule 23
        if self.attributes["planted_crop"] == "none":
            if self.attributes["soil_type"] == "loamy" and self.attributes["rainfall"] == "medium":
                self.recommendations.append("Rule 23: Consider planting wheat or corn in loamy soil with medium rainfall.")
            # Rule 24
            if self.attributes["soil_type"] == "clay" and self.attributes["rainfall"] == "high":
                self.recommendations.append("Rule 24: Consider planting rice in clay soil with high rainfall.")
            # Rule 25
            if self.attributes["soil_type"] == "sandy" and self.attributes["rainfall"] == "low":
                self.recommendations.append("Rule 25: Consider planting drought-resistant crops in sandy soil with low rainfall.")

    def display_recommendations(self):
        print("\nRecommendations:")
        if self.recommendations:
            for i, recommendation in enumerate(self.recommendations, 1):
                print(f"{i}. {recommendation}")
        else:
            print("No recommendations available based on the inputs provided.")
        print("\nThank you for using AgriAdvisor!")

    def run(self):
        self.get_user_inputs()
        self.apply_rules()
        self.display_recommendations()


# Run the system
if __name__ == "__main__":
    system = AgriculturalExpertSystem()
    system.run()