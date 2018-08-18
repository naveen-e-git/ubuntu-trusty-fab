 Vagrant.configure("2") do |config|
  config.hostmanager.enabled = true
  config.vm.box = "ubuntu/trusty64"
  config.vm.synced_folder "vpro_app", "/root"
  config.vm.network 'public_network'

############################################ INSTALLING CI SERVER ###############################################################################
  config.vm.define "ci" do |build|
   build.vm.hostname = 'build01.com'
   build.vm.network "private_network", ip: "192.168.10.10"
   build.vm.provision :shell, inline: <<-SHELL
   sudo sed -i 's/PasswordAuthentication no/PasswordAuthentication yes'/ /etc/ssh/sshd_config
   sudo systemctl restart ssh
   cd /root
   echo "installing python"
   sudo apt install python2.7 -y
   sudo apt update
   echo ""
   echo "#############################################################"
   sudo apt install python-pip -y
   sudo pip install --upgrade pip
   echo "##############################installing fabric##########################################"
   sudo apt install fabric -y
   echo "#######################################################################################"
   sudo pip install fabric
   fab ci_u
   SHELL
end

  config.vm.define "app" do |app|
   app.vm.hostname = 'app01.com'
   app.vm.network "private_network", ip: "192.168.10.12"
   app.vm.provision :shell, inline: <<-SHELL
   sudo sed -i 's/PasswordAuthentication no/PasswordAuthentication yes'/ /etc/ssh/sshd_config
   sudo systemctl restart ssh
   cd /root
   echo "installing python"
   sudo apt install python2.7 -y
   sudo apt update
   echo ""
   echo "#############################################################"
   sudo apt install python-pip -y
   sudo pip install --upgrade pip
   echo "##############################installing fabric##########################################"
   sudo apt install fabric -y
   echo "#######################################################################################"
   sudo pip install fabric
   fab app_u
   SHELL
end

  config.vm.define "db" do |db|
   db.vm.hostname = 'db01.com'
   db.vm.network "private_network", ip: "192.168.10.13"
   db.vm.provision :shell, inline: <<-SHELL
   sudo sed -i 's/PasswordAuthentication no/PasswordAuthentication yes'/ /etc/ssh/sshd_config
   sudo systemctl restart ssh
   cd /root
   echo "installing python"
   sudo apt install python2.7 -y
   sudo apt update
   echo ""
   echo "#############################################################"
   sudo apt install python-pip -y
   sudo pip install --upgrade pip
   echo "##############################installing fabric##########################################"
   sudo apt install fabric -y
   echo "#######################################################################################"
   sudo pip install fabric
   fab db_u
   SHELL
end

  config.vm.define "lb" do |lb|
   lb.vm.hostname = 'lb01.com'
   lb.vm.network "private_network", ip: "192.168.10.14"
   lb.vm.provision :shell, inline: <<-SHELL
   sudo sed -i 's/PasswordAuthentication no/PasswordAuthentication yes'/ /etc/ssh/sshd_config
   sudo systemctl restart ssh
   cd /root
   echo "installing python"
   sudo apt install python2.7 -y
   sudo apt update
   echo ""
   echo "#############################################################"
   sudo apt install python-pip -y
   sudo pip install --upgrade pip
   echo "##############################installing fabric##########################################"
   sudo apt install fabric -y
   echo "#######################################################################################"
   sudo pip install fabric
   fab lb_u
   SHELL
end

  config.vm.define "mem" do |mem|
   mem.vm.hostname = 'memcache.com'
   mem.vm.network "private_network", ip: "192.168.10.14"
   mem.vm.provision :shell, inline: <<-SHELL
   sudo sed -i 's/PasswordAuthentication no/PasswordAuthentication yes'/ /etc/ssh/sshd_config
   sudo systemctl restart ssh
   cd /root
   echo "installing python"
   sudo apt install python2.7 -y
   sudo apt update
   echo ""
   echo "#############################################################"
   sudo apt install python-pip -y
   sudo pip install --upgrade pip
   echo "##############################installing fabric##########################################"
   sudo apt install fabric -y
   echo "#######################################################################################"
   sudo pip install fabric
   fab memcache_u
   SHELL
end

  config.vm.define "rmq" do |rmq|
   rmq.vm.hostname = 'rmq01.com'
   rmq.vm.network "private_network", ip: "192.168.10.14"
   rmq.vm.provision :shell, inline: <<-SHELL
   sudo sed -i 's/PasswordAuthentication no/PasswordAuthentication yes'/ /etc/ssh/sshd_config
   sudo systemctl restart ssh
   cd /root
   echo "installing python"
   sudo apt install python2.7 -y
   sudo apt update
   echo ""
   echo "#############################################################"
   sudo apt install python-pip -y
   sudo pip install --upgrade pip
   echo "##############################installing fabric##########################################"
   sudo apt install fabric -y
   echo "#######################################################################################"
   sudo pip install fabric
   fab rabbitmq_u
   SHELL
end
end
