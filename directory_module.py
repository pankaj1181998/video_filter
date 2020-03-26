from pathlib import Path

class Directory :

   def __init__(self) :
      print("Directory Class Initiated")

   def input_directory(self,input_dir: str):
      p = Path(input_dir)
      try:
         p.mkdir()
         print("Created Successfully...")
      except FileExistsError as exc:
         print(exc)

   def output_directory(self,output_dir : str):
      p = Path(output_dir)
      try:
         p.mkdir()
         print("Created Successfully...")
      except FileExistsError as exc:
         print(exc)