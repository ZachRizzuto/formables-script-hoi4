import tqdm
import time
from tkinter import Tk, filedialog

def pick_input_file():
    root = Tk()
    root.withdraw()
    root.attributes("-topmost", True)

    file_path = filedialog.askopenfilename(title="Select state ID text file", filetypes=[("Text files", "*.txt")])
    root.destroy()
    return file_path



def main():
    input_file = pick_input_file()

    if not input_file:
        print("No file selected. Terminating.")
        return
    with open(input_file, "r") as f:
        states = [line.strip() for line in f if line.strip()]
    
    if not states:
        print("File empty. Terminating.")
        return

    total_steps = len(states)*3
    with tqdm.tqdm(total=total_steps, desc="Generating HOI4 logic", unit="step", dynamic_ncols=True) as pbar:
        with open("./log_1.txt", "w") as f:
            pbar.desc = "Generating log 1"
            for state in states:
                f.write(f"state={state}\n")
                time.sleep(int(state)/100000)
                pbar.update(1)
        with open("./log_2.txt", "w") as f:
            pbar.desc = "Generating log 2"
            for state in states:
                f.write(f"controls_state={state}\n")
                time.sleep(int(state)/100000)
                pbar.update(1)

        with open("./log_3.txt", "w") as f:
            pbar.desc = "Generating log 3"
            for state in states:
                f.write(f"{state}={{ add_core_of=ROOT }}\n")
                time.sleep(int(state)/100000)
                pbar.update(1)
if __name__ == "__main__":
    main()