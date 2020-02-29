import re

text = 'PythonPythonCosTam'

def wstaw(text):
    X = re.sub(r"(\w)([A-Z])", r"\1 \2", text)
    return X

a = wstaw(text)
print(a)
