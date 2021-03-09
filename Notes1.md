# QUICK REVISION NOTES

## 1. INTRODUCTION TO PROGRAMMING

### 1.1 What is Programming Language and Operating System and why do we need them?
A Programming Language is a set of predefined words that are combined into a program according to predefined rules(syntax). Programming languages are used to develop the application which helps in turn to get our task done. 

An Operating Systemis a software that allows a user to run other applications on a computing device. The main job of operating system is to manage computer’s software and hardware resources like I/O device, Network device, storage device etc. and to run the application on our system and resource allocation required for the same.
### 1.2 A brief introduction to computer memory
There are mainly two types of memory in computer:-
    1. Volatile Memory - Primary Memory - Temporary Storage - RAM, Cache, Register
   2. Non-volatile memory - Secondary Memory - Permanent Storage - HDD, SDD, Floppy, CD, Pen Drive

-> Every program runs into RAM. 
-> Secondary memory are used for permanent storage.
### 1.3 Types of Programming Languages
There are mainly two types of programming language.
    1. Low Level Programming Language
        I. Machine Level Language or Binary Code
        II. Assembly Language
    2. High Level Programming Language
        I. Based on purpose
            i. General Purpose PL
            ii. Special Purpose PL
        II. Based on converters used
            i. Compiled —> C/C++/Java/Python
            ii. Interpreted —> Perl/Java Script/Python
### 1.4 What is Source code, Byte code and Machine code in Python?
Source Code:- The code, written to develop the application. In python, (.-)file is source code.

Byte code:- A fixed set of instructions that represents all operations like arithmetic, comparison, memory related operations etc. The code generated after the compilation of source code. (.pyc) file is byte code. Byte code is system and platform independent. It is also called p-code, portable code or object code.

PVM:- Stands for Python Virtual Machine and is a software which comes with Python. PVM comes with Interpreter. 

Machine code:- The code generated after interpretation of byte code. It is system and platform dependent.
### 1.5 Type of Errors in Python
Error Handling is one of the most important feature of Python. It was main deciding factor in development of Python.
There are mainly two type of errors in Python:-
    I. Compile-time Error at compilation stage
    II. Run-time Error caught at run time or interpretation stage.

Syntax & Syntactical Errors:- Every Programming Language comes with a set of rules which defines that how the codes will be written and interpreted or compiled. These set of rules are called Syntax. Not following the rules may lead to errors which are called Syntax errors. In Python, at compilation stage we check for the syntax errors. If there are no syntax errors in your program then it will be compiled successfully and byte code will be generated. If there are some syntax error in your program then compilation will not happen and byte code will not be generated. Syntax Error happens when Python can’t understand what you are saying.


Run Time Errors:- Run time error happens when Python can understand what you are saying but runs into problem while running your instructions. To find the list of all run time error you may execute the below code:-


---> print(dir(“__builtins__”))


We can handle runtime errors using exception handling concept in Python unlike syntax errors which has to be rectified before compilation. Run time errors may cause partial implementation of your code.

[Reference:-]
1. https://cscircles.cemc.uwaterloo.ca/1e-errors/
### 1.6 Compiled Languages vs Interpreted Languages
I. Compiled languages needs compiler to translate the code whereas Interpreted languages needs interpreter to translate the code from one form to another.

II. Compiler & Interpreter both are translator and are computer programs.

III. Compiler translates the whole code from one form to another form all at once while interpreter is instruction by instruction execution.

IV. In Python, Compiler is used to translate Source code to byte code whereas Interpreter is used to translate the Byte code to Machine code.

V. All Syntactical errors are caught at compilation stage in Python whereas all run time errors are caught at interpretation stage.

NOTE:- Originally, Python is Interpreted Language. But over the time, Python is made compiled and Interpreted both as python has established itself as full fledged programming language and is acceptable across wide area of application.


