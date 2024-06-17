# Transcript Generation Using Python  

Python Application to generate transcription from video files.  

### Required Software and Packages

- Software :  
    - `Python`  
    - `VS Code`
- Software Packages :  
    - `pydub` : pip install  
    - `speechrecognition` : pip install  
    - `speechrecognition` : pip install  
    - `torch` : pip install  
    - `torchvision` : pip install  
    - `torchaudio` : pip install
    - `ffmpeg` : sudo apt install  

### Folder Structure  

- `Transcript Application` : it is our parent folder which will contain all application related files.

    - `videos` : it will store our video files.  

    - `audio` : it will store audios generated from our videos.  

    - `transcript` : it will store the transcript from audios.  

    - `summaries` : it will store the summary from our transcripts.  

    - `scripts` : it will store all the script and requred to convert transcript from video files.  

### Run Script

We can run application to generate trabnscription and summary using this command : **``python3 scripts/process_videos.py``**

**Note:** We can modify the code according to Python Version and Software Package Compatibility.  

`Logger has been implemented and we can have a log file here also to know which methods have been called.`