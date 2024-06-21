import os
from PIL import Image
import pillow_heif
path = r"/Users/williamrae/Desktop/Lego-Scanner/Dataset/Test/Red"

def convert_heic_to_png(input_path, output_path=None):
    # If no output path is provided, replace the original file
    if output_path is None:
        output_path = os.path.splitext(input_path)[0] + '.png'
    
    # Read the HEIC file
    heif_file = pillow_heif.read_heif(input_path)
    
    # Convert to PIL Image
    image = Image.frombytes(
        heif_file.mode, 
        heif_file.size, 
        heif_file.data,
        "raw",
        heif_file.mode,
        heif_file.stride,
    )
    
    # Save as PNG
    image.save(output_path, 'PNG')
    
    # If we're replacing the original file, remove the HEIC file
    if output_path == os.path.splitext(input_path)[0] + '.png':
        os.remove(input_path)

def bulk_convert(directory):
    for filename in os.listdir(directory):
        if filename.lower().endswith('.heic'):
            input_path = os.path.join(directory, filename)
            convert_heic_to_png(input_path)
            print(f"Converted {filename} to PNG")

if __name__ == "__main__":
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python script.py <file_or_directory>")
        sys.exit(1)
    
    path = sys.argv[1]
    
    if os.path.isfile(path):
        convert_heic_to_png(path)
        print(f"Converted {path} to PNG")
    elif os.path.isdir(path):
        bulk_convert(path)
    else:
        print(f"Error: {path} is not a valid file or directory")