"""Simple Valentine GUI with improved visuals (no name entry)."""
import tkinter as tk
from tkinter import messagebox
import tkinter.font as tkfont
import random


class ValentineApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Will You Be My Valentine? 💕")

        # Preferred window size
        win_w, win_h = 520, 420
        self.root.geometry(f"{win_w}x{win_h}")

        # Center the window on the screen
        self.root.update_idletasks()
        x = (self.root.winfo_screenwidth() // 2) - (win_w // 2)
        y = (self.root.winfo_screenheight() // 2) - (win_h // 2)
        self.root.geometry(f"{win_w}x{win_h}+{x}+{y}")

        # Fonts
        self.title_font = tkfont.Font(family="Helvetica", size=20, weight="bold")
        self.text_font = tkfont.Font(family="Helvetica", size=12)
        self.emoji_font = tkfont.Font(family="Segoe UI Emoji", size=36)

        self.root.configure(bg="#FFD7E8")

        # Main frame (pane)
        self.main_frame = tk.Frame(root, bg="#FFD7E8", padx=18, pady=18)
        self.main_frame.pack(fill=tk.BOTH, expand=True)

        # Title pane with decorative heart
        self.title_frame = tk.Frame(self.main_frame, bg="#FF6FAF", padx=12, pady=12)
        self.title_frame.pack(fill=tk.X, pady=(0, 14))

        self.heart_label = tk.Label(self.title_frame, text="💘", font=self.emoji_font, bg="#FF6FAF")
        self.heart_label.pack(side=tk.LEFT, padx=(6, 10))

        self.title_label = tk.Label(
            self.title_frame,
            text="Will You Be My Valentine?",
            font=self.title_font,
            bg="#FF6FAF",
            fg="white",
        )
        self.title_label.pack(side=tk.LEFT, anchor=tk.CENTER)

        # Message pane (static — no name entry)
        self.message_frame = tk.Frame(self.main_frame, bg="white", padx=14, pady=14, relief=tk.RIDGE, bd=2)
        self.message_frame.pack(fill=tk.BOTH, expand=True, pady=(0, 12))

        self.message_label = tk.Label(
            self.message_frame,
            text=self.default_message(),
            font=self.text_font,
            bg="white",
            fg="#C2185B",
            justify=tk.CENTER,
            wraplength=420,
        )
        self.message_label.pack(fill=tk.BOTH, expand=True)

        # Button pane with spacing and shadow effect
        self.button_frame = tk.Frame(self.main_frame, bg="#FFD7E8")
        self.button_frame.pack(fill=tk.X)

        self.yes_button = tk.Button(
            self.button_frame,
            text="💖 YES! 💖",
            font=("Helvetica", 12, "bold"),
            bg="#E91E63",
            fg="white",
            activebackground="#C2185B",
            activeforeground="white",
            padx=18,
            pady=8,
            relief=tk.RAISED,
            bd=3,
            command=self.yes_clicked,
        )
        self.yes_button.pack(side=tk.LEFT, padx=8)
        self.yes_button.bind("<Enter>", lambda e: self.on_hover(self.yes_button, "#FF4D84"))
        self.yes_button.bind("<Leave>", lambda e: self.on_hover(self.yes_button, "#E91E63"))

        self.no_button = tk.Button(
            self.button_frame,
            text="Maybe Not",
            font=("Helvetica", 12),
            bg="#BA68C8",
            fg="white",
            activebackground="#9C27B0",
            activeforeground="white",
            padx=16,
            pady=8,
            relief=tk.RAISED,
            bd=3,
            command=self.no_clicked,
        )
        self.no_button.pack(side=tk.LEFT, padx=8)
        self.no_button.bind("<Enter>", lambda e: self.on_hover(self.no_button, "#CE93D8"))
        self.no_button.bind("<Leave>", lambda e: self.on_hover(self.no_button, "#BA68C8"))

    def default_message(self):
        return (
            "I like you and I would love to spend\nValentine's Day with you!\n\nWhat do you say?"
        )

    def on_hover(self, widget, color):
        widget.config(bg=color)

    def yes_clicked(self):
        messagebox.showinfo("💕 Success! 💕", "Yay! You made me the happiest! 🎉\nHappy Valentine's Day! ❤️")

    def no_clicked(self):
        # Make the "No" button harder to click (move it) but safely within window
        messages = [
            "Are you sure?",
            "Think about it again!",
            "Give me another chance!",
            "Pretty please? 🥺",
            "I'm not giving up!",
            "Come onnnnn! 💕",
            "Don't be shy!",
            "Let's make memories together!",
            "You know you want to! 😉",
        ]

        messagebox.showwarning("Oh No!", random.choice(messages))

        # Temporarily remove pack layout, place randomly inside window bounds
        try:
            self.no_button.pack_forget()
        except Exception:
            pass

        # compute safe placement bounds
        win_w = self.root.winfo_width()
        win_h = self.root.winfo_height()
        btn_w = 120
        btn_h = 40
        max_x = max(20, win_w - btn_w - 20)
        max_y = max(120, win_h - btn_h - 40)
        x = random.randint(20, max_x)
        y = random.randint(120, max_y)

        self.no_button.place(x=x, y=y)

        # Restore original layout after a short delay
        def restore():
            try:
                self.no_button.place_forget()
            except Exception:
                pass
            self.no_button.pack(side=tk.LEFT, padx=8)

        self.root.after(2000, restore)


if __name__ == "__main__":
    root = tk.Tk()
    app = ValentineApp(root)
    root.mainloop()
