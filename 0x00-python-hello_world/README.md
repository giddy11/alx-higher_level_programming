The beginning of Python

General
Why Python programming is awesome
Who created Python
Who is Guido van Rossum
Where does the name ‘Python’ come from
What is the Zen of Python
How to use the Python interpreter
How to print text and variables using print
How to use strings
What are indexing and slicing in Python
What is the official Python coding style and how to check your code with pycodestyle


Python Scripts
Allowed editors: vi, vim, emacs
All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
All your files should end with a new line
The first line of all your files should be exactly #!/usr/bin/python3
A README.md file at the root of the repo, containing a description of the repository
A README.md file, at the root of the folder of this project, is mandatory
Your code should use the pycodestyle (version 2.8.*)
All your files must be executable
The length of your files will be tested using wc


More Info
Zen
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!


Quiz questions
Great! You've completed the quiz successfully! Keep going! (Hide quiz)
Question #0
What does this command line print?

>>> a = "Python is cool"
>>> print(a[7:-5])

nohtyP


on


is


Python


si

Question #1
What does this command line print?

>>> print("Holberton school")

“Holberton school”


Holberton


‘Holberton school’


Holberton school

Question #2
What does this command line print?

>>> a = "Python is cool"
>>> print(a[7:])

Python is


Python i


is cool


cool

Question #3
What does this command line print?

>>> print(f"{98} Battery street, {'San Francisco'}")

8 Battery street, San


“98 Battery street, San Francisco”


San Francisco Battery street, 98


98 Battery street, San Francisco

Question #4
Who created Python?


Julien Barbier


Yukihiro Matsumoto


Guido van Rossum

Question #5
What does this command line print?

>>> a = "Python is cool"
>>> print(a[:6])

Python


Pytho


is cool


Python is

Question #6
What does this command line print?

>>> a = "Python is cool"
>>> print(a[0:6])

Pytho


Python


Python is cool


Python is

Question #7
What does this command line print?

>>> print(f"{98} Battery street")

f"98 Battery street"


98 Battery street


8 Battery street


9 Battery street

Question #8
What does this command line print?

>>> a = "Python is cool"
>>> print(a[4])

n


P


h


o

Question #9
What does this command line print?

>>> a = "Python is cool"
>>> print(a[-2])

l


ol


Nothing


o


Tasks
0. Run Python file
mandatory
Score: 100.0% (Checks completed: 100.0%)
Write a Shell script that runs a Python script.

The Python file name will be saved in the environment variable $PYFILE


1. Run inline
mandatory
Score: 100.0% (Checks completed: 100.0%)
Write a Shell script that runs Python code.

The Python code will be saved in the environment variable $PYCODE


2. Hello, print
mandatory
Score: 100.0% (Checks completed: 100.0%)
Write a Python script that prints exactly "Programming is like building a multilingual puzzle, followed by a new line.
https://github.com/alx-tools/0x00.py/blob/master/3-print_number.py
https://realpython.com/python-f-strings/
Use the function print


4. Print float
mandatory
Score: 100.0% (Checks completed: 100.0%)
Complete the source code in order to print the float stored in the variable number with a precision of 2 digits.

You can find the source code here
https://github.com/alx-tools/0x00.py/blob/master/4-print_float.py
The output of the program should be:
Float:, followed by the float with only 2 digits
followed by a new line
You are not allowed to cast number to string
You have to use f-strings


5. Print string
mandatory
Score: 100.0% (Checks completed: 100.0%)
Complete this source code in order to print 3 times a string stored in the variable str, followed by its first 9 characters.
https://github.com/alx-tools/0x00.py/blob/master/5-print_string.py

You can find the source code here
https://github.com/alx-tools/0x00.py/blob/master/5-print_string.py
The output of the program should be:
3 times the value of str
followed by a new line
followed by the 9 first characters of str
followed by a new line
You are not allowed to use any loops or conditional statement
Your program should be maximum 5 lines long


6. Play with strings
mandatory
Score: 100.0% (Checks completed: 100.0%)
Complete this source code to print Welcome to Holberton School!

You can find the source code here
https://github.com/alx-tools/0x00.py/blob/master/6-concat.py
You are not allowed to use any loops or conditional statements.
You have to use the variables str1 and str2 in your new line of code
Your program should be exactly 5 lines long


7. Copy - Cut - Paste
mandatory
Score: 100.0% (Checks completed: 100.0%)
Complete this source code

