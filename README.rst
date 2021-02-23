.. -*- mode: rst -*-

|GHActions|_ |Codecov|_ |CircleCI|_

.. |GHActions| image:: https://github.com/mne-tools/mne-project-template/workflows/build/badge.svg
.. _GHActions: https://github.com/mne-tools/mne-project-template/actions

.. |Codecov| image:: https://codecov.io/gh/mne-tools/mne-project-template/branch/master/graph/badge.svg
.. _Codecov: https://codecov.io/gh/mne-tools/mne-project-template

.. |CircleCI| image:: https://circleci.com/gh/mne-tools/mne-project-template.svg?style=svg
.. _CircleCI: https://circleci.com/gh/mne-tools/mne-project-template/tree/master

mne-project-template - A template for mne-python compatible extensions
======================================================================

.. _mne-python: https://mne.tools

**mne-project-template** is a template project for mne-python_ compatible
extensions.

*Thank you for cleanly contributing to the mne-python ecosystem!*

.. _documentation: https://mne.tools/mne-project-template

Refer to the documentation_ to modify the template for your own mne-python
extension or follow this quick reference::

    $ git clone https://github.com/mne-tools/mne-project-template.git mne-foo
    $ cd mne-foo
    $ # update mne_project_template_bootstrap.sh
    $ bash mne_project_template_bootstrap.sh
    $ rm mne_project_template_bootstrap.sh
    $ rm -rf .git
    $ git init && git add . && git commit -m 'Initial commit'
    $ git remote add origin https://github.com/your_remote/mne-foo.git
    $ git push origin master
    $ # Activate all CIs
