from django.apps import AppConfig

class LostandfoundConfig(AppConfig):
    name = 'lostandfound'

    def ready(self):
        import lostandfound.signals

