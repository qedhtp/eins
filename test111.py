import subprocess

# 示例命令：打开带有指定几何参数的 gnome-terminal
command = ["gnome-terminal", "--geometry", "94x19+0+0"]

# 使用subprocess.run运行命令
result = subprocess.run(command)

# 打印命令的返回码
print("返回码：", result.returncode)