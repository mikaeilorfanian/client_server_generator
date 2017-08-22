*Important Note: this project is in **experiment** mode. This means things change rapidly and you cannot depend on the 
exposed functionalities.*
# Coding Web Apps Got Even Easier
Sometimes, your web application's server and client code is written in Python. Let's say you've made a command 
line application that interacts with your server using HTTP.   
Every time you change your urls on the server, you'll have to reflect these changes on the client side. This 
back-and-forth editing is annoying to say the least. Now, what if your client side app is already shipped? How would 
you go about changing the urls you hardcoded in your client app? Worse yet, what if your client app is using more than
 one
 of 
your server applications?   
No one wants to maintain such an application. I wouldn't either, but I've actually made a command-line application 
that fits the above description. This project was born to make my life eaiser.   
# How It Works
This library will generate server side and client side helper functions from a single config file. Basically, you put
 your URL definitions in one file and forget about URLs altogether, both on the server side and the client side.   
 Plus, you can choose the web framework and http library of your choice(right now, only Bottle and requests are 
 supported).   
 As a result, you can make all the changes you want to your URLs in a single place and rest assured that your server 
 and client apps won't crash. This will be true even when client apps have already been shipped!   
# See It In Action
TODO
