We first try and see what the program is doing 

![alt text](https://github.com/Mohamed-Adil-Cyber/AthackReverseSolutions/blob/main/Authorize/images/Screenshot_0.jpg)

the program wants two inputs as arguments and will write "You cannot access me with this password" when the input is wrong and "Give me the username and the password" when there is no input. 

Let see what functions decides if the input is wrong or correct


we open ida and search for the sring "password" assuming that it should be in the function that decides if the input is wrong or correct

![alt text](https://github.com/Mohamed-Adil-Cyber/AthackReverseSolutions/blob/main/Authorize/images/Screenshot_1.jpg)
![alt text](https://github.com/Mohamed-Adil-Cyber/AthackReverseSolutions/blob/main/Authorize/images/Screenshot_2.jpg)
![alt text](https://github.com/Mohamed-Adil-Cyber/AthackReverseSolutions/blob/main/Authorize/images/Screenshot_3.jpg)

we see that the function has 4 outputs with only one of them being correct and outputs the flag, the flag is based on out input. so we have to understand the correct input

![alt text](https://github.com/Mohamed-Adil-Cyber/AthackReverseSolutions/blob/main/Authorize/images/Screenshot_4.jpg)

we see that the function takes the second and checks if its length is 16
then takes the first argument and check if its length 8
then finally checks if the second argument is equal to 95295a20f4a48485


![alt text](https://github.com/Mohamed-Adil-Cyber/AthackReverseSolutions/blob/main/Authorize/images/Screenshot_5.jpg)

after that the function calls another function to decide the username

![alt text](https://github.com/Mohamed-Adil-Cyber/AthackReverseSolutions/blob/main/Authorize/images/Screenshot_6.jpg)

the function loops through an algorithm and randomize the username based on the static seed of 1337. Because the seed is static that means the output is static. we go through the loop to see the output and find that the username is s3cur1ty 


![alt text](https://github.com/Mohamed-Adil-Cyber/AthackReverseSolutions/blob/main/Authorize/images/Screenshot_7.jpg)

meaning that the correct input is s3cur1ty 95295a20f4a48485 giving us the flag 
AtHackCTF{s3cur1ty_95295a20f4a48485}


