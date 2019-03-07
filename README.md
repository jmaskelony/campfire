# Campfire
Client binary will gather iptable information and send it to a web server via POST request.  The server will be [Reach](https://github.com/degenerat3/reach), which will process the data and ship it to an ELK stack.

### Config:
In the "campfire.go" file, lines 18 and 19 contain the variables that must be changed  
`var serv = "127.0.0.1:5000"`  
`var loop_time = 60`  
The "serv" variable contains the IP/port of the Reach server, and the "loop_time" variable is an integer dictating how often the binary will post data back to the server (in seconds).    
Once these variables are updated, the code can be compiled into a binary using the following command, which can then be dropped on to the hosts:  
`go build campfire.go`  
Note: Target OS must be set to Linux (GOOS env variable)


### Usage:
##### Client
The client binary has two options when running, to loop or to only execute a single time.  Executing with no arguments will cause the binary to post data every X seconds, where X is defined as explained above. Executing with any argument will cause the binary to only post data back once, then terminate.  

### Old Version:
There is a standalone tracker/server that can be used, which runs a simple flask app for callbacks instead of using Reach.  Instructions for usage can be found in the `server` directory.

<!--
##### Server
###### Install
The docker image can be built from the "server" directory by using the following command:  
`sudo docker build -t campfire:latest .`  
once the build is finished, it can be run with the following:  
`sudo docker run -d -p 5000:5000 campfire`  
The flask server is now accessible via port 5000  

###### Navigation
Once the server is running, the hosts will be able to send their post requests to "_IP_:5000/api/rule_send" which can then be viewed by going to the associated host URL.  For hostname "test1" the url would be ""_IP_:5000/api/hosts/test1" or users can navigate to "_IP_:5000/hosts/" and they will have a list of all tracked targets. 

###### Tracker
As an alternative to using a web browser to manually navigate the pages, users can run the "tracker.py" script, which offers a CLI to list tracked hosts and view firewall information of a specific host.  The only configuration needed for "tracker.py" is to install the requirements(the requests library), and to replace the "server" variable on line 10 with the IP address of your campfire flask server.  
`server = "127.0.0.1:5000"`  
 
-->
