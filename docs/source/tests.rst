Tests
=============

Launching Tests
------------------
.. code-block:: bash

    pytest --cov=. --cov-report=term-missing

Current coverage > **80%**

Structure
------------------
* Lettings/tests: Contains tests for the lettings app (models and views).
* Profiles/tests: Contains tests for the profiles app (models and views).
* OC_lettings_site: Contains tests for views, errors.
