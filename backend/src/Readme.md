# Setup on Linux

Start by creating an isolated virtual environment. 

```bash
python -m venv venv
source venv/bin/activate 
```

```bash
pip install -r requirements.txt
```

Start the webserver with the following command

```bash
./start.sh
```


# Setup on Windows

Start by creating an isolated virtual environment. 

```bash
python -m venv venv
.\venv\Scripts\activate.bat
```

```bash
pip install -r requirements.txt
```

Start the webserver with the following command

```bash
uvicorn main:app --reload
```


# Access
After starting open the following URL [http://127.0.0.1:8000/static/index.html](http://127.0.0.1:8000/static/index.html)

