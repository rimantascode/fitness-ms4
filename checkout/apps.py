

class CheckoutConfig(AppConfig):
    name = 'checkout'

    def ready(self):
        import checkout.signals
