#!/bin/bash
#chkconfig:1234 90 60
# 给出 启动/关闭级别，1,2,3,4代表在设置在那个level中是on的，也可以写一个横线，表示一个都不on，后面两个数字代表S和K的默认序号
# Default-Start:     2 3 4 5
# Default-Stop:      S 0 1 6


# 描述所启动的服务的作用
# description: Saves and restores system entropy pool for \
# higher quality random number generation
servername=myservice
serverdir=/opt/myservice
binpath=/opt/myservice/myservice.sh

prog=$(basename $binpath)
. /etc/init.d/functions

restart() {
        stop
        start
}
reload() {
        stop
        start
}
start() {
echo -n $"Starting $daemon:"
        daemon $binpath start
        retval=$?
        echo
        [ $retval -eq 0 ]
}

stop() {
echo -n $"Stopping $daemon:"
        daemon $binpath stop
        retval=$?
        echo
        [ $retval -eq 0 ]
}

ha_status() {
        #status $prog
        status $prog
        ps -ef|grep $prog && exit 0
}

case "$1" in

     start)
        $1
     ;;
     stop)
        $1
     ;;
     reload)
        $1
     ;;
     restart)
        $1
     ;;
     status)
        ha_status
     ;;
     *)
        echo "Usage:$0 {start|stop|reload|restart|status}"
        exit 1
esac

#!/bin/bash
# chkconfig: 35 95 1
# description: script to start/stop smsafe
case $1 in
start)
sh /opt/startsms.sh
;;
stop)
sh /opt/stopsms.sh
;;
*)
echo "Usage: $0 (start|stop)"
;;
esac