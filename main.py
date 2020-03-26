from directory_module import *
from frames import *
if __name__ == '__main__':
   
   input_directory_name = "input"
   output_directory_name = "output"
   
   dir = Directory()
   dir.input_directory(input_directory_name)
   dir.output_directory(output_directory_name)
   
   video = create_frames('Funny WhatsApp Status - Minions Funny 30 Second Video -.mp4')
   