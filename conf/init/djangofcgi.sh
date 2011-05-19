#!/bin/sh

PATH=/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin
NAME=djangofcgi.sh
DESC=djangofcgi.sh
SOCKFILE=/tmp/django.sock
PIDFILE=/tmp/django.pid
SU_USER=www-data
NUM_PROCS=3
MAX_REQUESTS=2000
CONN_OPTIONS="socket=${SOCKFILE}"
CONN_OPTIONS="host=0.0.0.0 port=9010"
EH_HOME="/home/antonio/eh"

start_fcgi() {
        cd $EH_HOME
        su ${SU_USER} -c "python manage.py runfcgi ${CONN_OPTIONS} pidfile=${PIDFILE} daemonize=true maxspare=${NUM_PROCS} maxrequests=${MAX_REQUESTS}"
}

stop_fcgi() {
        kill `cat ${PIDFILE}`
}


case "$1" in
  start)
        echo -n "Starting $DESC: "
                start_fcgi
        echo "$NAME."
        ;;
  stop)
        echo -n "Stopping $DESC: "
                stop_fcgi
        echo "$NAME."
        rm -f $PIDFILE
        ;;

  restart|force-reload)
        #
        #       If the "reload" option is implemented, move the "force-reload"
        #       option to the "reload" entry above. If not, "force-reload" is
        #       just the same as "restart".
        #
        echo -n "Restarting $DESC: "
                stop_fcgi
        sleep 1
                start_fcgi
        echo "$NAME."
        ;;

  *)
        N=/etc/init.d/$NAME
        # echo "Usage: $N {start|stop|restart|reload|force-reload}" >&2
        echo "Usage: $N {start|stop|restart|force-reload}" >&2
        exit 1
        ;;
esac

exit 0
