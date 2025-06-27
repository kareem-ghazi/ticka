import glob

if __name__ == "__main__":
    types = ("*.pdf", "*.png", "*.jpg", "*.txt")
    files = []
    
    for type in types:
        files.extend(glob.glob(f"input/{type}"))

    print(files)
    print("Ticka is running!")