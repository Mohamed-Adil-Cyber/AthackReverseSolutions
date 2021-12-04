We open the binary on radare to see it as assembly using VVV option on radare

![alt text](https://github.com/Mohamed-Adil-Cyber/AthackReverseSolutions/blob/main/Shellcode%20Devil/Images/Screenshot_0.jpg)

we see that it immediatly jumps to 4d at the begining so we go and check what is happening there

![alt text](https://github.com/Mohamed-Adil-Cyber/AthackReverseSolutions/blob/main/Shellcode%20Devil/Images/Screenshot_1.jpg)

we see that rdx points to a location in the file then takes whatever its ponting to up to 8 bytes and stores it in eax then points to a location after 20 (32) hex characters and takes 8 bytes and xor it to the first 8 bytes, rbx is then subtracted and the process is looped a number of times and the program ends.

so to simplify it choses a space that has 64 bytes and takes the first 32 byte and xors it with the last 32 byte

![alt text](https://github.com/Mohamed-Adil-Cyber/AthackReverseSolutions/blob/main/Shellcode%20Devil/Images/Screenshot_0.jpg)
we go back to the beginning of the code and notice that everything starting from D to 4D is not used which is exactly 64 


![alt text](https://github.com/Mohamed-Adil-Cyber/AthackReverseSolutions/blob/main/Shellcode%20Devil/Images/Screenshot_2.jpg)
we take the first 32 bytes


![alt text](https://github.com/Mohamed-Adil-Cyber/AthackReverseSolutions/blob/main/Shellcode%20Devil/Images/Screenshot_3.jpg)
and the last 32 bytes


![alt text](https://github.com/Mohamed-Adil-Cyber/AthackReverseSolutions/blob/main/Shellcode%20Devil/Images/Screenshot_4.jpg)
and xor them together 


![alt text](https://github.com/Mohamed-Adil-Cyber/AthackReverseSolutions/blob/main/Shellcode%20Devil/Images/Screenshot_5.jpg)
then convert to ascii and we got the flag which is AtHackCTF{FF00CEC3E746AA7F00FF0}

