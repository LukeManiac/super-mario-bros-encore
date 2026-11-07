import os, json, textwrap, tkinter as tk
from tkinter import ttk, messagebox

cwd = os.path.dirname(os.path.abspath(__file__))

def make_dialog():
    dialog_text_value = dialog_text.get("1.0", "end-1c")
    dialog_id_value = dialog_id_var.get().strip()
    dialog_speaker_value = dialog_speaker_var.get()

    if not dialog_id_value:
        messagebox.showwarning("Missing Data", "You forgot to add the dialog ID!")
        dialog_id.focus_set()
        return

    wrapped_lines: list[str] = []

    # Split only on intentional line breaks.
    for line in dialog_text_value.split("\n"):
        # Remove trailing spaces, but preserve the actual line.
        line = line.rstrip()

        if line == "":
            wrapped_lines.append("")
            continue

        # Wrap this individual line at 40 characters.
        wrapped_lines.extend(textwrap.wrap(line, width=40, break_long_words=False, break_on_hyphens=False, replace_whitespace=False, drop_whitespace=True))

    # Turn the preserved/wrapped lines into literal \n characters.
    dialog_text_formatted: list[str] = []

    for line_index, line in enumerate(wrapped_lines):
        dialog_text_formatted.extend(line.rstrip().lower())

        if line_index < len(wrapped_lines) - 1:
            # A blank line already represents the intentional linebreak,
            # so don't add an extra wrapping linebreak before it.
            if line != "" and wrapped_lines[line_index + 1] == "":
                continue

            dialog_text_formatted.append("\n")

    result = (
        f'"{dialog_id_value}":{{\n'
        f'    "speaker":"{dialog_speaker_value.lower()}",\n'
        f'    "dialog":{json.dumps(dialog_text_formatted,separators=(",",":"))}\n'
        f'}}'
    )

    result_text.config(state="normal")
    result_text.delete("1.0", tk.END)
    result_text.insert("1.0", result)
    result_text.config(state="disabled")
    copy_result()

def on_mousewheel(event):
    dialog_text.yview_scroll(-int(event.delta / 120), "units")
    return "break"

def copy_result():
    root.clipboard_clear()
    root.clipboard_append(result_text.get("1.0", "end").rstrip())
    root.update()
    messagebox.showinfo("Success", "Successfully copied result to clipboard!")

with open(os.path.join(cwd, "dialog display.json"), encoding="utf-8") as dialog_json:
    dialog_data = json.load(dialog_json)
    dialog_npcs = [npc.title() for npc in list(dialog_data["npcprops"].keys())]

root = tk.Tk()
root.title("Dialog Maker")
root.geometry("700x700")

dialog_text_var = tk.StringVar()
dialog_id_var = tk.StringVar()
dialog_speaker_var = tk.StringVar(value=dialog_npcs[0])

main = ttk.Frame(root, padding=10)
main.pack(fill="both", expand=True)

# Dialog label
ttk.Label(main, text="Dialog").pack(anchor="w")

# Dialog text area with scrolling
dialog_frame = ttk.Frame(main)
dialog_frame.pack(fill="both", expand=True, padx=5, pady=5)

dialog_text = tk.Text(dialog_frame, wrap="word", height=12)
dialog_text.pack(side="left", fill="both", expand=True)

dialog_scrollbar = ttk.Scrollbar(dialog_frame, orient="vertical", command=dialog_text.yview)
dialog_scrollbar.pack(side="right", fill="y")

dialog_text.bind("<MouseWheel>", on_mousewheel)
dialog_text.bind("<Button-4>", lambda *_: dialog_text.yview_scroll(-1, "units"))
dialog_text.bind("<Button-5>", lambda *_: dialog_text.yview_scroll(1, "units"))
dialog_text.configure(yscrollcommand=dialog_scrollbar.set)

# Dialog ID
ttk.Label(main, text="Dialog ID").pack(anchor="w")

dialog_id = ttk.Entry(main, textvariable=dialog_id_var)
dialog_id.pack(fill="x", padx=5, pady=5)

# Speaker
ttk.Label(main, text="Speaker").pack(anchor="w")

dialog_speaker = ttk.Combobox(main, textvariable=dialog_speaker_var, values=dialog_npcs, state="readonly")
dialog_speaker.pack(fill="x", padx=5, pady=5)

# Make Dialog button
make_button = ttk.Button(main, text="Make Dialog", command=make_dialog)
make_button.pack(fill="x", padx=5, pady=5)

# Result
ttk.Label(main, text="Result").pack(anchor="w")

result_frame = ttk.Frame(main)
result_frame.pack(fill="both", expand=True, padx=5, pady=5)

result_text_frame = ttk.Frame(result_frame)
result_text_frame.pack(fill="both", expand=True)

result_text = tk.Text(result_text_frame, wrap="none", height=8)
result_text.pack(side="left", fill="both", expand=True)

result_scrollbar = ttk.Scrollbar(result_text_frame, orient="vertical", command=result_text.yview)
result_scrollbar.pack(side="right", fill="y")

result_horizontal_scrollbar = ttk.Scrollbar(result_frame, orient="horizontal", command=result_text.xview)
result_horizontal_scrollbar.pack(fill="x")

result_text.configure(xscrollcommand=result_horizontal_scrollbar.set, yscrollcommand=result_scrollbar.set)

result_text.config(state="disabled")

result_copy = ttk.Button(result_frame, text="Copy Result", command=copy_result)
result_copy.pack(fill="x", pady=(5, 0))

root.mainloop()