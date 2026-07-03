class EventBus:
    """
    Lightweight event system (later Kafka/RabbitMQ upgrade)
    """

    def publish(self, event_name: str, data: dict):
        print(f"[EVENT] {event_name}: {data}")
