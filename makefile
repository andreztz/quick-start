build:
	python setup.py sdist bdist_wheel

clean:
	rm -r build
	rm  -r dist

release:
	twine upload --config-file ~/.pypirc dist/*

release-test:
	twine upload --repository-url https://test.pypi.org/legacy/ dist/*


