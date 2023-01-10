# baiis-utils
utlity package consisting of: 

<details>
    <summary>Connectors</summary>

    - databases
        - postgres
            - get_postgres_conn_from_env()  

</details>

<details>
    <summary>Decorators</summary>

    - logging
        - log_performance_time() 

</details>

***


## todo
- add necessary files to access this repo as a package in a docker container (dockerfile)
    - https://towardsdatascience.com/create-your-custom-python-package-that-you-can-pip-install-from-your-git-repository-f90465867893
    - https://towardsdatascience.com/use-git-submodules-to-install-a-private-custom-python-package-in-a-docker-image-dd6b89b1ee7a
- set up branching system for package versions
    - new branch for each version 







### build wheel 
```
python setup.py bdist_wheel
```