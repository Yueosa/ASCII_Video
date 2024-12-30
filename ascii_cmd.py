import os
import time
import sys
import re
import shutil


def get_numeric_part(filename):
    """
    从文件名中提取数字部分，用于排序
    :param filename: 文件名
    :return: 提取的数字部分
    """
    match = re.search(r'(\d+)', filename)
    return int(match.group(0)) if match else -1


def get_terminal_size():
    """
    获取终端窗口大小
    :return: (width, height)
    """
    size = shutil.get_terminal_size()
    return size.columns, size.lines


def crop_frame(frame, width, height):
    """
    裁剪帧内容以适配终端大小
    :param frame: ASCII艺术帧
    :param width: 终端宽度
    :param height: 终端高度
    :return: 裁剪后的帧
    """
    lines = frame.splitlines()
    cropped_lines = [line[:width] for line in lines[:height]]
    return "\n".join(cropped_lines)


def center_frame(frame, width, height):
    """
    居中帧内容以适配终端大小
    :param frame: ASCII艺术帧
    :param width: 终端宽度
    :param height: 终端高度
    :return: 居中的帧
    """
    lines = frame.splitlines()
    frame_height = len(lines)
    frame_width = max(len(line) for line in lines) if lines else 0

    # 计算上下左右的填充
    vertical_padding = max((height - frame_height) // 2, 0)
    horizontal_padding = max((width - frame_width) // 2, 0)

    # 添加上下左右的填充
    padded_lines = [
        " " * horizontal_padding + line[:width - horizontal_padding] for line in lines
    ]
    empty_line = " " * width
    return (
        "\n" * vertical_padding
        + "\n".join(padded_lines)
        + "\n" * max(height - vertical_padding - frame_height, 0)
    )


def adapt_frame(frame, width, height):
    """
    适配帧内容以适配终端大小
    :param frame: ASCII艺术帧
    :param width: 终端宽度
    :param height: 终端高度
    :return: 适配后的帧
    """
    lines = frame.splitlines()
    frame_height = len(lines)
    frame_width = max(len(line) for line in lines) if lines else 0

    # 如果帧内容过大，裁剪
    if frame_width > width or frame_height > height:
        return crop_frame(frame, width, height)

    # 如果帧内容过小，居中
    return center_frame(frame, width, height)


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

    # 播放帧
    for frame in ascii_frames:
        width, height = get_terminal_size()  # 获取当前终端大小
        adapted_frame = adapt_frame(frame, width, height)  # 调整帧内容

        sys.stdout.write("\033[H\033[J")  # 光标移动到左上角并清屏
        sys.stdout.write(adapted_frame)
        sys.stdout.flush()
        time.sleep(frame_delay)


# 主程序
if __name__ == "__main__":
    ascii_dir = "./ascii_frames"
    play_ascii_frames(ascii_dir)
