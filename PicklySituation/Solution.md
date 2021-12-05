the program is surprisingly a python script this time and not an exe so lets see what the code is doing

![alt text](https://github.com/Mohamed-Adil-Cyber/AthackReverseSolutions/blob/main/PicklySituation/images/Screenshot_1.jpg)

the code is turned into a character stream using pickle and encoded with base 64 and we run it the code works normally on python 3.6 which means the encoded part includes "exec" to run the string

so firstly we take the base 64 string and and decode it without the pickle

![alt text](https://github.com/Mohamed-Adil-Cyber/AthackReverseSolutions/blob/main/PicklySituation/images/Screenshot_2.jpg)
![alt text](https://github.com/Mohamed-Adil-Cyber/AthackReverseSolutions/blob/main/PicklySituation/images/Screenshot_3.jpg)
we find exec as expected in the encoded script and more encoded base 64 script but more importantly we find marshall library 

what is marshall library? marshall is used to run python compiled files and scripts.
so the encoded script is python compiled file. Lets deompile and check

![alt text](https://github.com/Mohamed-Adil-Cyber/AthackReverseSolutions/blob/main/PicklySituation/images/Screenshot_4.jpg)

as expected its a python compiled, what we can do now is use marhsall and dis library to dissasble the script and write as python bytecode

![alt text](https://github.com/Mohamed-Adil-Cyber/AthackReverseSolutions/blob/main/PicklySituation/images/Screenshot_5.jpg)
![alt text](https://github.com/Mohamed-Adil-Cyber/AthackReverseSolutions/blob/main/PicklySituation/images/Screenshot_6.jpg)
![alt text](https://github.com/Mohamed-Adil-Cyber/AthackReverseSolutions/blob/main/PicklySituation/images/Screenshot_7.jpg)
![alt text](https://github.com/Mohamed-Adil-Cyber/AthackReverseSolutions/blob/main/PicklySituation/images/Screenshot_8.jpg)

now we have it as python bytecode we can now manually translate it to a python scirpt

the byte code is taking input and storing it in x then creating an array called flag and fills it with numbers

the code then creates a variable key and has its value as "ABRAXUS" then uses key and xors the input and checks if its equal the flag array 

here is my interpretation of the code

![alt text](https://github.com/Mohamed-Adil-Cyber/AthackReverseSolutions/blob/main/PicklySituation/images/Screenshot_9.jpg)

we just have to xor the key with the flag array and we get the flag , here is a script I made to solve it

![alt text](https://github.com/Mohamed-Adil-Cyber/AthackReverseSolutions/blob/main/PicklySituation/images/Screenshot_10.jpg)


and we get the flag which is AtHackCTF{w0wza_p1ckl3s_4r3_c3w1!}
