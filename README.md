# Keylogger Project

[ibaiba2112][https://github.com/ibaiba2112]

## Description
This project is an educational keylogger designed for security research and ethical hacking purposes. This is still a work in progress and I am trying to learn as much as I can

## Disclaimer
This project is for educational purposes only. I do not condone any illegal activities or misuse of this software. Use it responsibly and only with the explicit permission of the owner of the system you are testing.

<hr>

## Setup
### Script
The script is relatively simple, The documentation on pypi.org give very in-depth and detailed description for use of the pynput library. Link to documentation --> (https://pypi.org/project/pynput/)

### Pathing 
I initially set up the script where it would write to the file "file_write.txt" within the project but I changed the path to the file with same name except on my desktop, I will add another version where it goes directly to file in the same project folder
I haven't made a path version for Windows yet so it only it works with Mac

### Pyinstaller
I wanted to make the script fit more in a real life setting so I used pyinstaller to package the script into a single executable file, You can find the pyinstaller instructions in the pyinstaller.md file.

## Use
* You can either run the program as normal it in vscode or find the executable file and run it, you can find that file in the dist folder in this project
* Type anything, I provided "text_input.txt" for your ease of use but anywhere works really
* Press esc when finished
* In your "file_write.txt" file, you should see the copied text from your keyboard

## Notice
You will be asked to allow accessability on your Mac for certain files and programs, mainly your executable file.








