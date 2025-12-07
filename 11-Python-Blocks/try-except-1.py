try:
  x = "Hello Try except Block"
  print(y)
except NameError as ne:
    print(f"A NameError occured: {ne}")
except Exception as e:
    print(f"An unexpected error occured: {e}")