# transcripts

Here we provide the code complementing our blog post.

This program was made for running on a windows computer with chrome installed.

To run this script, you first need to install a few things. You will need python 3, which you can install here: https://www.python.org/downloads/windows/.

Next you will need pip. Here you can find a guide on how to install pip on windows: https://www.geeksforgeeks.org/how-to-install-pip-on-windows/.

Now you can install selenium, a python library for browser automation. To do so, open the command prompt and type in the command: py -m pip install selenium

The last thing you need to add is a webdriver. As we are using Chrome, you have to install Chromium, which you can find here: https://sites.google.com/chromium.org/driver/.

After you have added all the things needed you can download the script transcripts.py from this repository. Open the command prompt and navigate to the file with the cd command. 
Then you can run the program with the command: py transcripts.py tadic

A Chrome window should open with the icty website. The program will take a few minutes, after which the window will close. The program will generate a new file called tadic.html,
which you can find in the same directory as transcripts.py. Instead of tadic, you can run the script with any icty case. An overview can be found here: https://www.icty.org/en/cases. 
To find the exact name, click on the case you are interested in and copy the name of the case from the url (eg: https://www.icty.org/en/case/aleksovski -> aleksovski).