[References:-]
1.https://en.wikipedia.org/wiki/Interpreted_language
2.https://www.freecodecamp.org/news/compiled-versus-interpreted-languages/
### 1.7 Why do we need translator?
Computer's hardware are electronic devices and they can not understand human language, rather they communicate with each other with the help of signals. Signals are nothing but binary code and is completely low level language. To translate High level languages in human readable format to machine readable format(binary code), we need translators. 
### 1.8 Why do we need Byte code?
Byte code are also called object code or p-code or portable code which may be be directly shipped to your client. As well as it is platform independent so it can run on any platform. Which makes service provider's and developer's life easy as they do not have to write the code for the same application to be used on different platform.
### 1.9 Why Python is compiled and interpreted both? Can’t we make it either compiled or interpreted?
Traditional programming languages like C or C++ were compiled languages. If you execute any source code in C or C++, it  first creates an executable file which is platform dependent and then you run this file to get the output on that particular platform.

Source Code —> Compiler —> Executable Code(.exe file) —> Output


You can see here that the intermediate code which are generated is not platform independent. But remember that the Source code written in these languages are portable.

So, to counter this problem, languages like Java and Python were developed which are first compiled to object code or Byte code or p-code(portable code). These object codes are completely platform independent. Now when you move this object code to other platform then you need to translate it to machine code. For translation at this stage, you may either use compiler or interpreter, any translator which again translates the byte code to machine code. For Instance, Java, PyPI, JPython uses JIT compiler, where CPython uses interpreter.

Source Code —> Compiler —> Byte Code —> Interpreter or JIT compiler(PVM/JVM) —> Machine Code —> Output 

So basically, we may say that to bridge the gap between portable programming languages and platform independent programming languages we came up with this idea to have two translators. First time it is used to generate shippable code and second time it is used to convert the byte code to machine code.


[References:-]
1.https://en.wikipedia.org/wiki/Python_(programming_language)
2.https://www.geeksforgeeks.org/history-of-python/
3.http://effbot.org/pyfaq/why-was-python-created-in-the-first-place.htm
4.https://www.artima.com/intv/python.html
## 2. WHAT IS PYTHON?
Python is General purpose, High level programming language.
### 2.1 What are some good features of Python?
1.Simple & easy to learn:-Python is one of the simplest language ever. Syntaxes are simple, easy to remember and quite expressive. When it comes to learning, it has been found that the learning curve for python is quite steeper compared to other programming languages.


Sample Program in Java to add two numbers:-
public class add{
    public static void main(string[]args){
        int a = 10;
        int b = 20;
        int c = a+b;
        System.out.println(c);
    }
}

Sample Program in Python to add two numbers:-
a = 10
b = 20
c = a+b
print(c)


2.Most expressive language:-Being one of the most expressive language is easy to write the code in fewer lines, which leads to less cluttered program, faster execution and easy to debug and maintain.

3.Freeware and open source:-Python being freeware, you don’t have to spend on licensing. And since it is open source so its original source code is freely available and can be redistributed and modifiable.


4.Compiled and Interpreted both:- Originally, Python was developed to bridge the gap between C and shell scripting and also include the feature of exception handling from ABC language. So we can say that, initially Python was interpreted language. But later it was made compiled and interpreted both.

Generally, the steps involved in execution of any python program are - 
### 2.2 How a python program runs on our system?
Source code ---> compiler ---> byte code ---> interpreter(PVM) ---> Machine code ---> Hardware ---> output

In the above flow diagram, compiler is responsible to compile the source code. In the compilation stage all the syntactical errors are checked whereas interpreter is responsible to interpret the byte code and check the run time error in this stage. 
Compiler and interpreter both are translator. Compiler translates the source code to byte code(.pyc file) all at once whereas interpreter translates byte code to machine code one instruction at a time which interacts with hardware to give the final output.


Few important commands:-
1.python File_Name.py —> To run the file
2.python -m py_compile File_Name.py —> To compile the file
3.python -m dis File_Name.py —> To see the byte code.
4.python File_Name.cpython-38.pyc —> To run the compiled code.


