import os
import json

# Root images folder
IMAGE_DIR = "images"

# Output JSON file
OUTPUT_JSON = "cars.json"

cars = []

for car_folder in os.listdir(IMAGE_DIR):
    car_path = os.path.join(IMAGE_DIR, car_folder)

    if os.path.isdir(car_path):
        images = []

        for file in os.listdir(car_path):
            # Handle .jfif -> .jpg rename
            if file.lower().endswith(".jfif"):
                old = os.path.join(car_path, file)
                new = os.path.join(car_path, file.rsplit(".", 1)[0] + ".jpg")
                os.rename(old, new)
                file = os.path.basename(new)  # update name

            # Only allow valid image formats
            if file.lower().endswith((".jpg", ".jpeg", ".png", ".gif", ".webp")):
                images.append(f"{IMAGE_DIR}/{car_folder}/{file}")

        if images:
            cars.append({
                "name": car_folder.capitalize(),
                "images": images
            })

# Write JSON
with open(OUTPUT_JSON, "w", encoding="utf-8") as f:
    json.dump(cars, f, indent=2)

print(f"✅ Generated {OUTPUT_JSON} with {len(cars)} cars")
