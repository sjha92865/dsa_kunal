
Ansible is configuration  tool while teraform is provisioning management tool.
i.e for creating instances we would use teraform for installing packages or tools like nginx and all we use Ansible.
Chef vs Ansible
Ansible works on push based mechanism that means we push the updates directly while chef fetches the configuration
and then updates and all.
Need to install ansible on master and then push the update on all other computers using ssh connection.
Same key pair use krna for all master and slaves
register krwa skte ho agar different keys ka use kr liya ho to.
/etc/ansible/hosts me group bna skte ho dev and prod env ka, with list of servers
[servers]
server_1 ansible_hosts=x.y.z, variable_name=ansible_hosts
scp se local se server pe private_key jo download kiya tha, daal do.
[servers:vars]
ansible_ssh_private_key_file=location
ansible servers -a "free -h", this is for adhoc command, will give the ram utilised and all.
adhoc commands are great for the command that you repeat rarely.
ansible modules are set of commands that can be control system or run system commands
ansible all -m ping -u ubuntu
similarly can run sudo apt update command as well
group change krdo agr alg alg krna hai kuch execution.
can put hostnames as well instead of ips.
ansible prd -m ping-->unreachable due to not having variables to connect
ansible inventory --list
[all:vars],[server:vars]
mkdir playbook
vim abc_play.yml --> playbook runs tasks, where-->on server
Creating a File

ubuntu@ip-172-31-91-124:~/ansible/playbooks$ cat create_file.yml
---
- name: This playbook will create a file
hosts: all
become: true
tasks:
- name: creating a file
file:
path: /home/ubuntu/testdemo2.txt
state: touch
ansible-playbook -v abc_play.yml, -v is verbose shows output of the playbook.
 
