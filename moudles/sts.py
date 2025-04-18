import vosk
import wave

def speech_to_text(audio_path):
    model = vosk.Model("model")
    wf = wave.open(audio_path, "rb")
    rec = vosk.KaldiRecognizer(model, wf.getframerate())
    
    while True:
        data = wf.read(4000)
        if len(data) == 0:
            break
        if rec.AcceptWaveform(data):
            result = rec.Result()
            return result
