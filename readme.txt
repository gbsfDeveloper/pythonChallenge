Before beggining:

You need to have docker installed and running on your PC.

1. Download the project with git:

    https://github.com/gbsfDeveloper/pythonChallenge.git

2. in the root path of the folder run the follow:

    docker build -t pythonchallenge .

    docker run -p 5000:5000 pythonchallenge

3. Ready, go!

    You can go to:

        http://127.0.0.1:5000/

    to see the project.

4. to run the test you can enter to docker console and run inside this command:
    
    python -m unittest