5.Portable and Platform Independent:- Python is portable and platform independent both. Source code is portable whereas byte code(.pyc file) is platform independent. C is portable but not platform independent.

6.Dynamically typed programming language:- In python, everything is an object. Objects get stored in the heap area and it’s memory address is referenced by the variable or name with which it is binded. Unlike other programming languages, In python, memory location does not work like a container rather it works on reference model. No need to specify the data type explicitly in python.

7.Extensible and Embedded both - Extensibility - Extending the code from other programming languages into Python code. Embedded - Embedding Python code to other programming languages code.


8.Batteries included:- Python comes with huge library support required for full usability.


9.Community Support:- Huge Python community support available for beginner, intermediate and advance level programmers.
10.CBSE 10th standard syllabus has Python now.
11.The growth and acceptance python has shown over the years, is exceptional. Click Here for more details.

[References:-]
1.https://en.wikipedia.org/wiki/Python_(programming_language) 
### 2.3 Garbage Collection in Python
Python supports automatic garbage collection. It uses a combination of reference counting and cycle-detecting garbage collector for memory management an optimisation. gc module in python stands for garbage collector which runs from time to time and which ever object’s reference count reaches to zero, that gets garbage collected automatically. As a user you are not allowed to interfere in memory management. It is task of the PVM to manage the memory. Yes, but if you want to check whether gc module is enabled or disabled or if you want to enable or disable it then you may use it like below:-

```python
import gc
print(dir(gc),'\n')
print(gc.isenabled(),'\n')
gc.disable()
print(gc.isenabled(),'\n')
gc.enable()
print(gc.isenabled(),'\n')
```

    ['DEBUG_COLLECTABLE', 'DEBUG_LEAK', 'DEBUG_SAVEALL', 'DEBUG_STATS', 'DEBUG_UNCOLLECTABLE', '__doc__', '__loader__', '__name__', '__package__', '__spec__', 'callbacks', 'collect', 'disable', 'enable', 'freeze', 'garbage', 'get_count', 'get_debug', 'get_freeze_count', 'get_objects', 'get_referents', 'get_referrers', 'get_stats', 'get_threshold', 'is_tracked', 'isenabled', 'set_debug', 'set_threshold', 'unfreeze'] 
    
    True 
    
    False 
    
    True 
    


### 2.4 Different Flavours of Python
There are different flavours or implementation of python are available. Out of which the most common are:-

 1.Cpython:- C implementation of Python, developed to run C application on PVM, which was designed using C.
 2.Jython:- Java implementation of Python, developed to run Java application on PVM,which was designed using Java.
 3.PyPI:- Python implementation of Python. Implements JIT compiler, to improve the performance of python app.
 4.Ruby Python:- Ruby implementation of Python and was developed to run the Ruby application.
 5.Stackless Python:- Was developed to implement concurrency in Python.
 6.Anaconda Python:- Was developed to handle and process the big data.
## 3. COMPONENTS OF PYTHON
1.Literals
2.Constants
3.Identifiers
4.Variables
5.Reserved words
6.Expressions
7.Statements
8.Comments
9.Suites
10.Block and identation
### 3.1 Literals in Python
---> a = 15

-Data or constant value stored in a variable.
-In the above example, constant value ’15’ is stored in a variable ’a’. 15, here is literal.
-5 is integer value so it is also called integer literal.

Python supports different type of literals:-
1.Numeric Literals
	- Integer Literals - 200, -15
	- Binary Literals - 0b1010
	- Octal Literals - 0o12
	- Hexadecimal Literals - 0xa
	- Float Literals - 10.20, -20.6
	- Complex Literals - 10+20j, 10-20j
    
2.Boolean Literals
	- True, False
    
3.Special Literal
	1. None
    
4.String Literals
	1. Sequence of characters enclosed between single quotation, double quotation or triple quotation.
