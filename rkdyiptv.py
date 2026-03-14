#!/usr/bin/env python3
import os
import shutil
import time

os.system("clear")

width = shutil.get_terminal_size().columns

banner = [
"██████╗ ██╗  ██╗██████╗ ██╗   ██╗",
"██╔══██╗██║ ██╔╝██╔══██╗╚██╗ ██╔╝",
"██████╔╝█████╔╝ ██║  ██║ ╚████╔╝ ",
"██╔══██╗██╔═██╗ ██║  ██║  ╚██╔╝  ",
"██║  ██║██║  ██╗██████╔╝   ██║   ",
"╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝    ╚═╝   ",
"",
"        RKDYIPTV"
]

print("\033[92m")

for line in banner:
    print(line.center(width))

print("\033[0m")

time.sleep(1)

print("\n" + "✨ Welcome to RKDYIPTV ✨".center(width))
time.sleep(1)

print("\n" + "Thank you for using RKDYIPTV".center(width))
time.sleep(1)

print("\n" + "⚠ Script has been taken down.".center(width))

input("\n" + "Press Enter to exit...".center(width))
