build:
	python setup.py sdist bdist_wheel

clean:
	rm -r build
	rm  -r dist

release:
	twine upload --repository-url https://upload.pypi.org/legacy/ dist/*

release-test:
	twine upload --repository-url https://test.pypi.org/legacy/ dist/*


