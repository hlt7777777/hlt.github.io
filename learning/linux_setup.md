## 虚拟机的安装
需要准备的安装包：
1. VMware Workstation (密钥 5A02H-AU243-TZJ49-GTC7K-3C61N)  
1. xshell
1. xftp

安装VMware、Linux（centOS 7）

#### Linux账号
- root 123456
- hlt hlt123456

#### 网络连接
1. 由`NAT模式`改为`桥接模式`,复制物理网络连接状态；
1. 查看`ip a`，直接 在xshell中用IP远程连接虚拟机

#### 修改IP名
 打开hosts，注释掉已有的，添加IP地址
```
vim /etc/hosts   #修改IP代称
172.16.11.180 bigdata   #给hosts文档添加这行
```
---
## MySQL的安装
#### 查看系统版本
shell中输入`cat /etc/redhat-release`;
得到`CentOS Linux release 7.4.1708 (Core) `
#### MySQL的安装
1. 下载安装
```
wget http://dev.mysql.com/get/mysql-community-release-el7-5.noarch.rpm  #下载
rpm -ivh mysql-community-release-el7-5.noarch.rpm  #解压缩
#安装MySQL
yum install mysql
yum install mysql-devel
yum install mysql-community-server
```
2. 重启MySQL服务，设置密码
```
$service mysqld restart  #重启MySQL
$mysql -u root  #第一次进入MySQL
mysql>set password for 'root'@'localhost' =password('123456') WITH GRANT OPTION; #为root用户添加远程连接
```
3. 关闭防火墙
```
firewall-cmd --state  #查看防火墙状态为running
systemctl stop firewalld.service   #关闭防火墙
```
---
## superset的安装
#### 安装anaconda
下载Linux版本的anaconda，并安装reboot。
#### 部署superset
##### 安装依赖包
```
yum -y install gcc gcc-c++ libffi-devel python-devel python-pip python-wheel openssl-devel libsasl2-devel openldap-devel
```
##### 创建虚拟环境，并安装设置superset
```
conda create -n superset python=3.4
source activate superset
pip install superset -i  https://pypi.douban.com/simple
fabmanager create-admin --app superset
superset db upgrade
superset init
superset runserver
source deactivate
```
##### 修改superset汉化
1. 在路径`/root/anaconda3/envs/superset/lib/python3.4/site-packages/superset`中修改Setup default language默认为`zh`
1. 在`/root/anaconda3/envs/superset/lib/python3.4/site-packages/superset/translations/`中生成`zh/LC_MESSAGES/messages.mo`；messages.mo文件自己下载。
 



