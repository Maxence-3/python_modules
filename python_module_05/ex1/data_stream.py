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

    def filter_data(self, data_batch: List[Any], criteria: Optional[str] = None) -> List [Any]:
        if criteria is None:
            return data_batch

        filtered = [item for item in data_batch if criteria.lower() in str(item).lower()]
        return filtered

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return {"stream_id": self.stream_id, "type": self.stream_type, "total_processed": self.total}

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
                return f"Sensor analysis: {len(data_batch)} readings processed, avg temp: {avg_temp:.1f}°C"
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
            return f"Transaction analysis: {len(data_batch)} operations, net flow: {sign}{self.net_flow} units"
        except Exception as e:
            return f"Transaction processing error: {e}"

class EventStream(DataStream):
    def __init__(self, stream_id: str):
        super().__init__(stream_id, "System Events")
        self.error = 0

    def process_batch(self, data_batch: List[Any]) -> str:
        try:
            self.total += len(data_batch)

            for item in data_batch:
                if "error" in str(item):
                    self.error += 1
            return f"Event analysis: {len(data_batch)} events, {self.error} error detected"
        except Exception as e:
            return f"Event processing error: {e}"

class StreamProcessor(DataStream):
    def __init__(self, stream_id: str):
        super().__init__(stream_id)

if __name__ == "__main__":
    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===\n")

    print("Initializing Sensor Stream...")
    sensor = SensorStream("SENSOR_001")
    print(f"Stream ID: {sensor.stream_id}, Type: {sensor.stream_type}")

    data = ["temp:22.5", "humidity:65", "pressure:1013"]
    print(f"Processing sensor batch: {data}")
    result = sensor.process_batch(data)
    print(result)

    print("\nInitializing Transaction Stream...")
    transaction = TransactionStream("TRANS_001")
    print(f"Stream ID: {transaction.stream_id}, Type: {transaction.stream_type}")

    data = ["buy:100", "sell:150", "buy:75"]
    print(f"Processing transaction batch: {data}")
    result = transaction.process_batch(data)
    print(result)

    print("\nInitializing Event Stream...")
    event = EventStream("EVENT_001")
    print(f"Stream ID: {event.stream_id}, Type: {event.stream_type}")

    data = ["login", "error", "logout"]
    print(f"Processing event batch: {data}")
    result = event.process_batch(data)
    print(result)

    print("\n=== Polymorphic Stream Processing ===")
    print("Processing mixed stream types through unified interface...")