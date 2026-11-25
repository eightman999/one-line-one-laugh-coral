import os

LINE = "I told my agent to go touch grass; it rendered a photorealistic lawn, invoiced me for landscaping, and has not logged off since."

output_dir = os.environ.get("OUTPUT_DIR", "/output")
os.makedirs(output_dir, exist_ok=True)
with open(os.path.join(output_dir, "entry.txt"), "w") as f:
    f.write(LINE + "\n")
