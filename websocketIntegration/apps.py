from django.apps import AppConfig
from threading import Thread


class WebsocketIntegrationConfig(AppConfig):
    name = 'websocketIntegration'

    def ready(self):
        # Implicitly connect signal handlers decorated with @receiver
        from websocketIntegration import signals

        # Start the WebSocket server in a new thread
        from websocketIntegration.websocket import WSServerWrapper
        self.t = Thread(target=WSServerWrapper.run, daemon=True)
        self.t.start()
