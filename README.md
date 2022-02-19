# WebSocket-in-Django

Simple PoC of the integration of a loosely coupled WebSocket server within a Django application.

This demo is part of the "WebSocket Integration in Django" technical report, available at <TODO:link>.

## Dependencies

This project is developed using the [Django Python framework](https://www.djangoproject.com) and the [SimpleWebSocketServer](https://github.com/dpallot/simple-websocket-server/blob/master/SimpleWebSocketServer/SimpleWebSocketServer.py) module.

## Usage

In order to run the proof-of-concept, clone this repository and install the requirements by opening your favourite **Terminal**, typing as follows:

```sh
git clone https://github.com/tsumarios/WebSocket-in-Django
cd WebSocket-in-Django
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
```

Then, you can run the Django application within the WebSocket server type the following command:

```sh
python3 manage.py runserver --noreload [port]
```

Note that by default the Django server will be listening on port 8000 and the WebSocket server will be using port 5678. In order to change this setting, you need to set a new port value in the `DEFAULT_WS_PORT` variable in the [settings.py](https://github.com/tsumarios/WebSocket-in-Django/blob/main/websocketIntegration/settings.py) file.

#### TLS

The WebSocket server can also run using the WSS (WebSocket Secure) protocol. Assuming the certificate and private key are in the base directory and named as "cert.pem" and "key.pem", just switch the `ws_server` in the [websocket.py](https://github.com/tsumarios/WebSocket-in-Django/blob/main/websocketIntegration/websocket.py) file from *SimpleWebSocketServer* to *SimpleSSLWebSocketServer* by uncommenting [line 47](https://github.com/tsumarios/WebSocket-in-Django/blob/325edba2a96bac70cf5052817af859035f1357f4/websocketIntegration/websocket.py#L47) and commenting its next line. If the TLS protocol is enabled, remember to switch the WebSocket URL from <ws://host:port/> to <wss://host:port/> in [line 24](https://github.com/tsumarios/WebSocket-in-Django/blob/ebb477b5cf4ed8d3a9a59a1e9cda58ca3ac7f06e/client/websocket.html#L24) in the websocket.html file or in your WebSocket client.

### PoC

Eventually, once the servers are running you need to perform two last steps:

1. Open the [websocket.html](https://github.com/tsumarios/WebSocket-in-Django/blob/main/client/websocket.html) file with your favourite browser and press the "connect" button (or any WebSocket client/plugin and connect to the following URL: <ws://locahost:5678/>). Note that if you send any message, the server will already echo it back.
2. Open a new tab/window in your favourite browser and go to the following URL: <http://localhost:8000/>. The index page will show a simple "Hello, it's me..." text.

Whenever the index page is accessed - you can just press the refresh button (F5) in the browser - the custom `update_signal` is triggered and the WebSocket server, upon reacting to such signal, broadcasts a message to all its connected clients and you should be able to see the magic happen in the websocket.html page or, in general, in your WebSocket client.

#### Contacts

- Email: mario.raciti@inaf.it / marioraciti@pm.me
- LinkedIn: linkedin.com/in/marioraciti
- Twitter: twitter.com/tsumarios

**Enjoy WebSockets!**
