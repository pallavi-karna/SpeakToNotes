import threading
import customtkinter as ctk
import tkinter as tk
import torch  
import whisper 
import openai
import tqdm
import sys
import os

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.geometry("900x750")
        self.title("Whisper 2 Summarize - Multi-language")
        self.resizable(False, False)

        self.grid_rowconfigure(5, weight=1)
        self.grid_columnconfigure((0, 1), weight=1)

        self.titlelabel = ctk.CTkLabel(self, text="What would you want to transcribe?", font=ctk.CTkFont(family="Verdana", size=30, weight="bold"))
        self.titlelabel.grid(row=0, column=0, columnspan=2, padx=20, pady=20, sticky="ew")

        self.audiobutton = ctk.CTkButton(self, command=self.select_audio, height=50, text="Select Audio File", font=ctk.CTkFont(family="Verdana", size=16, weight="bold"))
        self.audiobutton.grid(row=1, columnspan=2, padx=20, pady=10, sticky="nsew")

        # Row 2: Model and API Key
        self.modelselect = ctk.CTkComboBox(self, values=["tiny", "base", "small", "medium", "large"], variable=ctk.StringVar(value="base"))
        self.modelselect.grid(row=2, column=0, padx=20, pady=10, sticky="ew")

        self.apitext = ctk.CTkEntry(self, placeholder_text="Enter your OpenAI API Key here.")
        self.apitext.grid(row=2, column=1, padx=20, pady=10, sticky="ew")

        # Row 3: Language and Task Selection
        self.lang_map = {
            "Auto-Detect": None,
            "Telugu (te)": "te",
            "Hindi (hi)": "hi",
            "English (en)": "en"
        }
        self.langselect = ctk.CTkComboBox(self, values=list(self.lang_map.keys()), variable=ctk.StringVar(value="Telugu (te)"))
        self.langselect.grid(row=3, column=0, padx=20, pady=10, sticky="ew")

        self.taskselect = ctk.CTkComboBox(self, values=["Transcribe (Original Script)", "Translate to English"], variable=ctk.StringVar(value="Transcribe (Original Script)"))
        self.taskselect.grid(row=3, column=1, padx=20, pady=10, sticky="ew")

        # Row 4: Action Buttons
        self.transcribebutton = ctk.CTkButton(self, command=self.transcribe_button, height=50, text="Transcribe with Whisper", font=ctk.CTkFont(family="Verdana", size=16, weight="bold"))
        self.transcribebutton.grid(row=4, column=0, padx=20, pady=10, sticky="nsew")

        self.summarybutton = ctk.CTkButton(self, command=self.summary_button, height=50, text="Summarize with GPT", font=ctk.CTkFont(family="Verdana", size=16, weight="bold"))
        self.summarybutton.grid(row=4, column=1, padx=20, pady=10, sticky="nsew")

        # Row 5: Output Console
        self.console = ctk.CTkTextbox(self)
        self.console.grid(row=5, column=0, columnspan=2, padx=20, pady=(20, 20), sticky="nsew")

    def write(self, *message, end="\n", sep=" "):
        text = ""
        for item in message:
            text += "{}".format(item)
            text += sep
        text += end
        self.console.insert("insert", text)

    def select_audio(self):
        self.audio = tk.filedialog.askopenfilename(initialdir='C:/Users/', title="Select Audio", filetypes=(("Open an audio file", "*.mp3 *.wav *.m4a"), ("All files", "*.*")))
        if self.audio:
            self.audiofilename = os.path.basename(self.audio)
            self.audiobutton.configure(text="Selected " + self.audiofilename)

    def transcribe_button(self):
        if not hasattr(self, 'audio') or not self.audio:
            self.write("Please select an audio file first!")
            return
        threading.Thread(target=self.transcribe).start()

    def summary_button(self):
        if not hasattr(self, 'transcript') or not self.transcript:
            self.write("Please transcribe an audio file before summarizing!")
            return
        threading.Thread(target=self.gpt_process).start()

    def transcribe(self):
        class _CustomProgressBar(tqdm.tqdm):
            def __init__(self, *args, **kwargs):
                super().__init__(*args, **kwargs)
                self._current = self.n  
                
            def update(self, n):
                super().update(n)
                self._current += n
                app.write("Audio Transcribe Progress: " + str(round(self._current / self.total * 100)) + "%")
                
        devices = torch.device("cuda:0" if torch.cuda.is_available() else "cpu") 
        selected_model = self.modelselect.get()
        if selected_model in ["Select the Whisper Model", ""]:
            selected_model = "base"

        self.write(f"Loading Whisper model '{selected_model}' on {devices}...")
        model = whisper.load_model(selected_model, device=devices)
        
        transcribe_module = sys.modules['whisper.transcribe']
        transcribe_module.tqdm.tqdm = _CustomProgressBar

        selected_lang_str = self.langselect.get()
        target_lang = self.lang_map.get(selected_lang_str, None)

        task_mode = "translate" if "Translate" in self.taskselect.get() else "transcribe"

        self.write(f"Beginning Transcribing Process (Language: {selected_lang_str}, Task: {task_mode})...")

        # Transcribe call with explicit language and task
        kwargs = {"verbose": True, "fp16": False, "task": task_mode}
        if target_lang:
            kwargs["language"] = target_lang

        result = model.transcribe(self.audio, **kwargs)
        transcribed = result["text"]
        
        output_filename = self.audiofilename + "_Transcript.txt"
        with open(output_filename, "w", encoding='utf-8') as text_file:
            text_file.write(transcribed)
            self.transcript = transcribed
            self.write("Transcription Completed!")
            self.write("Saved Transcript to " + output_filename)
            self.write("\n--- RESULT ---")
            self.write(transcribed)
            self.write("--------------\n")

    def gpt_process(self):
        openai.api_key = self.apitext.get()
        if not openai.api_key:
            self.write("Error: OpenAI API Key is missing.")
            return

        self.write("Processing Transcript with GPT...")
        n = 1300
        split = self.transcript.split()
        snippet = [' '.join(split[i:i+n]) for i in range(0, len(split), n)]
        
        summary = ""
        previous = ""
        for i in range(0, len(snippet), 1):
            self.write("Summarizing Transcribed Snippet {} of {}".format(i + 1, len(snippet)))
            gpt_response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": "\"" + snippet[i] + "\"\n Rewrite the transcript above into clean structured notes and bullet points. For additional context here is the previous rewritten message: \n " + previous}],
                temperature=0.6,
            )
            previous = gpt_response['choices'][0]['message']['content']
            summary += gpt_response['choices'][0]['message']['content']

        output_summary = self.audiofilename + "_Summary.txt"
        with open(output_summary, "w", encoding='utf-8') as text_file:
            text_file.write(summary)
            self.write("Summarizing Completed.")
            self.write("Saved Summary to " + output_summary)

if __name__ == "__main__":
    app = App()
    app.mainloop()