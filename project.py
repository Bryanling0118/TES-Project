class AgriculturalExpertSystem:
    def __init__(self):
        self.attributes = {
            "area": None,
            "soil_type": None,
            "weather": None,
            "rainfall": None,
            "planted_crop": None,
            "crop_stage": None,
            "soil_quality": None,
            "temperature": None,
            "sunlight": None,
            "season": None,
            "pest_level": None,
            "market_demand": None,
        }
        self.recommendations = []

    def get_user_inputs(self):
        print("Welcome to AgriAdvisor: Comprehensive Farming Guidance!")
        print("Please provide the following details for recommendations:\n")
        self.attributes["area"] = input("Enter your area type (tropical/temperate/arid): ").strip().lower()
        self.attributes["soil_type"] = input("Enter soil type (sandy, loamy, clay, silt): ").strip().lower()
        self.attributes["weather"] = input("Enter weather condition (hot, rainy, cold, humid): ").strip().lower()
        self.attributes["rainfall"] = input("Enter rainfall level (low/medium/high): ").strip().lower()
        self.attributes["planted_crop"] = input("Enter the crop type (wheat/corn/rice/potatoes/soybeans/cotton): ").strip().lower()
        self.attributes["crop_stage"] = input("Enter crop growth stage (seedling, vegetative, flowering, harvesting, none): ").strip().lower()
        self.attributes["soil_quality"] = input("Enter soil quality (poor/fertile): ").strip().lower()
        self.attributes["temperature"] = int(input("Enter current temperature (°C): "))
        self.attributes["sunlight"] = input("Enter sunlight level (low/medium/high): ").strip().lower()
        self.attributes["season"] = input("Enter the current season (summer/winter/spring/autumn): ").strip().lower()
        self.attributes["pest_level"] = input("Enter pest level (low/medium/high): ").strip().lower()
        self.attributes["market_demand"] = input("Enter market demand for your crop (low/medium/high): ").strip().lower()

    def apply_rules(self):
        # Detailed Crop Recommendations
        if self.attributes["planted_crop"] == "wheat":
            if self.attributes["soil_type"] == "loamy" and self.attributes["rainfall"] == "medium":
                self.recommendations.append("Wheat thrives in loamy soil with medium rainfall; ensure proper fertilization with nitrogen.")
            if self.attributes["crop_stage"] == "vegetative" and self.attributes["pest_level"] == "medium":
                self.recommendations.append("Monitor pests and use biological pest control to minimize damage during wheat's vegetative stage.")
        
        if self.attributes["planted_crop"] == "corn":
            if self.attributes["soil_type"] in ["loamy", "clay"] and self.attributes["sunlight"] == "high":
                self.recommendations.append("Corn grows best in loamy or clay soils with high sunlight exposure.")
            if self.attributes["crop_stage"] == "flowering" and self.attributes["weather"] == "hot":
                self.recommendations.append("Ensure consistent watering during the flowering stage of corn in hot weather to maximize yields.")
        
        if self.attributes["planted_crop"] == "rice":
            if self.attributes["soil_type"] == "clay" and self.attributes["rainfall"] == "high":
                self.recommendations.append("Rice requires clay soil and high rainfall; waterlogging is acceptable for optimal growth.")
            if self.attributes["season"] == "summer" and self.attributes["temperature"] > 30:
                self.recommendations.append("Rice thrives in summer temperatures above 30°C; ensure consistent irrigation.")
        
        if self.attributes["planted_crop"] == "potatoes":
            if self.attributes["soil_type"] == "sandy" and self.attributes["rainfall"] == "low":
                self.recommendations.append("Potatoes grow well in sandy soil with low to medium rainfall; ensure adequate irrigation.")
            if self.attributes["crop_stage"] == "vegetative" and self.attributes["pest_level"] == "high":
                self.recommendations.append("Apply targeted pesticides to control pests during the vegetative stage of potatoes.")
        
        if self.attributes["planted_crop"] == "soybeans":
            if self.attributes["soil_quality"] == "poor":
                self.recommendations.append("Soybeans can improve poor soil by fixing nitrogen; consider planting as a rotation crop.")
            if self.attributes["crop_stage"] == "flowering" and self.attributes["sunlight"] == "medium":
                self.recommendations.append("Soybeans in flowering stage benefit from medium sunlight and adequate irrigation.")
        
        if self.attributes["planted_crop"] == "cotton":
            if self.attributes["area"] == "arid" and self.attributes["rainfall"] == "low":
                self.recommendations.append("Cotton is suited for arid regions with low rainfall; use drip irrigation to conserve water.")
            if self.attributes["crop_stage"] == "seedling" and self.attributes["temperature"] > 25:
                self.recommendations.append("Maintain temperatures above 25°C for optimal seedling growth in cotton.")

        # Additional Recommendations for No Specific Crop
        if self.attributes["planted_crop"] == "none":
            if self.attributes["area"] == "temperate" and self.attributes["season"] == "spring":
                self.recommendations.append("In temperate areas during spring, consider planting barley or soybeans.")
            if self.attributes["soil_quality"] == "poor" and self.attributes["rainfall"] == "low":
                self.recommendations.append("Plant legumes like peanuts or chickpeas to improve soil quality.")

        # Weather Adaptation Rules
        if self.attributes["temperature"] > 35 and self.attributes["weather"] == "hot":
            self.recommendations.append("Use shade nets and increase irrigation to prevent heat stress on crops.")
        if self.attributes["weather"] == "rainy" and self.attributes["soil_type"] == "clay":
            self.recommendations.append("Construct drainage channels to prevent waterlogging in clay soil during rainy weather.")

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