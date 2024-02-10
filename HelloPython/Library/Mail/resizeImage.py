from PIL import Image
import os

def should_resize(input_path, max_size_kb=100):
    size_kb = os.path.getsize(input_path) / 1024
    return size_kb > max_size_kb

def resize_and_save(input_path, output_folder, target_size_kb=100, quality=85):
    if should_resize(input_path, target_size_kb):
        image = Image.open(input_path)
        rgb_image = image.convert('RGB')

        # Kích thước mới để giữ dung lượng dưới ngưỡng target_size_kb
        new_size_kb = target_size_kb * 1024
        factor = (new_size_kb / os.path.getsize(input_path)) ** 0.5

        width, height = rgb_image.size
        new_width = int(width * factor)
        new_height = int(height * factor)

        resized_image = rgb_image.resize((new_width, new_height))
        output_path = os.path.join(output_folder, os.path.basename(input_path))
        resized_image.save(output_path, quality=quality)

if __name__ == "__main__":
    input_folder = "/home/thanh/code-server/config/PythonProject/DjangoWeb/static/home/images/artical"
    output_folder = "/home/thanh/code-server/config/PythonProject/DjangoWeb/static/home/images/artical"

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        if filename.endswith(('.jpg', '.jpeg')):
            input_path = os.path.join(input_folder, filename)
            resize_and_save(input_path, input_folder)
