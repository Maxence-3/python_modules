from abc import ABC, abstractmethod
from typing import Any, List

class DataProcessor(ABC):
    @abstractmethod
    def process(self, data: Any) -> str:
        pass

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    def format_output(self, result: str) -> str:
        return f"Output: {result}"

class NumericProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        try:
            if not isinstance(data, list):
                return False
            for item in data:
                if not isinstance(item, int):
                    return False
            return True
        except:
            return False

    def process(self, data: Any) -> str:
        if not self.validate(data):
            raise ValueError("Invalid numeric data")
        else:
            length = len(data)
            total = sum(data)
            avg = total/length
            return f"Processed {length} numeric values, sum={total}, avg={avg}"

class TextProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        try:
            if not isinstance(data, str):
                return False
            return True
        except:
            return False
    
    def process(self, data: Any) -> str:
        if not self.validate(data):
            raise ValueError ("Invalid text data")
        else:
            length = len(data)
            words = len(data.split())
            return f"Processed text: {length} characters, {words} words"

class LogProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if not isinstance(data, str):
            return False
        elif "ERROR" in data or "INFO" in data:
            return True
        else:
            return False

    def process(self, data: Any) -> str:
        if not self.validate(data):
            raise ValueError ("Invalid log data")
        
        if "ERROR" in data:
            level = "ERROR"
            prefix = "[ALERT]"
        elif "INFO" in data:
            level = "INFO"
            prefix = "[INFO]"
        
        message = data.split(":", 1)[1].strip() if ":" in data else data

        return f"{prefix} {level} level detected: {message}"


if __name__ == "__main__":
    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===\n")

    print("Initializing Numeric Processor...")
    num_processor = NumericProcessor()
    data = [1, 2, 3, 4, 5]
    print(f"Proccessing data: {data}")

    if num_processor.validate(data):
        print("Validation: Numeric data verified")
        result = num_processor.process(data)
        print(num_processor.format_output(result))

    print("\nInitializing Text Processor...")
    txt_processor = TextProcessor()
    data = "Hello Nexus World"
    print(f"Processing data: {data}")

    if txt_processor.validate(data):
        print("Validation: Text data verified")
        result = txt_processor.process(data)
        print(txt_processor.format_output(result))

    print("\nInitializing Log Processor...")
    log_processor = LogProcessor()
    data = "ERROR: Connection timeout"
    print(f"Processing data: {data}")

    if log_processor.validate(data):
        print("Validation: Log entry verified")
        result = log_processor.process(data)
        print(log_processor.format_output(result))

    print("\n=== Polymorphic Processing Demo ===\n")
    print("Processing multiple data type through same interface...")

    processors = [NumericProcessor(), TextProcessor(), LogProcessor()]
    test_data = [[1, 2, 3], "Hello World!", "INFO: System ready"]

    for i, (proc, data) in enumerate(zip(processors, test_data), 1):
        try:
            if proc.validate(data):
                result = proc.process(data)
                print(f"Result {i}: {result}")
        except Exception as e:
            print(f"Error processing data {i}: {e}")
    print("\nFoundation systems online. Nexus ready for advanced streams.")