#First, Let's import the required modules
import os
import platform

def show_system_info():
    print("\n--- Checking your system... ---")
    
    #Operating System Information
    print(f"The name of the operating system: {platform.system()}")
    print(f"Release version: {platform.release()}")
    print(f"Internal system Name (os.name): {os.name}")
    
    print("\n---")
    
    #processor (CPU) Information
    print(f"processor Architecture: {platform.machine()}")
    print(f"Exact processor Name: {platform.processor()}")
    print(f"Number of Logical CPU Cores: {os.cpu_count()}")
    
    print("\n System check completed successfully!")
    
    #Run the function
if __name__ == "__main__":
    show_system_info()