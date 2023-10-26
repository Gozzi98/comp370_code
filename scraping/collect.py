from pathlib import Path
import requests
import bs4

def get_celebrity_html_data(name):
    fpath = Path(f"{name}.html")

    if not fpath.exists():
        data = requests.get(f"https://www.whosdatedwho.com/dating/{name}")

        with open(fpath, "w") as f:
            f.write(data.text) 
    with open(fpath, "r") as f:
        return f.read()

def main(): 
    name = "ryan-reynolds"
    html_data = get_celebrity_html_data(name)

    print(html_data)

if __name__ == "__main__":  
    main()