### 3.2 Identifiers in Python
-A name given to a variable, function, class or object.
-Allowed Characters in Python:-2. Identifiers in Python:-
	- Numbers - 0-9
	- Underscore - (_)
	- Alphabets Capital(A to Z) and small (a to z)
-Not Allowed:-
	- Special Symbols are not allowed - ($,#,@)
-Rules to define an Identifier:-
	- Identifier should not start with a number.
	- Identifiers are case sensitive.
	- Never use reserved words as identifier.
	- Not recommended to take lengthy identifier.
	- Identifier starting with _ - Private
	- Identifier starting with __ - Strongly Private
	- Identifier starting and ending with __ - Language defined special identifier
### 3.3 Variables in Python
-A variable in python is a name which may change the data associated with it over time in a program as and when required.
-Rules to define a variable is same as that of an identifier.
-It is just a name which is used to create a reference for the data or object associated with in a given program.
-Variable always refers to the memory location in heap where the data associated with it is stored.
-Once user changes the data associated with a variable then the memory address of the variable also changes.
-Variable are used to store the data in the memory and pass them to processor to process the data.
### 3.4 Constants in Python
-A constant value is similar to variable with one exception that it can not be changed once it is set.
-In Python, You may change the value associated with a constant.
-So, how constant is different from variable in Python:-
	- Constants in Python should follow the same rule used to define an identifier.
	- Constants in Python should use only capital letter.
	- Do not use generic name like NUM, you may use MAX_NUM or MIN_NUM.
	- Use a different  “constant.py” file to define all of your constants in your application and use them by importing this module into your main module.
### 3.5 Reserved words in Python
-Words with special meaning and task associated with it.
-There are total 35 reserved words in python.
-There are two types of reserved words:-
	- Reserved Literals:- True, False, None
	- Keywords:- Reserved words associated with some functionality. Apart from reserved literals, all reserved words are keywords.
-All reserved words contains only alphabet characters.
-All keywords contains only lowercase letters.

```python
import keyword
print(keyword.kwlist)
```

    ['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']


### 3.6 Comments in Python
-Writing comments in python is a very good programming practice.
-Writing comments in your program helps your peer coder to understand the reason of including the part of your code in your program.
-To create a single line comment we use #.
-Multiline comments are written inside triple quotation.
-Triple quotations are also used for writing the doctoring.
### 3.7 Expressions in Python
-An expression is a combination of values, variables, operators and call to functions.
-Expressions needs to be evaluated.
-If you use print function for an expression then it evaluates the expressions and prints the result.
-Expression generally evaluates to a value, which is why expression are written on the right hand side in an assignment statement.
-A single value itself is a simple expression.
### 3.8 Statements in Python
-Instructions written in the source code for execution are called statements.
-Different types of statements in python are:-
	- Assignment Statements
	- Compound Assignment Statements
	- Conditional statements
	- Loop Statements
	- Statements in python cam be extended to one or more lines using parenthesis(), braces{}, square brackets[], semi colon ;, continuation character \. 
### 3.9 Blocks or suites and indentation in Python
-A combination of statements in python is called block or suites.
-In other programming languages like C, C++, Java we use flower brackets to make a block in python.
-We use whitespaces to make indentation and indentations are used to make block or suite in python.
### 3.10 Escape sequence
1 ---> \ ---> Using this you may write a single line string into multi line string.

2 ---> \\ ---> To print \

3 ---> \n ---> New line

4 ---> \t ---> Horizantal tab

5 ---> \v ---> Vertical tab

6 ---> \' ---> To consider single quote(‘) as string character

7 ---> \'' ---> To consider double quote(") as string character
## 4. ZEN OF PYTHON


```python
import this
```

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


## 5. FUNDAMENTAL DATATYPES
---> int:
  Whole number without decimal point is integer ---> decimal->(int(10)),binary->(bin(0b)),octal->(oct(0o)),hexa->   (hex(0x))

---> float:
  any number with decimal point is a float ---> print(float(10))
    
---> complex:
  combination of real and imaginary part ---> 6+12j --> 6 is real part & 12j is imaginary part & j is imaginary value          

---> string:
  combination of characters kept inside quote-->print('python class')& print("python's class")& print('''python's   & "java"''')
    
---> boolean:
  represented by True or False (1 & 0) --> every thing other than 0 is True, 0 and empty string is False
    
---> None:
  it represents null/no value, null is not same as 0, It can be added anywere for future changes, ID of null is     same everywere.

## 6. SEQUENCE, INDEXING, SLICING, CONCATENATION AND REPETITION
---> Sequence:
   Sequence is a ordered collection of elements --> string,list,tuple,byte,bytearray,range.
   Indexing and slicing is allowed.

---> Index:
   Index is the represent of position of the element in python. Python allows both positive and negative index
           
                                           -6  -5  -4  -3  -2  -1
     Negative index (right to left)     <--------------------------    starts from -1
                                            p   y   t   h   o   n
     Positive index (left to right)     --------------------------->   starts from 0
                                            0   1   2   3   4   5
        
---> Indexing:
   Indexing is a concept of accessing single element from list. only one element can be accessed at a time.
     syntax :
             --> list_name[index_number] --> to access the element
             --> list_name.index('element',start,stop) --> to access the index of first occurance of element

---> Slicing:
   Slicing is a concept of accessing multiple element from list at a time.
     syntax :
            --> list_name[start:stop:step] --> to access multiple elements
                  start --> position to start slicing , default = 0
                  stop  --> position one more than were we want to end slicing, default = length of the string
                  step  --> step of slicing , default = 1.
                     step = 1  --> slices from left to right.
                     step = -1 --> slices from right to left.

---> Concatenation:
   Process of combining two sequence of same datatype. print('python' + ' ' + 'is awesome')
    
---> Repetition:
   It is the process of repeating a string multiple times. It should have one string and one integer datatype.
     ex: print('python is cool, '*3)
## 7. DERIVED DATATYPES
---> list:
       Collection of hetrogeneous elements written inside the square bracket --> [20,{30:40},(56,96)]
       It is a mutable datatype and a sequence so indexing and slicing is possible.
       list_name.append('element') ---> to add element at the end of the list.
       list_name.remove('element') ---> to remove the element from the list.

    
---> tuple:
       Collection of ordered and immutable data written inside round brackets. --> (20,{30:40},(56,96))
       It is sequence so indexing and slicing is possible.  
    
---> set:
       Collection of unordered unique elements written inside curly brackets --> {10,20,30,40}
       Set is mutable but it wont allow mutable datatype as element.  
       It is not a sequence so indexing and slicing is not possible.
       Set doesnot allow to duplicate elements inside it .
       set_name.add('immutable_element') --> to add element inside the set.
       set_name.remove('immutable_element') --> to remove element from the set. 

---> frozenset:
       Collection of elements written inside round brackets with prefix 'frozenset' --> frozenset({10,20,30,40})
       frozenset is immutable datatype. Indexing and slicing is not possible.

---> dictionary:
       Collection of unordered mutable combination of key-value pair written inside curly brackets --> {1:10,2:20,3:30}
       Keys can't be duplicated and it doesnot allow mutable datatypes as key.
       Values can be duplicated and it allows mutable datatype as values.
       dict_name.update({key:value}) --> adds a pair to the end of dictionary.
       dict_name.pop(key,'return_this_if_key_not_found') --> removes the element with specified key.
       dict_name.popitem() --> removes the last item from the dictionary.  
    
---> range:
       Creates a sequence of numbers based in pattern.
         Syntax :
                  range(start,stop,step)
                  range(stop) ---> stop = (n-1)
       range can be wraped in list,tuple,set to get range in particular datatype.

---> byte and bytearray:
       They are used to store images,pdf or soundclips.
       allowed characters are 0-256.
         byte --> immutable --> print(bytes([10,20,30]))
         bytearrray --> mutable --> print(bytearray([10,20,30]))

### preparing the rest .......
