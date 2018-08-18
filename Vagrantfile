 Vagrant.configure("2") do |config|
  config.hostmanager.enabled = true
  config.vm.box = "ubuntu/xenial64"
  config.vm.synced_folder "vpro_app", "/root"
  config.vm.network 'public_network'

############################################ INSTALLING CI SERVER ###############################################################################
  config.vm.define "ci" do |build|
   build.vm.hostname = 'build.com'
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
   fab ciserver_u
   SHELL
end

  config.vm.define "app" do |app|
   app.vm.hostname = 'app.com'
   app.vm.network "private_network", ip: "192.168.10.11"
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

  config.vm.define "app" do |app|
   app.vm.hostname = 'app.com'
   app.vm.network "private_network", ip: "192.168.10.11"
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
   fab db_u
   SHELL
end
end
