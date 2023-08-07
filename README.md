# Create your own processes
You can create your own automation process with the template by choosing the template with ```cd Template```. From there, you can alter the code to do tasks to your own likings. 
To find the coordination of your mouse:

For the template to work:
- First install python from this link: https://www.python.org/downloads/
- Make sure you have added this to your environmental path:
    - Search "Edit the system environment variables" (you'll have to add yourself to the admin to make changes)
    - Go to your environmental variables and select the one that begins with "PATH".
    - Click on Edit.
    - Click on NEW.
    - Type in this for your new path ```C:\Users\YOURUSERNAME\AppData\Local\Programs\Python\Python311```
    - Click okay.
    - Kill your terminal.
    - Restart your computer.
- Choose your IDLE. I use VS Code, however, you can use command prompt that's already installed in windows by default.
- If you do not want to use the template and you want to use Command Prompt to create a new file, in your terminal type in ```notepad```. If you're using other IDLE, simply start typing in a new file.
- Otherwise, if you want to use the template:
    - On your terminal, type in ```git clone https://github.com/cindypangs/SLBPublicAutomationTemplate.git```
    - After this, type in ```cd SLBPublicAutomationTemplate```
    - If you're using Command Prompt, type in ```notepad template.py``` and you'll see the template file.
    - Save this on your local desktop and alter it. DO NOT ALTER IT STRAIGHTAWAY. You must first save it locally to ensure this template does not get changed for others.

  Getting the coordinates of your mouse:
- Open a new terminal and type in ```python``` or ```py```.
- Type in ```import pyautogui``` to import the library.
- Type in ```pyautogui.position()``` and move your mouse to the desired position before executing the code.
- In the terminal you should be able to see the corrdination in (x,y) formation of your mouse.
- Replace this number with the (x,y) coordinates in the template.
