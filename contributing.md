# Steps to take when contributing

- Clone the repository (first time only) or update to the latest `master`.
- Create a new branch.
- Create (first time only) or update the conda environment using `environment.yml`.
- Use `pip` to install `freqtag` in the editable mode (first time only). 
- Make your changes.
- Check test coverage, run tests, build docs.
- Push to GitHub and open a PR.

## Creating/updating the conda environment

From root:

```sh
conda env update -n freqtag -f environment.yml --prune
```

Once the process is finished, activate the environment with

```sh
conda activate freqtag
```

All the other commands should be run within the `freqtag` environment.

## Install `freqtag` in the editable mode

From root

```
pip install -e .
```

## Check test coverage

From `freqtag`:

```sh
pytest --cov=freqtag tests
```

## Running tests

From root:

```sh
python -m pytest freqtag
```

## Building docs

From `doc`:

```sh
make html
```
