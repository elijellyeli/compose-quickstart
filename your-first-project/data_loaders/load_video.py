import csv
import cv2
import os 
# from mage_ai.io.file import FileIO
if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@data_loader
def load_data_from_file(*args, **kwargs):

    print(f'curr wd {os.getcwd()}')

    # Open the video file
    vid_capture = cv2.VideoCapture(r"your-first-project/vids/one_hour.mp4")
    
    if (vid_capture.isOpened() is False):
        print("Error opening the video file")
        return 

    # Read fps and frame count
    else:
        # Create a CSV file to store the data
        csv_file = open(r"your-first-project/files/video_data.csv", "w", newline="")
        csv_writer = csv.writer(csv_file)

        # Write the header row to the CSV file
        csv_writer.writerow(["frame_number", "timestamp", "brightness"])

        # Iterate over the video frames
        while True:
            # Read the next frame
            ret, frame = vid_capture.read()
            # If the frame is empty, we have reached the end of the video
            if not ret:
                break
            # Calculate the brightness of the frame
            brightness = cv2.mean(frame)[0]
            # Write the frame data to the CSV file
            csv_writer.writerow([vid_capture.get(cv2.CAP_PROP_POS_FRAMES), vid_capture.get(cv2.CAP_PROP_POS_MSEC), brightness])

        # Close the CSV file
        csv_file.close()

    return csv_file.name


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