You can find the source code here
https://github.com/alx-tools/0x00.py/blob/master/7-edges.py
You are not allowed to use any loops or conditional statements
Your program should be exactly 8 lines long
word_first_3 should contain the first 3 letters of the variable word
word_last_2 should contain the last 2 letters of the variable word
middle_word should contain the value of the variable word without the first and last letters


8. Create a new sentence
mandatory
Score: 100.0% (Checks completed: 100.0%)
Complete this source code to print object-oriented programming with Python, followed by a new line.

You can find the source code here
https://github.com/alx-tools/0x00.py/blob/master/8-concat_edges.py
You are not allowed to use any loops or conditional statements
Your program should be exactly 5 lines long
You are not allowed to create new variables
You are not allowed to use string literals



9. Easter Egg
mandatory
Score: 100.0% (Checks completed: 100.0%)
Write a Python script that prints “The Zen of Python”, by TimPeters, followed by a new line.

Your script should be maximum 98 characters long (please check with wc -m 9-easter_egg.py)


10. Linked list cycle
mandatory
Score: 0.0% (Checks completed: 0.0%)
Technical interview preparation:

You are not allowed to google anything
Whiteboard first
This task and all future technical interview prep tasks will include checks for the efficiency of your solution, i.e. is your solution’s runtime fast enough, does your solution require extra memory usage / mallocs, etc.
Write a function in C that checks if a singly linked list has a cycle in it.

Prototype: int check_cycle(listint_t *list);
Return: 0 if there is no cycle, 1 if there is a cycle
Requirements:

Only these functions are allowed: write, printf, putchar, puts, malloc, free



11. Hello, write
#advanced
Score: 100.0% (Checks completed: 100.0%)
Write a Python script that prints exactly and that piece of art is useful - Dora Korpar, 2015-10-19, followed by a new line.

Use the function write from the sys module
You are not allowed to use print
Your script should print to stderr
Your script should exit with the status code 1
guillaume@ubuntu:~/py/0x00$ ./100-write.py
and that piece of art is useful - Dora Korpar, 2015-10-19
guillaume@ubuntu:~/py/0x00$ echo $?
1
guillaume@ubuntu:~/py/0x00$ ./100-write.py 2> q
guillaume@ubuntu:~/py/0x00$ cat q
and that piece of art is useful - Dora Korpar, 2015-10-19
guillaume@ubuntu:~/py/0x00$ 



12. Compile
#advanced
Score: 100.0% (Checks completed: 100.0%)
Write a script that compiles a Python script file.

The Python file name will be stored in the environment variable $PYFILE

The output filename has to be $PYFILEc (ex: export PYFILE=my_main.py => output filename: my_main.pyc)

guillaume@ubuntu:~/py/0x00$ cat main.py 
#!/usr/bin/python3
print("Best School")

guillaume@ubuntu:~/py/0x00$ export PYFILE=main.py
guillaume@ubuntu:~/py/0x00$ ./101-compile
Compiling main.py ...
guillaume@ubuntu:~/py/0x00$ ls
101-compile  main.py  main.pyc
guillaume@ubuntu:~/py/0x00$ cat main.pyc | zgrep -c "Best School"
1
guillaume@ubuntu:~/py/0x00$ od -t x1 main.pyc # SYSTEM DEPENDANT => CAN BE DIFFERENT
0000000 ee 0c 0d 0a 91 26 3e 58 31 00 00 00 e3 00 00 00
0000020 00 00 00 00 00 00 00 00 00 02 00 00 00 40 00 00
0000040 00 73 0e 00 00 00 65 00 00 64 00 00 83 01 00 01
0000060 64 01 00 53 29 02 7a 10 48 6f 6c 62 65 72 74 6f
0000100 6e 20 53 63 68 6f 6f 6c 4e 29 01 da 05 70 72 69
0000120 6e 74 a9 00 72 02 00 00 00 72 02 00 00 00 fa 07
0000140 6d 61 69 6e 2e 70 79 da 08 3c 6d 6f 64 75 6c 65
0000160 3e 02 00 00 00 73 00 00 00 00
0000172
guillaume@ubuntu:~/py/0x00$ 



13. ByteCode -> Python #1
#advanced
Score: 100.0% (Checks completed: 100.0%)
Write the Python function def magic_calculation(a, b): that does exactly the same as the following Python bytecode:

  3           0 LOAD_CONST               1 (98)
              3 LOAD_FAST                0 (a)
              6 LOAD_FAST                1 (b)
              9 BINARY_POWER
             10 BINARY_ADD
             11 RETURN_VALUE
Tip: Python bytecode



