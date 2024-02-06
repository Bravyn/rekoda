import sounddevice as sd 
import soundfile as sf

from tkinter import *

def voicer():
    sample_rate = 48000

    
    duration = 5 #in seconds
    recording1 = sd.rec(int(duration * sample_rate),samplerate = sample_rate, channels=2)
    sd.wait()

    #save file
    return sf.write("reco1.flac", recording1, sample_rate)

master = Tk()

Label(master, text = "Voicer").grid(row = 0, sticky=W, rowspan=5)

b = Button(master, text="Start", command=voicer)
b.grid(row = 0, column=2, columnspan=2, rowspan=2, padx=5, pady=5)

mainloop()