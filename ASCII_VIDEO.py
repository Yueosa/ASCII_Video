import os
import cv2
import time
import sys
import re
from PIL import Image
from tqdm import tqdm


# ASCII字符集
ASCII_CHARS = " .:-=+*%@#"


def extract_frames(video_path, output_dir):
    """
    从视频中提取每一帧并保存为 jpg 格式
    :param video_path: 视频文件路径
    :param output_dir: 保存帧的输出目录
    """
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # 使用OpenCV读取视频
    cap = cv2.VideoCapture(video_path)
    frame_count = 0

    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    with tqdm(total=total_frames, desc="Extracting Frames", unit="frame") as pbar:
        while True:
            ret, frame = cap.read()
            if not ret:
                break

            frame_file = os.path.join(output_dir, f"frame_{frame_count:04d}.jpg")
            cv2.imwrite(frame_file, frame)
            frame_count += 1
            pbar.update(1)

    cap.release()
    print(f"Extracted {frame_count} frames from the video.")


def image_to_ascii(image_path, width=100):
    """
    将图像文件转换为ASCII艺术
    :param image_path: 图像文件路径
    :param width: 输出ASCII艺术的宽度
    :return: 转换后的ASCII艺术字符串
    """
    img = Image.open(image_path)
    aspect_ratio = img.height / img.width
    new_height = int(width * aspect_ratio * 0.55)
    img = img.resize((width, new_height))
    img = img.convert("L")

    pixels = img.getdata()
    ascii_str = "".join(ASCII_CHARS[min(pixel // 25, len(ASCII_CHARS) - 1)] for pixel in pixels)
    
    ascii_lines = [ascii_str[i:i+width] for i in range(0, len(ascii_str), width)]
    return "\n".join(ascii_lines)  # 返回完整的ASCII艺术


def convert_frames_to_ascii(input_dir, output_dir, width=100):
    """
    将指定目录下的所有帧文件(图片)转换为ASCII艺术并保存为文本文件
    :param input_dir: 输入目录，包含帧图片
    :param output_dir: 输出目录, 保存转换后的ASCII文本文件
    :param width: 输出ASCII艺术的宽度
    """
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    frame_files = sorted(os.listdir(input_dir), key=lambda x: get_numeric_part(x))
    
    total_frames = len(frame_files)
    
    with tqdm(total=total_frames, desc="Converting Frames to ASCII", unit="frame") as pbar:
        for frame_file in frame_files:
            input_path = os.path.join(input_dir, frame_file)
        
            if not frame_file.endswith(".jpg"):
                continue
        
            output_path = os.path.join(output_dir, frame_file.replace(".jpg", ".txt"))
        
            ascii_art = image_to_ascii(input_path, width)
        
            with open(output_path, "w") as f:
                f.write(ascii_art)
            
            pbar.update(1)
    
    print(f"Converted {total_frames} frames to ASCII art.")


if __name__ == "__main__":
    video_path = "./video/video.mp4"
    frames_dir = "./frames" 
    ascii_dir = "./ascii_frames"

    extract_frames(video_path, frames_dir)
    
    convert_frames_to_ascii(frames_dir, ascii_dir, width=100)
