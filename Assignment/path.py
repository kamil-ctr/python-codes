import os

def find_image_path(image_name):
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
    for root, dirs, files in os.walk(desktop_path):
        if image_name in files:
            return os.path.join(root, image_name)
    return None

if __name__ == "__main__":
    image_name = "PHOTO-2024-09-07-11-18-02.jpg"
    image_path = find_image_path(image_name)
    if image_path:
        print(f"Image found at: {image_path}")
    else:
        print("Image not found.")
