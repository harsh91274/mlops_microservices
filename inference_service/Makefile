.PHONY: run install clean check runner
.DEFAULT_GOAL:=runner

run: install
	cd app && poetry run python run.py

install: pyproject.toml
	poetry install

clean:
	- for /d /r . %%d in (__pycache__) do @rmdir /s /q "%%d"

check:
	- poetry run flake8 app/

runner: check run clean