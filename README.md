# RyPass

When main.py is executed, a folder called `gen_passwords` will be created if doesn't exist and will include all password instances

#### Video Demo:  <URL HERE>
#### Description:
That's a utility for generating complex passwords based on a given input.
First of all, an instance of Generator class is required, and running the init class method to create an instance of this class
which will handle taking input, and then through the generate method, there are four functions that create random letters, symbols and numbers
respectively based on user input, random seeds are chosen and inserted "randomly" into a new string, which will later be copied to clipboard
and written to a file in the root directory (gen_passwords), and you're able to generate multiple files, each one will be named according to
the number of files in the directory, so if password(0).txt and password(1).txt are existing, the next password's file will be written as password(3).txt, just adding one to the greatest number found in this case, 1.

# IMPORTANT!
please cd into src and run `main.py` from there so unexpected things won't occur
<br>
<br>
`cd src` 
<br>
<br>
`python main.py`

# Usage
`python main.py`

    

