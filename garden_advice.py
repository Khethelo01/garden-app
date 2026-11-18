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
    season = season.strip().lower()
    plant_type = plant_type.strip().lower()
    seasonal = SEASON_ADVICE.get(season, "No advice for this season.")
    plant = PLANT_ADVICE.get(plant_type, "No advice for this type of plant.")
    return f"{seasonal}\n{plant}"


def read_choice(label, choices):
    """Prompt until the user enters a supported choice, ignoring case/spaces."""
    options = ", ".join(choices)
    while True:
        value = input(f"Choose {label} ({options}): ").strip().lower()
        if value in choices:
            return value
        print(f"Please choose one of: {options}.")


def main():
    """Ask for local season and plant type, then display the matching advice."""
    print("Garden advice")
    print("Choose your local season; advice is available for summer and winter.")
    # Ask for the local season rather than assuming a hemisphere from the month.
    try:
        season = read_choice("a season", SEASON_ADVICE)
        plant_type = read_choice("a plant type", PLANT_ADVICE)
    except (EOFError, KeyboardInterrupt):
        print("\nInput cancelled. No advice was generated.")
        return
    print("\n" + get_advice(season, plant_type))


if __name__ == "__main__":
    main()
