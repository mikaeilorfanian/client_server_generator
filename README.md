*Important Note: this project is in **experiment** mode. This means things change rapidly and you cannot depend on the 
exposed functionalities.*
# Coding Web Apps Got Even Easier
Sometimes, your web application's server and client code is written in Python. Let's say you've made a command 
line application that interacts with your server using HTTP. Every time you change your URLs and routes on the server 
side, you'll 
have to reflect these changes on the client side, too. This 
back-and-forth editing is annoying to say the least.   
Now, what if your client side app is already shipped? How would 
you go about changing the URLs you hardcoded in an app you've already shipped? Worse yet, what if your client app is 
using 
more than
 one
 of 
your server applications?   
No one wants to maintain such an application. I wouldn't either, but I've actually made a command-line application 
that fits the above description. This project was born to make my life eaiser and help me save $$$(more on that 
later!).   
# How It Works
This library will generate server side and client side helper functions from a single config file. Basically, you put
 your URL definitions in one file and forget about URLs altogether, both on the server side and the client side.   
 Plus, you can choose the web framework and http library of your choice(right now, only Bottle and requests are 
 supported).   
 As a result, you can make all the changes you want to your URLs in a single place and rest assured that your server 
 and client apps won't crash. This will be true even when client apps have already been shipped!   
# See It In Action
## Server Application
Notice the lack of URLs and routes. Instead, we define `route_name` for the class that inherits from `MagicRouter` 
and `handler` which is the controller for that route.
```python
from server_generator.server_generator import BottleServer, MagicRouter


class HelloNameURLHandler(MagicRouter):
    route_name = 'hello_name'

    def handler(self):
        return 'hello {}'.format(self.name)


app = BottleServer(
    HelloNameURLHandler(),
)
app.run()
```
`route_name` and other details about routes and URLs are defined in a config file that looks like this:   
```yaml
server:
  server_backend: bottle
  routes:
    - route_name: hello_name
      route: /hello/<name>
      route_variable: name
      http_method: GET

```
## Client Application
TODO
# Using This Library Saves You Time and a Lot of Headache
As you can see from the above sample applications, `client_server_generator` makes your job as a web developer eaiser
 by automating the generation of a lot of boilerplate code that deals with URLs and routes in your applications.   
Not all applications will benefit from this libarary. After all, you don't always create client and server side apps 
at the same time and using the same programming language. But, if you do, then `client_server_generator` will be of 
great 
benefit to you.
# For Developers
First, download this repo. Then, install it using pip:    
`pip install --editable .`    
Then, depending on which framework you want to use this library with, you need install what's required for that framework to work.   
At this moment, the following frameworks and libraries are supposed by `client_server_generator`:   
- bottle
