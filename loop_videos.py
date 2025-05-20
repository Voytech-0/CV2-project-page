import os
import cv2
import numpy as np

# Directory containing videos
INPUT_DIR = "static/videos"
OUTPUT_DIR = "static/videos_looped"

# Create output directory if it doesn't exist
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Supported video extensions
VIDEO_EXTENSIONS = [".mp4", ".avi", ".mov", ".mkv"]

def is_video_file(filename):
    return any(filename.lower().endswith(ext) for ext in VIDEO_EXTENSIONS)

def process_video(file_path, output_path):
    cap = cv2.VideoCapture(file_path)

    if not cap.isOpened():
        print(f"Failed to open {file_path}")
        return

    fps = int(cap.get(cv2.CAP_PROP_FPS))
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')

    # Read original frames
    frames = []
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        frames.append(frame)

    cap.release()

    # Create output video
    out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

    # Write original frames
    for frame in frames:
        out.write(frame)

    # Write reversed frames
    for frame in reversed(frames):
        out.write(frame)

    out.release()
    print(f"Processed: {output_path}")

def main():
    for filename in os.listdir(INPUT_DIR):
        if is_video_file(filename):
            input_path = os.path.join(INPUT_DIR, filename)
            output_filename = f"{os.path.splitext(filename)[0]}_extended.mp4"
            output_path = os.path.join(OUTPUT_DIR, output_filename)
            process_video(input_path, output_path)

if __name__ == "__main__":
    main()
