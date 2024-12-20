# Introduction 
- In this readme we have basic ways to run this python project

## Configuring flow token

1. Log into flow
1. Run the follow script in the console
    ```javascript
    javascript:(function(){prompt('Token', (document.cookie.split(';').filter(e => e.indexOf('Token') > 0))[0].split('=')[1]); })();
    ```
1. Copy the token
1. Open the .env file
1. Replace the value in the variable FLOW_TOKEN


## Configuring and running the project

Two options:
1. Running using docker compose
1. Running using venv


### Running using docker compose

```sh
docker compose up -d
```

You can run the call.http file for test if the app is working. For run the file you can install the 'REST Client' extension [link](https://marketplace.visualstudio.com/items?itemName=humao.rest-client).

Example:

![Rest Client Example](assets/rest-client-call-example.png)


### Running using venv

1. Check if you have python installed (if you need to installed, specially in windows make sure the python path will part of your windows path)

    ```bash
    python --version
    # or
    python3 --version

    # after check if is python3 or python
    python -m venv venv #or python3

    # activating venv

    # linux mac
    source venv/bin/activate

    # windows
    venv\Scripts\activate

    # pip or pip3
    pip3 install -r requirements.txt
    pip install -r requirements.txt

    ```


1. Executing the project

    ```bash
    python3 src/main.py
    
    # or
    python src/main.py

    ```


### Other commands

This command below delete container and image generated.

```
docker rm -f base_project-flask_app-1 && docker image rm -f base_project-flask_app 
```

Check the logs for the application

```
docker logs base_project-flask_app-1
```

### Extensions that can help you to run python in vscode

- [Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python)