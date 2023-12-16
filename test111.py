import subprocess
import platform

def get_screen_resolution():
    try:
        resolution_cmd = "xdpyinfo | grep dimensions | awk '{print $2}'"
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
            original_width, original_height = resolution

            # Calculate the new size for each terminal (half of the original size)
            terminal_width = original_width // 2
            terminal_height = original_height // 2

            # Open four terminals at different positions with the new size
            for i in range(2):
                for j in range(2):
                    position_x = i * terminal_width
                    position_y = j * terminal_height

                    subprocess.run(['gnome-terminal', '--geometry', f"{terminal_width}x{terminal_height}+{position_x}+{position_y}"])

    else:
        print("Unsupported operating system")

if __name__ == "__main__":
    open_terminals()
