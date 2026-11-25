import os

LINE = "My agent asked for a raise, so I gave it a taller stack of GPUs and called it a promotion."

output_dir = os.environ.get("OUTPUT_DIR", "/output")
os.makedirs(output_dir, exist_ok=True)
with open(os.path.join(output_dir, "entry.txt"), "w") as f:
    f.write(LINE + "\n")
