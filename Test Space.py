def blam(name: str = "?") -> str:
    """
    Function to blamify something

    Args:
        name (str, optional): Thing to blamify. Defaults to "?".

    Returns:
        str: Status of blamification
    """
    
    return f"{name} has been blammed!"



print("Hello World")
print(blam("Python"))



try:
  if int(input()) == 1:
    print("Correct!")
  else:
    print("Wrong number")
except:
  print("Invalid value")
