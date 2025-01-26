import tkinter as tk


class AgriculturalExpertSystem:
    def __init__(self, root):
        self.root = root
        self.attributes = {
            "soil_type": None,
            "rainfall": None,
            "planted_crop": None,
            "temperature": None
        }
        self.recommendations = []
        self.recommendation_count = 1
        self.create_widgets()

    def create_widgets(self):
        # Configure the root window's background color
        self.root.configure(bg='#f0f0f0')

        # Create a frame for input fields
        input_frame = tk.Frame(self.root, bg='#f0f0f0')
        input_frame.grid(row=0, column=0, padx=20, pady=20)

        # Soil type selection
        tk.Label(input_frame, text="Choose soil type (sandy, loamy, clay):", bg='#f0f0f0').grid(row=0, column=0, sticky=tk.W)
        self.soil_type_var = tk.StringVar(self.root)
        self.soil_type_var.set("sandy")
        soil_type_frame = tk.Frame(input_frame, bg='#f0f0f0')
        soil_type_frame.grid(row=0, column=1)
        for soil_type in ["sandy", "loamy", "clay"]:
            tk.Radiobutton(soil_type_frame, text=soil_type.capitalize(), variable=self.soil_type_var,
                           value=soil_type, bg='#f0f0f0').pack(side=tk.LEFT, padx=5)

        # Rainfall level selection
        tk.Label(input_frame, text="Choose rainfall level (low/medium/high):", bg='#f0f0f0').grid(row=1, column=0, sticky=tk.W)
        self.rainfall_var = tk.StringVar(self.root)
        self.rainfall_var.set("low")
        rainfall_frame = tk.Frame(input_frame, bg='#f0f0f0')
        rainfall_frame.grid(row=1, column=1)
        for rainfall in ["low", "medium", "high"]:
            tk.Radiobutton(rainfall_frame, text=rainfall.capitalize(), variable=self.rainfall_var,
                           value=rainfall, bg='#f0f0f0').pack(side=tk.LEFT, padx=5)

        # Crop type selection
        tk.Label(input_frame, text="Choose the crop type (wheat/corn/rice/none):", bg='#f0f0f0').grid(row=2, column=0, sticky=tk.W)
        self.planted_crop_var = tk.StringVar(self.root)
        self.planted_crop_var.set("wheat")
        crop_type_frame = tk.Frame(input_frame, bg='#f0f0f0')
        crop_type_frame.grid(row=2, column=1)
        for crop in ["wheat", "corn", "rice", "none"]:
            tk.Radiobutton(crop_type_frame, text=crop.capitalize(), variable=self.planted_crop_var,
                           value=crop, bg='#f0f0f0').pack(side=tk.LEFT, padx=5)

        # Temperature input
        tk.Label(input_frame, text="Enter current temperature (°C):", bg='#f0f0f0').grid(row=3, column=0, sticky=tk.W)
        self.temperature_entry = tk.Entry(input_frame)
        self.temperature_entry.grid(row=3, column=1, padx=5)

        # Create a frame for buttons
        button_frame = tk.Frame(self.root, bg='#f0f0f0')
        button_frame.grid(row=1, column=0, padx=20, pady=10)

        # Button to get recommendations
        self.get_recommendations_button = tk.Button(button_frame, text="Get Recommendations",
                                                    command=self.get_user_inputs,
                                                    width=20, height=2,
                                                    bg='#4CAF50', fg='white',
                                                    font=('Arial', 12))
        self.get_recommendations_button.pack(side=tk.LEFT, padx=10)

        # Clear recommendations button
        self.clear_button = tk.Button(button_frame, text="Clear Recommendations",
                                      command=self.clear_recommendations,
                                      width=20, height=2,
                                      bg='#FF5733', fg='white',
                                      font=('Arial', 12))
        self.clear_button.pack(side=tk.LEFT, padx=10)

        # Recommendations label
        tk.Label(self.root, text="Recommendations:", bg='#f0f0f0', font=('Arial', 12, 'bold')).grid(row=2, column=0, padx=20, pady=10, sticky=tk.W)

        # Recommendations display
        self.recommendations_text = tk.Text(self.root, height=25, width=80, font=('Arial', 12))
        self.recommendations_text.grid(row=3, column=0, padx=20, pady=10)

    def get_user_inputs(self):
        self.attributes["soil_type"] = self.soil_type_var.get()
        self.attributes["rainfall"] = self.rainfall_var.get()
        self.attributes["planted_crop"] = self.planted_crop_var.get()
        try:
            self.attributes["temperature"] = int(self.temperature_entry.get())
            self.apply_rules()
            self.display_recommendations()
        except ValueError:
            tk.messagebox.showerror("Error", "Please enter a valid integer for temperature.")

    def apply_rules(self):
        self.recommendations = []

        # Rules for Wheat
        if self.attributes["planted_crop"] == "wheat":
            if self.attributes["soil_type"] == "loamy" and self.attributes["rainfall"] == "medium":
                self.recommendations.append("Rule 1: Wheat thrives in loamy soil with medium rainfall.")
            if self.attributes["temperature"] < 10:
                self.recommendations.append("Rule 2: Wheat requires temperatures above 10°C for optimal growth.")
            if self.attributes["rainfall"] == "low":
                self.recommendations.append("Rule 3: Wheat needs supplemental irrigation in low rainfall areas.")
            if self.attributes["rainfall"] == "high":
                self.recommendations.append("Rule 4: High rainfall during wheat's early growth stage may lead to waterlogging; consider ridge planting.")

        # Rules for Corn
        if self.attributes["planted_crop"] == "corn":
            if self.attributes["soil_type"] in ["loamy", "clay"] and self.attributes["rainfall"] == "high":
                self.recommendations.append("Rule 5: Corn grows best in loamy or clay soils with high rainfall.")
            if self.attributes["temperature"] > 30:
                self.recommendations.append("Rule 6: Corn requires regular watering in temperatures above 30°C.")
            if self.attributes["rainfall"] == "medium":
                self.recommendations.append("Rule 7: Corn can also grow well in medium rainfall areas with proper irrigation.")
            if 20 <= self.attributes["temperature"] <= 30:
                self.recommendations.append("Rule 8: Corn grows optimally between 20°C and 30°C; ensure consistent watering and pest monitoring during flowering.")

        # Rules for Rice
        if self.attributes["planted_crop"] == "rice":
            if self.attributes["soil_type"] == "clay" and self.attributes["rainfall"] == "high":
                self.recommendations.append("Rule 9: Rice requires clay soil and high rainfall.")
            if self.attributes["temperature"] > 25:
                self.recommendations.append("Rule 10: Rice thrives in temperatures above 25°C.")
            if self.attributes["rainfall"] == "medium":
                self.recommendations.append("Rule 11: Rice can be grown in medium rainfall areas with controlled irrigation.")
            if self.attributes["rainfall"] == "low":
                self.recommendations.append("Rule 12: Rice can be cultivated in low rainfall areas using controlled irrigation techniques such as Alternate Wetting and Drying (AWD).")

        # General Temperature-Based Rules
        if self.attributes["temperature"] > 35:
            self.recommendations.append("Rule 13: Use shade nets and increase irrigation to prevent heat stress on crops.")
        if self.attributes["temperature"] < 5:
            self.recommendations.append("Rule 14: Protect crops from frost in temperatures below 5°C.")
            self.recommendations.append("Rule 15: Consider using frost cloths or heaters to protect crops from frost.")
        if 15 <= self.attributes["temperature"] <= 20:
            self.recommendations.append("Rule 16: Temperatures between 15°C and 20°C are ideal for wheat and corn growth stages.")

        # Soil and Rainfall Rules
        if self.attributes["soil_type"] == "sandy" and self.attributes["rainfall"] == "low":
            self.recommendations.append("Rule 17: Sandy soil with low rainfall is unsuitable for rice and wheat; consider irrigation for better crop establishment.")
        if self.attributes["soil_type"] == "clay" and self.attributes["rainfall"] == "low":
            self.recommendations.append("Rule 18: Clay soil with low rainfall requires efficient drainage systems for crops like wheat.")
        if self.attributes["soil_type"] == "loamy" and self.attributes["rainfall"] == "high":
            self.recommendations.append("Rule 19: Loamy soil with high rainfall is ideal for rice and corn.")

        # Rainfall and Temperature Rules
        if self.attributes["rainfall"] == "medium" and self.attributes["temperature"] > 20:
            self.recommendations.append("Rule 20: Medium rainfall and temperatures above 20°C are ideal for corn and rice.")
        if self.attributes["rainfall"] == "high" and self.attributes["temperature"] < 15:
            self.recommendations.append("Rule 21: High rainfall and temperatures below 15°C can impact crop yield; consider soil amendments.")

        # No Crop Planted Rules
        if self.attributes["planted_crop"] == "none":
            if self.attributes["soil_type"] == "loamy" and self.attributes["rainfall"] == "medium":
                self.recommendations.append("Rule 22: Consider planting wheat or corn in loamy soil with medium rainfall.")
            if self.attributes["soil_type"] == "clay" and self.attributes["rainfall"] == "high":
                self.recommendations.append("Rule 23: Consider planting rice in clay soil with high rainfall.")
            if self.attributes["soil_type"] == "sandy" and self.attributes["rainfall"] == "low":
                self.recommendations.append("Rule 24: Consider using supplemental irrigation for corn or wheat in sandy soil with low rainfall.")

    def display_recommendations(self):
        self.recommendations_text.insert(tk.END, f"Recommendations {self.recommendation_count}\n")
        if self.recommendations:
            for i, recommendation in enumerate(self.recommendations, 1):
                self.recommendations_text.insert(tk.END, f"{i}. {recommendation}\n")
        else:
            self.recommendations_text.insert(tk.END, "No recommendations available based on the inputs provided.")
        self.recommendation_count += 1

    def clear_recommendations(self):
        self.recommendations_text.delete(1.0, tk.END)
        self.recommendations = []
        self.recommendation_count = 1


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Agricultural Expert System")
    app = AgriculturalExpertSystem(root)
    root.mainloop()
