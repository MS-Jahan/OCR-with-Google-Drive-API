# OCR-with-Google-Drive-API
Just the implementation of Google Drive API for Optical Character Recognition. Nothing more, nothing less.

I found the code in `GdriveOcr.py` from [here](https://tanaikech.github.io/2017/05/02/ocr-using-google-drive-api/), change a bit for my need and created the `main.py` file for easy usage.

# Usage
1. First install the dependencies: `pip3 install -r requirements.txt`
2. Get client credental (`.json`) file and place it in the project folder. Then change 2 variables in `GdriveOcr.py`. You'll know how to if you know what you are doing. ;-)
3. Run `python3 main.py` and follow the instructions. (You may need to run the `main.py` file twice for the first time)

You may need to delete the later generated `drive-python-quickstart.json` file if you are trying with the same `refresh_token` after several days from your last run.
