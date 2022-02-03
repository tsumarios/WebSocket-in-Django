import os
from django.dispatch import receiver
from websocketIntegration.signals import update_signal
from websocketIntegration.settings import BASE_DIR
from SimpleWebSocketServer import SimpleWebSocketServer, SimpleSSLWebSocketServer, WebSocket

import logging
logger = logging.getLogger()


class WebSocketHandler(WebSocket):

    @staticmethod
    def sendBroadcast(msg):
        # Broadcast a message to connected clients
        for ws in WSServerWrapper.ws_server.connections.values():
            ws.sendMessage(msg)

    # Signal handling methods

    @staticmethod
    @receiver(update_signal)
    def onUpdateSignal(**kwargs):
        logger.info('Received a signal')
        msg = kwargs.get('msg', '')
        # Broadcast the message received from update_signal
        WebSocketHandler.sendBroadcast(msg)

    # WebSocket handling methods

    def handleMessage(self):
        logger.info('Received msg "%s" from %s' % (self.data, self.address[0]))
        self.sendMessage(self.data)  # Echo message back to client

    def handleConnected(self):
        logger.info('New client connected %s' % self.address[0])

    def handleClose(self):
        logger.info('Client disconnected %s' % self.address[0])


class WSServerWrapper():
    # NOTE: to use WSS, assuming the certificate and private key are in the base directory, switch the ws_server from SimpleWebSocketServer to SimpleSSLWebSocketServer.
    # ws_server = SimpleSSLWebSocketServer('', 5678, WebSocketHandler, certfile=os.path.join(BASE_DIR, 'cert.pem'), keyfile=os.path.join(BASE_DIR, 'key.pem'))
    ws_server = SimpleWebSocketServer('', 5678, WebSocketHandler)

    @staticmethod
    def run():
        logger.info('Starting WebSocket server')
        WSServerWrapper.ws_server.serveforever()
