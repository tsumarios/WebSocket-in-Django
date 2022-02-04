from django.apps import AppConfig
from threading import Event, Thread
from websocketIntegration.settings import DEFAULT_WS_PORT


class WebsocketIntegrationConfig(AppConfig):
    name = 'websocketIntegration'

    def ready(self):
        # Implicitly connect signal handlers decorated with @receiver
        from websocketIntegration import signals

        # Start the WebSocket server in a new thread
        from websocketIntegration.websocket import WSServerWrapper
        self.t = Thread(target=WSServerWrapper.run, daemon=True)
        self.t.start()
        if not WSServerWrapper.ws_started_event.wait(10):
            raise RuntimeError("Could not start websocket server on port %s"%DEFAULT_WS_PORT)
