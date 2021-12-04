Firstly we check what linkers does the exe have to see if we can decompile the code

![alt text](https://github.com/Mohamed-Adil-Cyber/AthackReverseSolutions/blob/main/Clippy2/images/Screenshot_1.jpg)

we see that it has a dot net linker meaning that we can compile it back to c# and visual basic 
we use dns spy to decompile the code

we see that its taking its input from the clipboard and placing it inside a function

to simplify what the function is doing an array named array is created and the xor of first and second character in our input is compared to the second character in the array
then compares the xor of the third and second charcter with the third in the array and so on

so I created a z3 solver script to output the solution as a decimal
