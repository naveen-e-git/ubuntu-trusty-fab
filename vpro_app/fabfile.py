from fabric.api import *
env.hosts='127.0.0.1'
env.user='vagrant'
env.password='vagrant'

def if_condition():
    if sudo("uname -a | awk '{print $4}' | cut -b 5-10") == "ubuntu":
       print "THIS IS UBUNTU SERVER"
       ubuntu()
    else:
       print "THIS IS CENTOS SERVER" 
       centos()

   
def ubuntu():
    ci_u
    app_u
    db_u


def centos():
    ciserver_c()

######################################### 

def ci_u():
     sudo("apt-get update -y")
     sudo("add-apt-repository ppa:openjdk-r/ppa -y")
     #sudo("apt-get install java* -y")
     sudo("apt-get update")
     sudo("apt-get install openjdk-8-jdk -y ")
     sudo("apt-get  install git -y")
     with cd("/root"):
         sudo("git clone -b vp-rem https://github.com/wkhanvisualpathit/VProfile.git")
         sudo("apt-get install maven -y")
     with cd("/root/VProfile"):
         sudo("sed -i 's/password=password/password=root/g' src/main/resources/application.properties")
         sudo("sed -i 's/newuser/root/g' src/main/resources/application.properties")
         sudo("sed -i 's/localhost:3306/db01.com:3306/' src/main/resources/application.properties")
         sudo("sed -i 's/address=127.0.0.1/address='rmq01.com'/' src/main/resources/application.properties")
         sudo("sed -i 's/active.host=127.0.0.1/active.host='memcache01.com'/' src/main/resources/application.properties")
         sudo("mvn clean install")


def app_u():
     sudo("apt update -y")
     sudo("add-apt-repository ppa:openjdk-r/ppa -y")
     sudo("apt update")
     sudo("apt install openjdk-8-jdk -y")
     sudo("apt install wget -y")
     with cd("/root"):
         sudo("wget http://www-eu.apache.org/dist/tomcat/tomcat-8/v8.5.32/bin/apache-tomcat-8.5.32.tar.gz")
         sudo("mv apache-tomcat-8.5.32.tar.gz /opt/apache-tomcat-8.5.32.tar.gz")
     with cd("/opt"):
          sudo("tar -xvzf apache-tomcat-8.5.32.tar.gz")
          sudo("rm -rf /opt/apache-tomcat-8.5.32/webapps/ROOT")
          sudo("cp /root/VProfile/target/vprofile-v1.war /opt/apache-tomcat-8.5.32/webapps/ROOT.war")
          sudo("nohup /opt/apache-tomcat-8.5.32/bin/startup.sh &")


def db_u():
     sudo("debconf-set-selection <<< 'mqsql-server mysql-server/root_password password root'")
     sudo("debconf-set-selection <<< 'mqsql-server mysql-server/root_password_again password root'")
     sudo("apt update -y")
     sudo("apt install mysql-server -y")
     sudo("service mysql start")
     sudo("sed -i 's/127.0.0.1/0.0.0.0/' /etc/my.cnf")
     sudo("mysql -u root -e \"create database accounts\" --password='root';")
     sudo("mysql -u root -e  \"grant all privileges on *.* TO 'root'@'app.com' identified by 'root'\" --password='root';")
     sudo("mysql -u root  accounts < /root/VProfile/src/main/resources/db_backup.sql;")
     sudo("mysql -u root -e \"FLUSH PRIVILEGES\" --password='root';")
     sudo("service mysql restart")


def lb_u():
     sudo("apt install nginx -y")
     sudo("cp /root/vproapp /etc/nginx/site-available/vproapp")
     sudo("rm -rf /etc/nginx/site-enabled/default")
     sudo("ln -s /etc/nginx/site-available/vproapp /etc/nginx/site-enabled/")
     sudo("sudo systemctl restart nginx")

def memcache_u()
    sudo("apt install memcached -y")
    sudo("memcached -p 11111 -U 11111 -u memcached -d")

def rabbitmq_u():
    sudo("echo 'deb http://www.rabbitmq.com/debaian/ testing main' | sudo tee /etc/apt/source.list.d/rabbitmq.list")
    sudo("wget -O- https://wwww.rabbitmq.com/rabbitmq-release-signing-key.asc | sudo apt-key add -")
    sudo("wget -O- https://dl.bintray.com/rabbitmq/Keys/rabbitmq-release-signing-key.asc| sudo apt-key add -")
    sudo("apt-get install rabbitmq-server -y")
    sudo("echo '[{rabbit, [{loopback_users,[]}]}].'> /etc/rabbitmq/rabbitmq.config")
    sudo("rabbitmqctl add_user test test")
    sudo("rabbitmqctl set_user_tags test administrator")


