"""Generate simple gardening advice for a season and plant type."""

SEASON_ADVICE = {
    "summer": "Water your plants regularly and provide some shade.",
    "winter": "Protect your plants from frost with covers.",
}
PLANT_ADVICE = {
    "flower": "Use fertiliser to encourage blooms.",
    "vegetable": "Keep an eye out for pests!",
}


def get_advice(season, plant_type):
    """Combine seasonal and plant advice with fallbacks for unknown choices."""
    seasonal = SEASON_ADVICE.get(season, "No advice for this season.")
    plant = PLANT_ADVICE.get(plant_type, "No advice for this type of plant.")
    return f"{seasonal}\n{plant}"


def main():
    """Display the starter's summer and flower advice."""
    print(get_advice("summer", "flower"))


if __name__ == "__main__":
    main()
