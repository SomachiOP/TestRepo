from time import sleep
from rich.traceback import install; install()
print("Hello World")

def blam(name: str = "?") -> str:
    """
    Function to blamify something

    Args:
        name (str, optional): Thing to blamify. Defaults to "?".

    Returns:
        str: Status of blamification
    """
    
    print(f"Blamming {name}...")
    sleep(3)
    
    
    return f"{name} has been blammed!"



print("Hello World")
print(blam("Python"))

print("Bruh Momento")
print ("Somachi - Trying to add another change")

try:
  if int(input()) == 1:
    print("Correct!")
  else:
    print("Wrong number")
except:
  print("Invalid value")
