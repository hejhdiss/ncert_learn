import subprocess
import os

def run_youtube_downloader():
    # Get the current working directory (the folder where the script is located)
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Define the path to the executable
    exe_path = os.path.join(script_dir, 'ytdownloader', 'YoutubeDownloader.exe')
    
    # Check if the executable exists before attempting to run it
    if os.path.exists(exe_path):
        try:
            # Run the application
            subprocess.run([exe_path], check=True)
            print("YoutubeDownloader.exe ran successfully!")
        except subprocess.CalledProcessError as e:
            print(f"Error occurred while running YoutubeDownloader.exe: {e}")
    else:
        print(f"{exe_path} not found!")

# Call the function to run the application

