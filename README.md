# video_filter

    A Python API to know the details of nsfw ( not safe for work content ) in the video .
    
### Directory Structure

     |--data
     |--train
          |--sfw
          |--nsfw
     |--validation
          |--sfw
          |--nsfw
     |--frames
          |--* (All images/frames of input video)
     |--python_learning
     |--Report_File_Excels ( Output timestamps where video is nfsw) 
          |-- *.xlsx
     |--saved_models
          |-- *.h5 (All CNN models)
     |--video_input 
     |--video_output
     |--cleaning_dataset.py
     |--creating_convoltional_neural_net_model_nsfw.py
     |--creating_excels.py
     |--**creating_frames.py
     |--directory_module.py
     |--load_model.py
     |--main.py
     |--README.md
     |--requirements.txt
     |--trial.py
     
### Installation
     run: **pip install -r requirements.txt** in your shell.
     If you have Nvidia graphic card change the tensorflow requirment to GPU (for fast performance) and install required dependencies .
