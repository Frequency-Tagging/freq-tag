# Steps to take when contributing

- Clone the repository (first time only) or update to the latest `master`.
- Create a new branch.
- Create (first time only) or update the conda environment using `environment.yml`.
- Use `pip` to install `freqtag` in the editable mode (first time only). 
- Make your changes.
- Check test coverage, run tests, build docs.
- Push to GitHub and open a PR.

The first four steps are described below in detail.

## Creating/updating a conda virtual environment

Open a terminal, clone the repository, and cd into the repositories root folder.

From root folder:

```sh
conda env update -n freqtag -f environment.yml --prune
```

Once the process is finished, activate the conda environment with

```sh
conda activate freqtag
```

All the other commands should be run with the activated `freqtag` conda environment.

## Install `freqtag` package in editable mode

From root folder:

```
pip install -e .
```

## Check test coverage

cd to `freqtag` folder:

```sh
pytest --cov=freqtag tests
```

## Running tests

cd to root folder:

```sh
python -m pytest freqtag
```

## Building docs

cd to `doc` folder:

```sh
make html
```


# Deploying the package

## PyPI

- build
- check
- [upload to TestPyPI]
- upload to PyPI

From root:

```sh
python setup.py sdist bdist_wheel
twine check dist/*
[twine upload --repository testpypi dist/*]
twine upload dist/*
```
