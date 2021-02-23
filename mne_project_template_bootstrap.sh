PKG_NAME=freq-tag
PYTHON_NAME=freqtag
GH_NAME=Frequency-Tagging

unameOut="$(uname -s)"

# Linux or CygWin/MinGW on Windows (but also anything but MacOS or OS X)
if [[ "${unameOut}" != "Darwin" ]]; then
	git grep -l 'mnetemplate' | xargs sed -i 's/mnetemplate/'"${PYTHON_NAME}"'/g'
	git grep -l 'mne-template' | xargs sed -i 's/mne-template/'"${PKG_NAME}"'/g'
	sed -i 's/mne-tools/'"${GH_NAME}"'/g' README.rst
	sed -i 's/mne-project-template/'"${PKG_NAME}"'/g' README.rst
	sed -i 's/mne-tools/'"${GH_NAME}"'/g' setup.py
	sed -i 's/mne-project-template/'"${PKG_NAME}"'/g' setup.py
# MacOS or OS X
else
    git grep -l 'mnetemplate' | xargs sed -i ' ' -e 's/mnetemplate/'"${PYTHON_NAME}"'/g'
    git grep -l 'mne-template' | xargs sed -i ' ' -e 's/mne-template/'"${PKG_NAME}"'/g'
    sed -i ' ' -e 's/mne-tools/'"${GH_NAME}"'/g' README.rst
    sed -i ' ' -e 's/mne-project-template/'"${PKG_NAME}"'/g' README.rst
    sed -i ' ' -e 's/mne-tools/'"${GH_NAME}"'/g' setup.py
    sed -i ' ' -e 's/mne-project-template/'"${PKG_NAME}"'/g' setup.py
fi
mv mnetemplate ${PYTHON_NAME}
