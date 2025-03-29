import matplotlib.pyplot as plt
import time
import random

class SimpleMemoryTracker:
    def __init__(self):
        self.memory_history = []
        self.timestamps = []
        
    def simulate_memory(self):
        """Simulates memory usage patterns"""
        # Random walk pattern
        if not self.memory_history:
            return 100  # Start at 100MB
        change = random.uniform(-5, 10)
        return max(50, self.memory_history[-1] + change)  # Never below 50MB
    
    def track(self, duration=10, interval=1):
        """Simulate tracking memory for given duration"""
        print(f"Simulating memory tracking for {duration} seconds...")
        
        for _ in range(duration):
            mem = self.simulate_memory()
            self.memory_history.append(mem)
            self.timestamps.append(time.time())
            
            print(f"Current memory: {mem:.1f} MB")
            time.sleep(interval)
        
        self.plot_results()
    
    def plot_results(self):
        """Plot the simulated memory usage"""
        plt.figure(figsize=(10, 5))
        times = [t - self.timestamps[0] for t in self.timestamps]
        plt.plot(times, self.memory_history, 'b-')
        plt.title("Simulated Memory Usage")
        plt.xlabel("Time (seconds)")
        plt.ylabel("Memory (MB)")
        plt.grid(True)
        plt.show()

if __name__ == "__main__":
    tracker = SimpleMemoryTracker()
    tracker.track(duration=10)  
