import os
import time
import sys
import re


def get_numeric_part(filename):
    """
    从文件名中提取数字部分，用于排序
    :param filename: 文件名
    :return: 提取的数字部分
    """
    match = re.search(r'(\d+)', filename)
    return int(match.group(0)) if match else -1


def play_ascii_frames(ascii_dir, frame_delay=0.016):
    """
    播放ASCII艺术帧文件，按数字顺序读取并显示
    :param ascii_dir: 存放ASCII帧的目录
    :param frame_delay: 帧与帧之间的延迟，控制播放速度
    """
    frames = sorted(os.listdir(ascii_dir), key=get_numeric_part)
    
    ascii_frames = []
    for frame_file in frames:
        frame_path = os.path.join(ascii_dir, frame_file)
        with open(frame_path, "r") as f:
            ascii_frames.append(f.read())
    
    for frame in ascii_frames:
        sys.stdout.write(frame)
        sys.stdout.flush()
        time.sleep(frame_delay)


# 主程序
if __name__ == "__main__":
    ascii_dir = "./ascii_frames"
    play_ascii_frames(ascii_dir)
