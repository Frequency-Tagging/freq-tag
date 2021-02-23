.. -*- mode: rst -*-

|GHActions|_ |Codecov|_ |CircleCI|_

.. |GHActions| image:: https://github.com/Frequency-Tagging/freq-tag/workflows/build/badge.svg
.. _GHActions: https://github.com/Frequency-Tagging/freq-tag/actions

.. |Codecov| image:: https://codecov.io/gh/Frequency-Tagging/freq-tag/branch/master/graph/badge.svg
.. _Codecov: https://codecov.io/gh/Frequency-Tagging/freq-tag

.. |CircleCI| image:: https://circleci.com/gh/Frequency-Tagging/freq-tag.svg?style=svg
.. _CircleCI: https://circleci.com/gh/Frequency-Tagging/freq-tag/tree/master

freq-tag - A template for mne-python compatible extensions
======================================================================

.. _mne-python: https://mne.tools

**freq-tag** is a template project for mne-python_ compatible
extensions.

*Thank you for cleanly contributing to the mne-python ecosystem!*

.. _documentation: https://mne.tools/freq-tag

Refer to the documentation_ to modify the template for your own mne-python
extension or follow this quick reference::

    $ git clone https://github.com/Frequency-Tagging/freq-tag.git mne-foo
    $ cd mne-foo
    $ # update mne_project_template_bootstrap.sh
    $ bash mne_project_template_bootstrap.sh
    $ rm mne_project_template_bootstrap.sh
    $ rm -rf .git
    $ git init && git add . && git commit -m 'Initial commit'
    $ git remote add origin https://github.com/your_remote/mne-foo.git
    $ git push origin master
    $ # Activate all CIs
