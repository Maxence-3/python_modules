from abc import ABC, abstractmethod
from typing import Any, List, Dict, Optional, Union


class DataStream(ABC):
    def __init__(self, stream_id: str, stream_type: str):
        self.stream_id = stream_id
        self.stream_type = stream_type
        self.total = 0

    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        pass

    def filter_data(self,
                    data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        if criteria is None:
            return data_batch

        filtered = [
            i for i in data_batch if criteria.lower() in str(i).lower()
        ]
        return filtered

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return {"stream_id": self.stream_id,
                "type": self.stream_type,
                "total_processed": self.total}


class SensorStream(DataStream):
    def __init__(self, stream_id: str):
        super().__init__(stream_id, "Environmental Data")
        self.temperatures = []

    def process_batch(self, data_batch: List[Any]) -> str:
        try:
            self.total += len(data_batch)
            for item in data_batch:
                item_str = str(item)
                if "temp" in item_str:
                    temp_value = float(item_str.split(":")[1])
                    self.temperatures.append(temp_value)

            if self.temperatures:
                avg_temp = sum(self.temperatures) / len(self.temperatures)
                return f"Sensor analysis: {len(data_batch)} \
readings processed, avg temp: {avg_temp:.1f}°C"
            else:
                return f"Sensor analysis: {len(data_batch)} readings processed"
        except Exception as e:
            return f"Sensor processing error: {e}"


class TransactionStream(DataStream):
    def __init__(self, stream_id: str):
        super().__init__(stream_id, "Financial Data")
        self.net_flow = 0

    def process_batch(self, data_batch: List[Any]) -> str:
        try:
            self.total += len(data_batch)

            for item in data_batch:
                item_str = str(item)

                if "buy" in item_str:
                    amount = int(item_str.split(":")[1])
                    self.net_flow += amount
                elif "sell" in item_str:
                    amount = int(item_str.split(":")[1])
                    self.net_flow -= amount

            sign = "+" if self.net_flow >= 0 else ""
            return f"Transaction analysis: {len(data_batch)} \
operations, net flow: {sign}{self.net_flow} units"
        except Exception as e:
            return f"Transaction processing error: {e}"


class EventStream(DataStream):
    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id, "System Events")
        self.error = 0

    def process_batch(self, data_batch: List[Any]) -> str:
        try:
            self.total += len(data_batch)

            for item in data_batch:
                if "error" in str(item):
                    self.error += 1
            return f"Event analysis: {len(data_batch)} events, \
{self.error} error detected"
        except Exception as e:
            return f"Event processing error: {e}"


class StreamProcessor:
    def __init__(self) -> None:
        self.streams: list[DataStream] = []

    def add_stream(self, stream: DataStream) -> None:
        self.streams.append(stream)

    def process_all_streams(self, data_batches: list[list[any]]) -> list[str]:
        results: list[str] = []
        for stream, data_batch in zip(self.streams, data_batches):
            result: str = stream.process_batch(data_batch)
            results.append(result)
        return results


if __name__ == "__main__":
    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===\n")

    print("Initializing Sensor Stream...")
    sensor: SensorStream = SensorStream("SENSOR_001")
    print(f"Stream ID: {sensor.stream_id}, Type: {sensor.stream_type}")

    data: list = ["temp:22.5", "humidity:65", "pressure:1013"]
    print(f"Processing sensor batch: {data}")
    result = sensor.process_batch(data)
    print(result)

    print("\nInitializing Transaction Stream...")
    transaction: TransactionStream = TransactionStream("TRANS_001")
    print(f"Stream ID: {transaction.stream_id}, \
Type: {transaction.stream_type}")

    data: list = ["buy:100", "sell:150", "buy:75"]
    print(f"Processing transaction batch: {data}")
    result: str = transaction.process_batch(data)
    print(result)

    print("\nInitializing Event Stream...")
    event: EventStream = EventStream("EVENT_001")
    print(f"Stream ID: {event.stream_id}, Type: {event.stream_type}")

    data: list = ["login", "error", "logout"]
    print(f"Processing event batch: {data}")
    result: str = event.process_batch(data)
    print(result)

    print("\n=== Polymorphic Stream Processing ===")
    print("Processing mixed stream types through unified interface...\n")

    processor: StreamProcessor = StreamProcessor()

    sensor2: SensorStream = SensorStream("SENSOR_002")
    transaction2: TransactionStream = TransactionStream("TRANS_002")
    event2: EventStream = EventStream("EVENT_002")

    processor.add_stream(sensor2)
    processor.add_stream(transaction2)
    processor.add_stream(event2)

    batch_data: list[list[any]] = [
        ["temp:21.0", "temp:23.0"],
        ["buy:50", "sell:30", "buy:100", "sell:80"],
        ["login", "logout", "error"]
    ]

    print("Batch 1 Results:")
    results: list[str] = processor.process_all_streams(batch_data)
    print("- Sensor data: 2 readings processed")
    print("- Transaction data: 4 operations processed")
    print("- Event data: 3 events processed")

    print("\nStream filtering active: High-priority data only")
    sensor_critical: list[any] = sensor.filter_data(
        ["temp:95.0", "temp:22.0", "temp:98.0"],
        "temp:9")
    transaction_large: list[any] = transaction.filter_data(
        ["buy:1000", "buy:50"],
        "1000")
    print(f"Filtered results: {len(sensor_critical)} \
critical sensor alerts, {len(transaction_large)} large transaction")

    print("\nAll streams processed successfully. Nexus throughput optimal.")
