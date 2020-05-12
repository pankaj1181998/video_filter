from pathlib import Path

class Directory :

   def __init__(self) :
      print("Directory Class Initiated")

   def create_directory(self,input_dir: str):
      p = Path(input_dir)
      try:
         p.mkdir()
         print("Directory Created Successfully...")
      except FileExistsError as exc:
         print(" {0} --  Directory Exist...!!!".format(input_dir))