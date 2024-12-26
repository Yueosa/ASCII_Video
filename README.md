# ASCII Video

**ASCII Video** 是一个将视频文件转换为 ASCII 艺术并在终端中播放的工具。它能够提取视频中的每一帧，将每一帧转换为 ASCII 艺术，并在终端中进行播放。这个项目使用 Python 和一些流行的库（如 OpenCV 和 Pillow）实现。

## 功能

- **提取视频帧**：从指定的视频文件中提取每一帧并保存为 JPG 格式。
- **转换为 ASCII 艺术**：将提取的每一帧转换为 ASCII 艺术，并保存为文本文件。
- **播放 ASCII 艺术**：按帧顺序将生成的 ASCII 艺术显示在终端中，模拟视频播放效果。

## 安装

1. 克隆该仓库：

    ```bash
    使用 https 克隆仓库：
    git clone https://github.com/Yueosa/ASCII_Video.git
    使用 ssh 克隆仓库：
    git clone git@github.com:Yueosa/ASCII_Video.git
    ```

2. 创建并激活虚拟环境（可选）：

    ```bash
    python -m venv venv
    source venv/bin/activate  # Linux/macOS
    venv\Scripts\activate  # Windows
    ```

3. 安装依赖库：

    ```bash
    pip install opencv-python pillow tqdm
    ```

## 使用

### 步骤 1: 提取视频帧

使用 `extract_frames` 函数从视频文件中提取帧。可以指定输出目录：

```python
extract_frames(video_path, output_dir)

    从视频中提取每一帧并保存为 jpg 格式
    :param video_path: 视频文件路径
    :param output_dir: 保存帧的输出目录
```

### 步骤 2: 将视频帧转换为 ASCII 艺术
使用 `convert_frames_to_ascii` 函数将提取的视频帧转换为 ASCII 艺术。可以指定输出目录：

```python
convert_frames_to_ascii(input_dir, output_dir, width=100):

    将指定目录下的所有帧文件(图片)转换为ASCII艺术并保存为文本文件
    :param input_dir: 输入目录，包含帧图片
    :param output_dir: 输出目录, 保存转换后的ASCII文本文件
    :param width: 输出ASCII艺术的宽度
    """
```

### 步骤 3: 播放 ASCII 艺术
使用 `play_ascii_frames` 函数播放 ASCII 艺术。可以指定播放速度：

```python
play_ascii_frames(ascii_dir, frame_delay=0.016):

    播放ASCII艺术帧文件，按数字顺序读取并显示
    :param ascii_dir: 存放ASCII帧的目录
    :param frame_delay: 帧与帧之间的延迟，控制播放速度
```

## 项目结构

```
ASCII_Video/
│
├── video/                # 输入视频文件
├── frames/               # 提取的视频帧
├── ascii_frames/         # 转换后的 ASCII 艺术文本文件
├── ASCII_VIDEO.py        # 主程序文件
├── ascii_cmd.py          # 播放程序文件
└── README.md             # 自述文件
```

## 贡献
欢迎提交 Issues 或 Pull Requests！你可以通过以下步骤贡献：

- **1.Fork 本仓库**
- **2.克隆到本地**
- **3.创建新分支并进行修改**
- **4.提交 Pull Reques**

## 许可证
该项目采用 MIT License 开源协议。
