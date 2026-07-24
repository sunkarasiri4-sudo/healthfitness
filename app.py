from flask import Flask, render_template, request

app = Flask(__name__)

# -------------------------------
# Home Page
# -------------------------------
@app.route("/")
def home():
    return render_template("index.html")


# -------------------------------
# Login Page
# -------------------------------
@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        name = request.form.get("name")
        age = request.form.get("age")
        phone = request.form.get("phone")
        email = request.form.get("email")

        return render_template(
            "dashboard.html",
            name=name,
            age=age,
            phone=phone,
            email=email
        )

    return render_template("login.html")


# -------------------------------
# Dashboard
# -------------------------------
@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")


# -------------------------------
# Health Details
# -------------------------------
@app.route("/health/<disease>")
def health_details(disease):

    health_data = {

        "bp": {
            "disease_name": "Blood Pressure",
            "eat_foods": [
                "Banana",
                "Leafy Vegetables",
                "Oats",
                "Low-fat Milk",
                "Beetroot"
            ],
            "avoid_foods": [
                "Salt",
                "Pickles",
                "Junk Food",
                "Soft Drinks"
            ],
            "exercises": [
                "Walking - 30 mins",
                "Yoga",
                "Meditation"
            ],
            "water_plan": [
                "Drink 2.5 to 3 Liters Daily"
            ],
            "tips": [
                "Reduce stress",
                "Sleep 8 hours",
                "Check BP regularly"
            ]
        },

        "sugar": {
            "disease_name": "Diabetes",
            "eat_foods": [
                "Brown Rice",
                "Whole Grains",
                "Vegetables",
                "Nuts"
            ],
            "avoid_foods": [
                "Sugar",
                "Sweets",
                "Soft Drinks",
                "White Bread"
            ],
            "exercises": [
                "Walking",
                "Cycling",
                "Yoga"
            ],
            "water_plan": [
                "Drink 3 Liters Daily"
            ],
            "tips": [
                "Monitor blood sugar",
                "Avoid sugary foods",
                "Exercise daily"
            ]
        },

        "fever": {
            "disease_name": "Fever",
            "eat_foods": [
                "Soup",
                "Rice",
                "Fruits",
                "Coconut Water"
            ],
            "avoid_foods": [
                "Oily Food",
                "Spicy Food"
            ],
            "exercises": [
                "Take Rest"
            ],
            "water_plan": [
                "Drink 3-4 Liters Daily"
            ],
            "tips": [
                "Take medicines on time",
                "Consult doctor if fever continues"
            ]
        },

        "gas": {
            "disease_name": "Gas Trouble",
            "eat_foods": [
                "Curd",
                "Banana",
                "Ginger Tea",
                "Rice"
            ],
            "avoid_foods": [
                "Soft Drinks",
                "Beans",
                "Fried Food"
            ],
            "exercises": [
                "Walking",
                "Breathing Exercises"
            ],
            "water_plan": [
                "Drink 3 Liters Daily"
            ],
            "tips": [
                "Eat slowly",
                "Avoid overeating"
            ]
        },

        "weight": {
            "disease_name": "Weight Loss",
            "eat_foods": [
                "Protein",
                "Eggs",
                "Vegetables",
                "Fruits"
            ],
            "avoid_foods": [
                "Fast Food",
                "Cold Drinks",
                "Bakery Items"
            ],
            "exercises": [
                "Running",
                "Gym",
                "Skipping"
            ],
            "water_plan": [
                "Drink 3-4 Liters Daily"
            ],
            "tips": [
                "Exercise regularly",
                "Eat healthy"
            ]
        },

        "stress": {
            "disease_name": "Stress",
            "eat_foods": [
                "Dark Chocolate",
                "Fruits",
                "Nuts"
            ],
            "avoid_foods": [
                "Alcohol",
                "Too much Coffee"
            ],
            "exercises": [
                "Yoga",
                "Meditation"
            ],
            "water_plan": [
                "Drink 2.5 Liters Daily"
            ],
            "tips": [
                "Sleep well",
                "Listen to music",
                "Practice meditation"
            ]
        },

        "sleep": {
            "disease_name": "Sleep Problems",
            "eat_foods": [
                "Warm Milk",
                "Banana",
                "Almonds"
            ],
            "avoid_foods": [
                "Coffee",
                "Tea at Night"
            ],
            "exercises": [
                "Light Yoga",
                "Deep Breathing"
            ],
            "water_plan": [
                "Drink 2 Liters Daily"
            ],
            "tips": [
                "Sleep before 10 PM",
                "Avoid mobile before sleep"
            ]
        },

        "fitness": {
            "disease_name": "Fitness",
            "eat_foods": [
                "Protein Foods",
                "Vegetables",
                "Fruits",
                "Healthy Fats"
            ],
            "avoid_foods": [
                "Junk Food",
                "Sugary Drinks"
            ],
            "exercises": [
                "Push-ups",
                "Squats",
                "Running",
                "Cycling"
            ],
            "water_plan": [
                "Drink 3 Liters Daily"
            ],
            "tips": [
                "Exercise every day",
                "Sleep 8 hours",
                "Stay hydrated"
            ]
        }

    }

    disease = disease.lower()

    if disease in health_data:
        return render_template(
            "health_details.html",
            **health_data[disease]
        )

    return "<h2>Disease information not found.</h2>"


# -------------------------------
# Run Flask App
# -------------------------------
import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)