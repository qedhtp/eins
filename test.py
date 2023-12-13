import subprocess
import platform

def get_screen_resolution():
    try:
        resolution_cmd = "xrandr | grep \* | cut -d' ' -f4"
        resolution_process = subprocess.Popen(resolution_cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        resolution, _ = resolution_process.communicate()
        width, height = map(int, resolution.decode().strip().split('x'))
        return width, height
    except Exception as e:
        print(f"Error getting screen resolution: {e}")
        return None

def open_terminals():
    system_platform = platform.system()

    if system_platform == 'Linux':
        resolution = get_screen_resolution()
        if resolution:
            width, height = resolution

            # 计算四个角的相对位置
            top_left = "0,0"
            top_right = f"{width},0"
            bottom_left = f"0,{height}"
            bottom_right = f"{width},{height}"

            # 打开四个终端
            subprocess.run(['gnome-terminal', '--geometry', f"80x24+{top_left}"], shell=True)
            subprocess.run(['gnome-terminal', '--geometry', f"80x24+{top_right}"], shell=True)
            subprocess.run(['gnome-terminal', '--geometry', f"80x24+{bottom_left}"], shell=True)
            subprocess.run(['gnome-terminal', '--geometry', f"80x24+{bottom_right}"], shell=True)
    else:
        print("Unsupported operating system")

if __name__ == "__main__":
    open_terminals()
