from ShazamAPI import Shazam

class ShazamWrapper:
    def __init__(self, file):
        mp3_file_content_to_recognize = file.read()
        shazam = Shazam(mp3_file_content_to_recognize)
        self.recognize_generator = shazam.recognizeSong()
    def getData(self):
        return next(self.recognize_generator)