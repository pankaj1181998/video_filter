from directory_module import *
from creating_frames import *
import os
if __name__ == '__main__':
   
   input_directory_name = "video_input"
   output_directory_name = "video_output"
   
   dir = Directory()
   dir.input_directory(input_directory_name)
   dir.output_directory(output_directory_name)
   print('Total Videos in Input Directory:', len(os.listdir(input_directory_name+'/')))
   
   for file in os.listdir(input_directory_name+'/'):
      print(file)
      create_frames(file)
      # video = create_frames('Funny WhatsApp Status - Minions Funny 30 Second Video -.mp4')
   