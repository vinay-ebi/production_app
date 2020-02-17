Production application
=============

- Instal
--
``` 
    - git clone  https://github.com/vinay-ebi/production_app.git
    - cd production_app
    - python setup.py  install
    - pip install -r requirements.txt
    - pip install .
``` 
 - Run application
    --
```
    - production_app
```
    
 
 - Example:
    --
```
    To use swager UI: http://localhost:8090/ensembl/handover
```
 
 - Run Test Case
    --
```
    - python -m pytest
```

 - Build docker image
  ---
   - sudo docker build  -t productionsrv:latest -f docker/Dockerfile .

 - Run Docker Container 
    --
   - sudo docker run  --network=host -it productionsrv:latest  -r handover -p 5000


-Submit and run background jobs with Rabbitmq, celery
=======

- Install
--------
```
- sudo apt-get install rabbitmq-server
- sudo service rabbitmq-server start
- pip install celery

```
- Start rabbitmq message broker, celery worker and flask
-------
```
- cd production_app	
- celery -A app.celery worker -Q handover --loglevel=info -n 'worker1%h'
- celery -A app.celery worker -Q datacheck --loglevel=info -n 'worker2%h'
- celery -A app.celery worker -Q dbcopy --loglevel=info -n 'worker3%h'
- celery -A app.celery worker -Q metadata  --loglevel=info -n 'worker4%h'
- production_app_api -p 8090 
```

-monitor celery worker using flower
--
- pip install flower 
-celery -A production_app.app_celery.celery  flower
-http://localhost:5555




- Example:
    --
    To use swager UI: http://localhost:8090/app/
    - 1: submit job to queue
        --
  ```
        
  http://localhost:5000/app/jobs
	
		Return the status and task_id submitted to queue
		---------------------------------
		-{ "status": "PENDING",  "task_id": "99081de1-2290-420d-96aa-0ca4c7221b22"}
  ```
    - 2: Get status and result for submitted job
        --
  ```

  ```






Hive initiation
======
- RUN HIVE config file to create HiveDB :

```
init_pipeline.pl Bio::EnsEMBL::Production::Pipeline::PipeConfig::CopyDatabase_conf -pipeline_url 'mysql://vinay:vinay@localhost/vinay_copy_database2' -hive_force_init 1
```

-RUN bekeeper.pl to submit the jobs
```
beekeeper.pl -url "mysql://vinay:vinay@localhost/vinay_copy_database2" -sync --keep_alive -sleep 0.5
```

-export Hive database URL used by production_app service
```
export SERVER_URIS_FILE=/home/vinay/Documents/Ensembl-Master/Projects/P3_rabbitmq_example/test_the_ensembl_srv/ensembl-prodinf-srv/server_uris.json
export HIVE_URI=mysql://vinay:vinay@localhost/vinay_copy_database2
```

