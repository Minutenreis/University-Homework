import os

allFiles = os.listdir("voll")
withoutGitignore = [f for f in allFiles if f != ".gitkeep"]
for f in withoutGitignore:
    os.remove(f"voll/{f}")