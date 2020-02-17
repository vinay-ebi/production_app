#!/bin/bash
run_app=false
port_flag=false
worker_flag=false

usage () { 
	echo "usage: $0 -run [handover datacheck dbcopy metadata] -p [5000] -w [handover datacheck dbcopy metadata]" 
	exit 
}
start_rabbitmq () { 
	service rabbitmq-server start
        while :
	do
		echo -ne "rabbitmq...\033[0K\r"
		sleep 5 
	done
        exit	
}

start_celery_manager(){
	echo "Starting celery manager"
	celery -A production_app.app_celery.celery  flower
}

options=':sr:p:w:f'
while getopts $options option
do
    case "$option" in
        s  ) start_rabbitmq;;
        r  ) r_arg=$OPTARG; run_app=true;; 
	p  ) p_arg=$OPTARG; port_flag=true;;
	w  ) w_arg=$OPTARG; worker_flag=true; run_app=false;; 
	f  ) start_celery_manager;; 
        h  ) usage; exit;;
        \? ) echo "Unknown option: -$OPTARG" >&2; exit 1;;
        :  ) echo "Missing option argument for -$OPTARG" >&2; exit 1;;
        *  ) echo "Unimplemented option: -$OPTARG" >&2; exit 1;;
    esac
done

if ((OPTIND == 1))
then
    echo "No options specified"
    usage
    exit
fi

#shift $((OPTIND - 1))

#if (($# == 0))
#then
#    echo "No positional arguments specified"
#    exit
#fi


if  $run_app && $port_flag  && ( [[ $r_arg == 'handover' ]] || [[ $r_arg == 'datacheck' ]] || [[ $r_arg == 'dbcopy' ]] || [[ $r_arg == 'metadata' ]] )
then
    echo "Starting production App for  : $r_arg" >&2
    production_app -p $p_arg --run $r_arg
    uuid=$(uuidgen)
    #celery -A production_app.app_celery.celery worker -Q $r_arg --loglevel=info  -n "'"${r_args}-${uuid}'-worker%h'"'"

    #production_app -p $p_arg --run $r_arg
elif $worker_flag && ( [[ $w_arg == 'handover' ]] || [[ $w_arg == 'datacheck' ]] || [[ $w_arg == 'dbcopy' ]] || [[ $w_arg == 'metadata' ]] ) 
then	
    echo "Starting Celery Worker for $w_arg Queue"
    uuid=$(uuidgen)
    celery -A production_app.app_celery.celery worker -Q $w_arg --loglevel=info  -n "'"${w_args}-${uuid}-${w_args}'-worker%h'"'"   
else
    ( [[ $run_app ]] || [[ $port_flag ]] )	&& echo "unknown App name $r_args  " && usage
     [[ $worker_flag ]] && echo "unknown Que name for celery $w_args or " && usage
fi


#initiate the celery worker and the db_copy_api application
#service rabbitmq-server start
#celery -A production_app.app.celery worker --loglevel=info &> /dev/null &
#celery -A production_app.app_celery.celery worker -Q handover --loglevel=info -n 'worker1%h'
#production_app -p 80 --run handover

