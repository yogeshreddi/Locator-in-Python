# Locator-in-Python
Write a command line application that takes a string and navigates the file system looking for either a file or directory with the name of the string that was passed. The output should be the absolute path, (full path) to the directory or file.

The arguments are as follows:

Root: This is the root directory to start looking. This is required.
String: This is the string to use to search for file or directory. This is required.

-f, --file: This will force the program to only list files. This is optional.

-d, --directory: This will force the program to only list directories. This is optional.

If neither –f or –d or their longnames are in the argument, then list both files and directories.

-m, --last-modified: The time the file/directory was last modified. This is optional.

The search string should be dynamic and allow *, ?, and ranges such as a-zA-Z. You should print the results in a nicelylaid format. You can decide how you want to do this. Example Call to your program:

python your_program_name.py –f C:\Users\%USERNAME% *.py
