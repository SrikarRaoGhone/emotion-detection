from fer import FER
from fer import Video

import pandas as pd

video_file: str = "./videos/vid2.mp4"

face_detector: FER = FER(tfserving=False)

processed_video = Video(video_file=video_file)

processing_data = processed_video.analyze(face_detector, display=False)