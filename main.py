from directory_module import *
from creating_frames import *
from load_model import *
import os
if __name__ == '__main__':
   
   input_directory_name = "video_input"
   output_directory_name = "video_output"
   excel_directory_name = "Report_File_Excels"
   
   dir = Directory()
   dir.create_directory(input_directory_name)
   dir.create_directory(output_directory_name)
   dir.create_directory(excel_directory_name)
   
   print('Total Videos in Input Directory:', len(os.listdir(input_directory_name+'/')))
   
   for file in os.listdir(input_directory_name+'/'):
      print(file)
      create_frames(file)
      
   for file in os.listdir(excel_directory_name+'/'):
      load_model_and_calculate(file)
      