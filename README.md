# video_filter

    A Python application to know the details of nsfw ( not safe for work content ) in the video .
    
### Directory Structure
```
|--data
     |--train
          |--sfw
          |--nsfw
     |--validation
          |--sfw
          |--nsfw
|--frames
     |-- (All images/frames of input video)
|--python_learning
     |--Report_File_Excels ( Output excel files with timestamps ) 
          |-- .xlsx
|--saved_models
     |-- .h5 (All CNN models)
|--video_input
     |-- .mp4 (Video Files)
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
``` 
### Installation

'''
run: **pip install -r requirements.txt** in your shell.
**Note** - If you have Nvidia graphic card change the tensorflow requirment to tensorflow-GPU (for fast performance) and install required dependencies .
'''

### Creating CNN Model  

'''
- Download the images for content **safe for work** and **not safe for work** from kaggle or other sources and place in the data folder.
- Run the code **creating_convoltional_neural_net_model_nsfw.py** and obtain the model in saved_models folder .
'''

### Steps to Follow -
'''
Place the video you want to be analysed in the **video_input** directory .
Run the **main.py** 
'''

### Working -

'''
Main.py will call the create_frames function which will read the video file and create all the image frames in frames folder .
Each frame/image is captured after 0.5 second(500 milliseconds) . The function create_frames will write the data into excel file using pandas in Report_File_Excels folder . Data contains 'full_path' , 'timestamp' and 'prediction' column as nil .
The frames are created for each and every video in video_input folder .
After creating frames . The load_model_and_calculate is called which will load the CNN model created at starting . All the images are fed to the model and the prediction results are written in the excel file .
'''
