# 


## 1. construct the project files

- copy template.py
- rename project_name
- run `python template.py` in the terminal

```shell
python template.py
```


## 2. Create a virtual environment & a requirement.txt file

Step 1: create virtual environment

```shell
python -m venv venvTextSumm
# or 
virtualenv venvTextSumm -p python3.9
```

```shell
source venvTextSumm/bin/activate
```

Step 2: check your python version if you want to

```shell
python --version
```

Step 4:
modif your requirements.txt
> Note: if `torch` is needed, you need to install independently in the terminal. Add `torch` to requirements.txt before deployment
> 
> Note:` -e .` it will tragger the setup.py file, delete it before deployment


## 4. setup.py

- copy setup.py
- change name
```python
PROJECT_NAME = "TextSummarizer"
AUTHOR_USER_NAME = "Zewen-Yang"
```


## 5. Run `requirements.txt`

```shell
pip install -r requirements.txt
```


## 6. Customize `utils/common.py, exception.py`

- copy `common.py` and `exception.py`


## 7. Conduct the training experiment in Colab

- `TextSummarizer.ipynb`

