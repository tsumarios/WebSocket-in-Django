from django.dispatch import receiver
from websocketIntegration.signals import update_signal
from SimpleWebSocketServer import SimpleWebSocketServer, WebSocket

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
    # To use WSS: SimpleSSLWebSocketServer('', 5678, WebSocketHandler, certfile='<path_to_cert.pem>', keyfile='<path_to_key.pem>')
    ws_server = SimpleWebSocketServer('', 5678, WebSocketHandler)

    @staticmethod
    def run():
        logger.info('Starting WebSocket server')
        WSServerWrapper.ws_server.serveforever()
