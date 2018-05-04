# project_badges
this is a server that will return images.

##before running:

[i] open '__ init __.py' in your text editor.
![l](https://user-images.githubusercontent.com/35032810/39611688-3155bb16-4f8c-11e8-8ffd-c8496720ed57.png)

[ii] change the path on line 6 to match the location of your 'project_ badges/badges/' folder to look like so.
![g](https://user-images.githubusercontent.com/35032810/39611721-8124a828-4f8c-11e8-872b-427fa7ea2220.png)
the correct path is necessary to see images in your browser.


##to run:

[1] navigate to 'hellotest' directory in terminal 

[2] activate virtual environment 
>`$ source venv/bin/activate`

which has flask installed and is necessary to run the server.

[3] then, run: 
>`$ python hello.py`

you should see something like
![running on port 3000](https://user-images.githubusercontent.com/35032810/39610601-1e8ff22e-4f84-11e8-9d52-c3f61a72e14a.png) 
which indicates that that the server is running on localhost on port 3000.


[4] you can then visit `localhost:3000/badges` in your browser to not receive an image, unless you refresh, in which case images will be fed and then denied again, changing every refresh.
![ll](https://user-images.githubusercontent.com/35032810/39610948-61474d18-4f86-11e8-883c-7886443ec094.png)

this is what you will see if you are successful.

![lll](https://user-images.githubusercontent.com/35032810/39611085-5c205a54-4f87-11e8-94a3-fd4ab708bb45.png)

if you are not interested, visit `localhost:3000/shanghai` to be given the information that the weather sucks, regardless of what the weather is actually like or any of the other endpoints in 'routes.py' for their respective images.



*if you have flask already installed, the virtual environment may not be necessary.*
