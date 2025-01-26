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


# addition rule
# Rule base, containing crop recommendation and planting advice rules
rules = [
    # Recommendation when in tropical area, loamy soil, hot weather, high rainfall, and no crop planted
    {
        "name": "Rule 1: Tropical Loamy Soil High Rainfall No Crop Planted Recommendation",
        "conditions": [
            lambda area, soil_type, weather, rainfall, planted_crop, growth_stage, soil_quality, temperature, sunlight, season:
            area == "tropical" and soil_type == "loamy" and weather == "hot" and rainfall == "high" and
            planted_crop == "none"
        ],
        "conclusion": "It is recommended to plant rice, bananas, and mangoes. Rice is suitable for growing in loamy soil in tropical areas, and the hot weather with high rainfall also meets its growth requirements. It is recommended to start sowing at the beginning of the rainy season. Before sowing, the land needs to be deeply plowed and fertilized, mainly with organic fertilizers; Bananas like a hot and rainy environment. When planting, choose a well-drained plot, fertilize regularly, and do a good job in pest control; Mangoes are suitable for growing in places with sufficient sunlight and fertile soil. Pay attention to reasonable pruning of the tree shape to promote ventilation and light transmission."
    },
    # Recommendation when in temperate area, sandy soil, hot weather, low rainfall, and no crop planted
    {
        "name": "Rule 2: Temperate Sandy Soil Low Rainfall No Crop Planted Recommendation",
        "conditions": [
            lambda area, soil_type, weather, rainfall, planted_crop, growth_stage, soil_quality, temperature, sunlight, season:
            area == "temperate" and soil_type == "sandy" and weather == "hot" and rainfall == "low" and
            planted_crop == "none"
        ],
        "conclusion": "It is recommended to plant corn, watermelons, and peanuts. Corn has a good adaptability to sandy soil. In a hot and low rainfall environment in temperate areas, it is more appropriate to choose drought-resistant varieties of corn for planting. The sowing time can be selected in spring, and pay attention to reasonable irrigation during the planting process; Watermelons like sandy soil, are drought-tolerant and afraid of waterlogging, and need sufficient light and appropriate fertilization during the growth period; Peanuts are suitable for growing in sandy soil, and can be sown in spring. Pay attention to preventing underground pests."
    },
    # Recommendation when in arid area, clay soil, hot weather, low rainfall, and no crop planted
    {
        "name": "Rule 3: Arid Clay Soil Low Rainfall No Crop Planted Recommendation",
        "conditions": [
            lambda area, soil_type, weather, rainfall, planted_crop, growth_stage, soil_quality, temperature, sunlight, season:
            area == "arid" and soil_type == "clay" and weather == "hot" and rainfall == "low" and
            planted_crop == "none"
        ],
        "conclusion": "It is recommended to plant sorghum, cotton, and prickly pear. Sorghum has strong drought resistance and is suitable for growing in clay soil in arid areas. Sowing can be carried out after the temperature rises in spring. When planting, pay attention to maintaining an appropriate plant spacing and row spacing; Cotton is drought-tolerant and can also grow in clay soil. When planting, reasonable close planting is required, and do a good job in pruning and pinching; Prickly pear adapts to arid environments, and the management is relatively extensive. Pay attention to preventing pests and diseases."
    },
    # Advice when wheat is planted and in the seedling stage, with poor soil quality
    {
        "name": "Rule 4: Wheat Seedling Stage Poor Soil Quality Advice",
        "conditions": [
            lambda area, soil_type, weather, rainfall, planted_crop, growth_stage, soil_quality, temperature, sunlight, season:
            planted_crop == "wheat" and growth_stage == "seedling" and soil_quality == "poor"
        ],
        "conclusion": "The wheat you planted is in the seedling stage, and the soil quality is poor. It is recommended to apply an appropriate amount of nitrogen and phosphorus fertilizers in a timely manner to promote the growth of the seedling roots and leaves. At the same time, pay attention to keeping the soil moist, but avoid waterlogging. You can apply a thin liquid fertilizer every 7 - 10 days, and apply it 2 - 3 times continuously."
    },
    # Advice when corn is planted and in the flowering stage, with high rainfall
    {
        "name": "Rule 5: Corn Flowering Stage High Rainfall Advice",
        "conditions": [
            lambda area, soil_type, weather, rainfall, planted_crop, growth_stage, soil_quality, temperature, sunlight, season:
            planted_crop == "corn" and growth_stage == "flowering" and rainfall == "high"
        ],
        "conclusion": "The corn you planted is in the flowering stage, and the rainfall is high at this time. Pay attention to timely drainage to prevent waterlogging in the field from affecting the pollination and fruiting of corn. At the same time, you can appropriately spray some trace element fertilizers, such as boron fertilizer, to improve the stress resistance and yield of corn. It is recommended to check the drainage situation every 3 - 5 days to ensure smooth drainage."
    },
    # Advice when wheat is planted in a tropical area, loamy soil, hot weather, and medium rainfall
    {
        "name": "Rule 6: Tropical Loamy Soil Medium Rainfall Wheat Planting Advice",
        "conditions": [
            lambda area, soil_type, weather, rainfall, planted_crop, growth_stage, soil_quality, temperature, sunlight, season:
            area == "tropical" and soil_type == "loamy" and weather == "hot" and rainfall == "medium" and
            planted_crop == "wheat"
        ],
        "conclusion": "When planting wheat in loamy soil in a tropical area, with hot weather and medium rainfall, wheat growth may face challenges. It is necessary to pay attention to irrigation and drainage management to avoid drought and waterlogging. At the same time, select wheat varieties suitable for the tropical climate and prevent and control pests and diseases in a timely manner. It is recommended to regularly monitor the soil moisture and carry out irrigation and drainage according to the actual situation."
    },
    # Recommendation when in a temperate area, silt soil, cold weather, high rainfall, and no crop planted
    {
        "name": "Rule 7: Temperate Silt Soil High Rainfall No Crop Planted Recommendation",
        "conditions": [
            lambda area, soil_type, weather, rainfall, planted_crop, growth_stage, soil_quality, temperature, sunlight, season:
            area == "temperate" and soil_type == "silt" and weather == "cold" and rainfall == "high" and
            planted_crop == "none"
        ],
        "conclusion": "It is recommended to plant barley, rye, and Chinese cabbage. Barley has a certain tolerance to cold climates and can grow well in silt soil in temperate areas. High rainfall also meets its growth needs. Sowing can be carried out in autumn. Before sowing, deeply plow the soil and apply sufficient base fertilizer; Rye is highly cold-resistant and can also grow well in this environment. Pay attention to reasonable close planting when planting; Chinese cabbage has strong adaptability and is suitable for planting in autumn. It needs sufficient water and fertilizer during the growth period."
    },
    # Advice when corn is planted in an arid area, sandy soil, hot weather, and medium rainfall
    {
        "name": "Rule 8: Arid Sandy Soil Medium Rainfall Corn Planting Advice",
        "conditions": [
            lambda area, soil_type, weather, rainfall, planted_crop, growth_stage, soil_quality, temperature, sunlight, season:
            area == "arid" and soil_type == "sandy" and weather == "hot" and rainfall == "medium" and
            planted_crop == "corn"
        ],
        "conclusion": "When planting corn in sandy soil in an arid area, with hot weather and medium rainfall, special attention should be paid to water management. Water-saving irrigation methods such as drip irrigation can be used to ensure the water required for corn growth. At the same time, increase the application of organic fertilizers to improve the water and fertilizer retention capacity of the soil. It is recommended to carry out drip irrigation once every 1 - 2 days, and adjust the irrigation time according to the soil moisture content."
    },
    # Advice when wheat is planted in a temperate area, loamy soil, rainy weather, low temperature
    {
        "name": "Rule 9: Temperate Loamy Soil Rainy Low Temperature Wheat Planting Advice",
        "conditions": [
            lambda area, soil_type, weather, rainfall, planted_crop, growth_stage, soil_quality, temperature, sunlight, season:
            area == "temperate" and soil_type == "loamy" and weather == "rainy" and rainfall == "low" and
            planted_crop == "wheat" and temperature < 10
        ],
        "conclusion": "The wheat you planted is in loamy soil in a temperate area, and the current weather is rainy and the temperature is low. It is necessary to do a good job in the drainage of the wheat field to prevent root hypoxia. At the same time, you can appropriately cover straw and other materials for heat preservation to promote wheat growth. It is recommended to clean the drainage ditch every 3 - 5 days to ensure smooth drainage."
    },
    # Advice when corn is planted in a tropical area, clay soil, hot weather, and high rainfall
    {
        "name": "Rule 10: Tropical Clay Soil High Rainfall Corn Planting Advice",
        "conditions": [
            lambda area, soil_type, weather, rainfall, planted_crop, growth_stage, soil_quality, temperature, sunlight, season:
            area == "tropical" and soil_type == "clay" and weather == "hot" and rainfall == "high" and
            planted_crop == "corn"
        ],
        "conclusion": "When planting corn in clay soil in a tropical area, in a hot and high rainfall environment, pay attention to preventing pests and diseases, especially pests such as the corn borer. At the same time, due to the poor air permeability of clay soil, it is necessary to carry out reasonable cultivation and loosening of the soil to promote the respiration of corn roots. It is recommended to carry out cultivation and loosening of the soil once every 7 - 10 days, with a depth controlled at 5 - 10 cm."
    },
    # Advice when bananas are planted in a tropical area, sandy soil, hot weather, and high rainfall
    {
        "name": "Rule 11: Tropical Sandy Soil High Rainfall Banana Planting Advice",
        "conditions": [
            lambda area, soil_type, weather, rainfall, planted_crop, growth_stage, soil_quality, temperature, sunlight, season:
            area == "tropical" and soil_type == "sandy" and weather == "hot" and rainfall == "high" and
            planted_crop == "banana"
        ],
        "conclusion": "When planting bananas in sandy soil in a tropical area, under the conditions of hot weather and high rainfall, banana growth is relatively favorable, but attention should be paid to preventing soil nutrient loss. It is recommended to regularly apply organic fertilizers and potassium fertilizers to enhance the lodging resistance of banana trees. At the same time, do a good job in drainage to avoid root rot caused by waterlogging. You can apply organic fertilizers once every 1 - 2 months, with a dosage of 5 - 10 kg per plant each time."
    },
    # Advice when apples are planted in a temperate area, loamy soil, cold weather, and low rainfall
    {
        "name": "Rule 12: Temperate Loamy Soil Cold Low Rainfall Apple Planting Advice",
        "conditions": [
            lambda area, soil_type, weather, rainfall, planted_crop, growth_stage, soil_quality, temperature, sunlight, season:
            area == "temperate" and soil_type == "loamy" and weather == "cold" and rainfall == "low" and
            planted_crop == "apple"
        ],
        "conclusion": "The apples you planted are in loamy soil in a temperate area, and the current weather is cold and the rainfall is low. In winter, do a good job in cold protection and heat preservation measures, such as whitewashing the tree trunks and wrapping them with straw ropes. At the same time, pay attention to reasonable irrigation to keep the soil moderately moist. Before the spring budding, you can apply a nitrogen fertilizer to promote the growth of new shoots. It is recommended to whitewash the tree trunks in November every year, with a whitewashing height of 1 - 1.5 meters."
    }
]