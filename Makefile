help:
	@echo "  deps        install dependencies using pip"
	@echo "  clean       remove compiled files"
	@echo "  lint        check style with flake8"

deps:
	sudo easy_install pip && \
	pip install -r requirements.txt

clean:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +

lint:
	flake8 .
