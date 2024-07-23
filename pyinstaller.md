# PyInstaller Instructions
## Creating a new file
* In command line --> Write this command with the file you want packaged as an executable.
```bash
pyinstaller --onefile example_file.py
```
* Adding --noconsole ensures that no console window appears when you run the executable
```bash
pyinstaller --onefile --noconsole example_file.py
```

