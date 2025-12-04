import os
import shutil
import subprocess
import tempfile
import threading
import time
from pathlib import Path
from typing import Optional
import tkinter as tk
from tkinter import messagebox
import cv2
from PIL import Image, ImageTk
import pygame

class Calculator:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("InPane Calculator")
        self.window.geometry("300x450")
        self.window.configure(bg="#2C3E50")
        
        # Initialize pygame for audio (guard in case audio device unavailable)
        try:
            pygame.init()
            pygame.mixer.init()
        except Exception:
            # audio will be disabled if initialization fails
            self._audio_available = False
        else:
            self._audio_available = True

        # Create temp directory for audio files in system temp (safer than home)
        self.temp_dir = Path(tempfile.gettempdir()) / "calculator_audio_temp"
        self.temp_dir.mkdir(exist_ok=True)
        
        # Initialize calculator variables
        self.current_number = "0"
        self.first_number = None
        self.operation = None
        self.should_reset = False
        
        # Video properties
        self.video_window = None
        self.video_frame = None
        self.cap = None
        self.is_playing = False
        self.video_thread = None
        self.audio_playing = False
        
        # Try a few default video locations; leave as None if none found
        self.video_path: Optional[str] = None
        candidate_paths = [
            r"c:\Users\alexa\Videos\Python\Sample2.Mp4",
            r"c:\Users\alexa\Videos\Python\Sample.Mp4",
        ]
        for p in candidate_paths:
            if os.path.exists(p):
                self.video_path = p
                break
        
        # Create the calculator interface
        self.create_widgets()
        
    def create_video_window(self):
        if self.video_window is None:
            # Create video window
            self.video_window = tk.Toplevel(self.window)
            self.video_window.title("Relapse ka muna")
            self.video_window.geometry("640x520")
            self.video_window.configure(bg="#2C3E50")
            
            # Video frame
            self.video_frame = tk.Label(self.video_window)
            self.video_frame.pack(pady=10)
            
            # Handle window close
            self.video_window.protocol("WM_DELETE_WINDOW", self.on_video_window_close)
            
            # Load and start playing the default video (if available)
            if not self.video_path or not os.path.exists(self.video_path):
                messagebox.showerror("Error", "Video file not found!")
                return

            # Load video capture
            self.cap = cv2.VideoCapture(self.video_path)

            # Try to play audio (best-effort)
            if self._audio_available:
                try:
                    self._try_play_audio_for_video(self.video_path)
                except Exception as e:
                    # Avoid crashing the UI for audio failures
                    print(f"Audio playback failed: {e}")

            # Start video thread
            self.is_playing = True
            self.video_thread = threading.Thread(target=self._play_video_thread)
            self.video_thread.daemon = True
            self.video_thread.start()
            
    def on_video_window_close(self):
        if self.cap is not None:
            self.is_playing = False
            self.cap.release()
        if self.audio_playing:
            pygame.mixer.music.stop()
            self.audio_playing = False
        self.video_window.destroy()
        self.video_window = None
        
    def create_widgets(self):
        # Display frame
        display_frame = tk.Frame(self.window, bg="#2C3E50")
        display_frame.pack(fill=tk.X, padx=20, pady=(20, 0))
        
        # Display
        self.display = tk.Label(
            display_frame,
            text="0",
            font=("Arial", 32, "bold"),
            bg="#34495E",
            fg="white",
            anchor="e",
            padx=15,
            pady=15
        )
        self.display.pack(fill=tk.X)
        
        # Buttons frame
        buttons_frame = tk.Frame(self.window, bg="#2C3E50")
        buttons_frame.pack(expand=True, fill=tk.BOTH, padx=20, pady=20)
        
        # Button layout
        buttons = [
            ('7', '#34495E'), ('8', '#34495E'), ('9', '#34495E'), ('÷', "#8722E6"),
            ('4', '#34495E'), ('5', '#34495E'), ('6', '#34495E'), ('×', "#8722E6"),
            ('1', '#34495E'), ('2', '#34495E'), ('3', '#34495E'), ('-', "#8722E6"),
            ('0', '#34495E'), ('.', '#34495E'), ('=', '#27AE60'), ('+', "#8722E6")
        ]
        
        # Configure grid
        for i in range(4):
            buttons_frame.columnconfigure(i, weight=1)
        for i in range(4):
            buttons_frame.rowconfigure(i, weight=1)
            
        # Create buttons
        for i, (text, color) in enumerate(buttons):
            row = i // 4
            col = i % 4
            
            def make_command(x=text):
                if x in "0123456789.":
                    return lambda: self.add_digit(x)
                elif x in "+-×÷":
                    op = "/" if x == "÷" else "*" if x == "×" else x
                    return lambda: self.set_operation(op)
                elif x == "=":
                    return self.calculate
                
            button = tk.Button(
                buttons_frame,
                text=text,
                font=("Arial", 18, "bold"),
                bg=color,
                fg="white",
                relief="raised",
                command=make_command()
            )
            button.grid(row=row, column=col, padx=3, pady=3, sticky="nsew")
            
            # Make buttons expand
            button.grid_configure(ipadx=10, ipady=10)
            
            # Hover effects
            def on_enter(e, btn=button):
                btn.config(bg="#2C3E50")
                
            def on_leave(e, btn=button, c=color):
                btn.config(bg=c)
                
            button.bind("<Enter>", on_enter)
            button.bind("<Leave>", on_leave)
            
        # Clear button
        clear_button = tk.Button(
            self.window,
            text="Clear",
            font=("Arial", 16, "bold"),
            bg="#C0392B",
            fg="white",
            relief=tk.RAISED,
            pady=8,
            cursor="hand2",
            command=self.clear
        )
        clear_button.pack(fill=tk.X, padx=15, pady=10)
        
    def add_digit(self, digit):
        if self.should_reset:
            self.current_number = "0"
            self.should_reset = False
            
        if self.current_number == "0" and digit != ".":
            self.current_number = digit
        else:
            if digit == "." and "." in self.current_number:
                return
            self.current_number += digit
        self.update_display()
        
    def set_operation(self, op):
        if self.first_number is None:
            self.first_number = float(self.current_number)
            self.operation = op
            self.should_reset = True
        else:
            self.calculate()
            self.operation = op
            self.first_number = float(self.display["text"])
            self.should_reset = True
            
    def calculate(self):
        if self.operation is None or self.first_number is None:
            return
            
        try:
            second_number = float(self.current_number)
            if self.operation == "+":
                result = self.first_number + second_number
            elif self.operation == "-":
                result = self.first_number - second_number
            elif self.operation == "*":
                result = self.first_number * second_number
            elif self.operation == "/":
                if second_number == 0:
                    messagebox.showerror("Error", "Cannot divide by zero!")
                    self.clear()
                    return
                result = self.first_number / second_number
                
            # Format result
            if result.is_integer():
                result = int(result)
            else:
                result = "{:.2f}".format(result)
                
            self.current_number = str(result)
            self.first_number = None
            self.operation = None
            self.update_display()
            
            # Create and show video window after calculation
            self.create_video_window()
            
        except ValueError:
            messagebox.showerror("Error", "Invalid calculation!")
            self.clear()
            
    def clear(self):
        self.current_number = "0"
        self.first_number = None
        self.operation = None
        self.should_reset = False
        self.update_display()
        
    def update_display(self):
        self.display.config(text=self.current_number)
        
    def load_default_video(self):
        if self.cap is not None:
            self.is_playing = False
            self.cap.release()
        if not self.video_path or not os.path.exists(self.video_path):
            messagebox.showerror("Error", "Video file not found!")
            return

        self.cap = cv2.VideoCapture(self.video_path)
        self.play_video()
    
    def play_video(self):
        if self.cap is not None and not self.is_playing:
            self.is_playing = True
            self.video_thread = threading.Thread(target=self._play_video_thread)
            self.video_thread.daemon = True
            self.video_thread.start()
    
    def pause_video(self):
        self.is_playing = False
    
    def _play_video_thread(self):
        try:
            while self.is_playing:
                ret, frame = self.cap.read()
                if ret:
                    # Convert frame to RGB
                    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                    # Resize frame if needed
                    frame_rgb = cv2.resize(frame_rgb, (640, 480))
                    # Convert to PhotoImage
                    image = Image.fromarray(frame_rgb)
                    photo = ImageTk.PhotoImage(image=image)
                    
                    # Update video frame if window still exists
                    if self.video_window is not None:
                        self.video_frame.configure(image=photo)
                        self.video_frame.image = photo
                    
                    time.sleep(1/30)  # Limit to ~30 fps
                else:
                    # Video ended, reset to beginning
                    self.cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
                    if self.audio_playing:
                        pygame.mixer.music.play()  # Restart audio
        except Exception as e:
            print(f"Error in video playback: {e}")
            self.is_playing = False

    def _try_play_audio_for_video(self, video_path: str) -> None:
        """Attempt to extract audio via ffmpeg and play it; fall back to direct playback.

        This is best-effort and will not raise for expected failures.
        """
        # If ffmpeg is available and the file is a common container, try extraction
        video_lower = video_path.lower()
        use_extraction = shutil.which("ffmpeg") is not None and video_lower.endswith((".mp4", ".mkv", ".avi"))

        if use_extraction:
            audio_path = self.temp_dir / f"audio_{int(time.time())}.wav"
            try:
                subprocess.run([
                    "ffmpeg",
                    "-i", video_path,
                    "-vn",
                    "-acodec", "pcm_s16le",
                    "-ar", "44100",
                    "-ac", "2",
                    "-y",
                    str(audio_path),
                ], capture_output=True, check=True)

                # Remove other old audio files
                for old_file in self.temp_dir.glob("audio_*.wav"):
                    if old_file != audio_path:
                        try:
                            old_file.unlink()
                        except Exception:
                            pass

                pygame.mixer.music.load(str(audio_path))
                pygame.mixer.music.play()
                self.audio_playing = True
                return
            except Exception:
                # If extraction or playback failed, fall back to direct playback
                self.audio_playing = False

        # Fallback: try to load container directly (may or may not work)
        try:
            pygame.mixer.music.load(video_path)
            pygame.mixer.music.play()
            self.audio_playing = True
        except Exception:
            self.audio_playing = False
    
    def run(self):
        self.window.mainloop()
    
    def __del__(self):
        if self.cap is not None:
            self.is_playing = False
            self.cap.release()
            
        # Clean up temp directory
        if hasattr(self, 'temp_dir'):
            for file in self.temp_dir.glob("audio_*.wav"):
                try:
                    file.unlink()
                except:
                    pass
            try:
                self.temp_dir.rmdir()
            except:
                pass

if __name__ == "__main__":
    calc = Calculator()
    calc.run()
