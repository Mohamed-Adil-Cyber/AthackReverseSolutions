Firstly we check what linkers does the exe have to see if we can decompile the code

![alt text](https://github.com/Mohamed-Adil-Cyber/AthackReverseSolutions/blob/main/Clippy2/images/Screenshot_1.jpg)

we see that it has a dot net linker meaning that we can compile it back to c# and visual basic 
we use dns spy to decompile the code

![alt text](https://github.com/Mohamed-Adil-Cyber/AthackReverseSolutions/blob/main/Clippy2/images/Screenshot_2.jpg)


we see that its taking its input from the clipboard and placing it inside a function

![alt text](https://github.com/Mohamed-Adil-Cyber/AthackReverseSolutions/blob/main/Clippy2/images/Screenshot_3.jpg)
![alt text](https://github.com/Mohamed-Adil-Cyber/AthackReverseSolutions/blob/main/Clippy2/images/Screenshot_4.jpg)

to simplify what the function is doing an array named array is created and the xor of first and second character in our input is compared to the second character in the array
then compares the xor of the third and second charcter with the third in the array and so on

![alt text](https://github.com/Mohamed-Adil-Cyber/AthackReverseSolutions/blob/main/Clippy2/images/Screenshot_5.jpg)

so I created a z3 solver script to output the solution after the second character

![alt text](https://github.com/Mohamed-Adil-Cyber/AthackReverseSolutions/blob/main/Clippy2/images/Screenshot_6.jpg)

flag is AtHackCTF{w0w_cl1ppy_t4ugh7_u_d0t_n3t_spy1ng}
