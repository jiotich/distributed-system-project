BIN=imago_env/bin/

venv:
	(python3 -m venv imago_env)

install:
	$(BIN)pip install -r requirements.txt