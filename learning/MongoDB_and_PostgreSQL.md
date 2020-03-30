

#### MongoDB 和 PostgreSQL 之间的区别
MongoDB 和 PostgreSQL 是数据库系统的两个热门选择。

MongoDB 是一种 NoSQL 文档数据库，用于处理 JSON 和存储无架构数据。 它适用于实现灵活性和处理非结构化数据、缓存实时分析以及进行水平缩放。
PostgreSQL（有时称为 Postgres）是一种 SQL 关系数据库，着重于扩展性和标准符合性。 现在，它也可以处理 JSON，但通常更适合处理结构化数据、进行垂直缩放以及符合 ACID 的需求，例如电子商务和金融交易。

架构：
PostgreSQL ：表 | 列 | 值 | 记录。
MongoDB (NoSQL) ：集合 | 键 | 值 | 文档。

选择的数据库类型应取决于将使用该数据库的应用程序的类型。 我们建议你查看结构化和非结构化数据库的优点和缺点，并根据用例进行选择。 除了 PostgreSQL 和 MongoDB，还可以考虑其他几种数据库系统。

#### 安装 PostgreSQL
要安装 PostgreSQL，请执行以下操作：
打开终端（即 Ubuntu 18.04）。
更新 Ubuntu 包：`sudo apt update`
更新该包后，使用以下命令安装 PostgreSQL（和 -contrib 包，其中包含一些有用的实用程序）：`sudo apt install postgresql postgresql-contrib`
确认安装并获取版本号：`psql --version`
安装 PostgreSQL 后，需要知道以下 3 个命令：
`sudo service postgresql status` 用于检查数据库的状态。
`sudo service postgresql start` 用于开始运行数据库。
`sudo service postgresql stop` 用于停止运行数据库。

##### PostgreSQL 用户设置
默认管理员用户 postgres 需要分配的密码才能连接到数据库。 要设置密码，请执行以下操作：
1. 输入命令：`sudo passwd postgres`
2. 系统将提示你输入新密码。
3. 关闭并重新打开终端。

##### 通过 psql shell 运行 PostgreSQL
psql 是 PostgreSQL 的基于终端的前端。 它使你能够以交互方式键入查询，将其发布到 PostgreSQL，并查看查询结果。 或者，输入也可由文件提供。 此外，它还提供了许多元命令和各种类似于 shell 的功能，便于编写脚本和自动执行各种任务。

要启动 psql shell，请执行以下操作：
启动 postgres 服务：`sudo service postgresql start`
连接到 postgres 服务，并打开 psql shell：`sudo -u postgres psql`

成功输入 psql shell 后，将显示更改为如下所示的命令行：`postgres=#`
>或者，也可以通过使用 su - postgres 切换为 postgres 用户，然后输入命令 psql 来打开 psql shell。

要退出 postgres=# enter，请使用 \q 或使用快捷键：Ctrl+D

要查看在 PostgreSQL 安装上创建的用户帐户，请在终端上使用 `psql -c "\du"`；如果已打开 psql shell，则仅使用 \du。 此命令将显示以下列：帐户用户名、角色属性列表和角色组成员。 要返回命令行，请输入：q。

#### 安装 MongoDB

要安装 MongoDB，请执行以下操作：
1. 打开终端（即 Ubuntu 18.04）。
2. 更新 Ubuntu 包：`sudo apt update`
3. 更新该包后，使用以下命令安装 MongoDB：`sudo apt-get install mongodb`
4. 确认安装并获取版本号：`mongod --version`

安装 MongoDB 后，需要知道以下 3 个命令：
1. `sudo service mongodb status` 用于检查数据库的状态。
2. `sudo service mongodb start` 用于开始运行数据库。
3. `sudo service mongodb stop` 用于停止运行数据库。
>你可能会看到在教程或文章中使用了命令 `sudo systemctl status mongodb`。 为了保持轻量，WSL 不包括 systemd（Linux 中的服务管理系统）。 它改为使用 SysVinit 在计算机上启动服务。 你应该不会注意到有什么区别，但是如果教程建议使用 `sudo systemctl`，请改用 `sudo /etc/init.d/`。 例如，对于 WSL，sudo systemctl status mongodb 应改用 `sudo /etc/inid.d/mongodb status`，或者也可以使用 `sudo service mongodb status`。

##### 在本地服务器中运行 Mongo 数据库
1. 检查数据库的状态：`sudo service mongodb status` 除非已经启动数据库，否则应该会显示 [Fail] 响应。
2. 启动数据库：`sudo service mongodb start` 现在，应该会显示 [OK] 响应。
3. 通过连接到数据库服务器并运行诊断命令进行验证：`mongo --eval 'db.runCommand({ connectionStatus: 1 })'` 这将输出当前数据库版本、服务器地址和端口以及状态命令的输出。 响应中“ok”字段的值 1 表示服务器正在运行。
4. 要停止运行 MongoDB 服务，请输入：`sudo service mongodb stop`
>MongoDB 有几个默认参数，包括在 /data/db 中存储数据和在端口 27017 上运行。 此外，mongod 是守护程序（数据库的主机进程），mongo 是连接到特定实例 mongod 的命令行 shell。


#### 设置配置文件别名

键入 `sudo service mongodb start` 或 `sudo service postgres start` 和 `sudo -u postgrest psql` 可能会很繁琐。 但是，你可以考虑在 `.profile` 文件中设置别名，使这些命令更便于使用、易于记忆。

要设置自己的自定义别名或快捷方式来执行这些命令，请执行以下操作：
1. 打开终端并输入 `cd ~`以确保位于根目录中。
2. 使用终端文本编辑器 Nano 打开 `.profile` 文件，该文件可控制终端的设置：`sudo nano .profile`
3. 在文件底部（请勿更改 # set PATH 设置），添加以下内容：
```bash
# My Aliases
alias start-pg='sudo service postgresql start'
alias run-pg='sudo -u postgres psql'
```
这样你就可以输入 `start-pg` 开始运行 postgresql 服务，并输入 `run-pg` 来打开 psql shell。 `start-pg` 和 `run-pg` 可更改为所需的任何名称，但是请注意不要覆盖 postgres 已经使用的命令！
1. 添加新别名后，请使用 Ctrl + X 退出 Nano 文本编辑器 - 系统提示“保存并输入”时选择 Y（是）（将文件名保留为 .profile） 。
2. 关闭并重新打开 WSL 终端，然后尝试使用新的别名命令。


