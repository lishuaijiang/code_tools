规划：
1. 蓝图嵌套控制版本(v1、v2、v3)
2. 自定义异常
3. marshmallow 序列化
4. jwt 双 token(access_token、refresh_token)
5. 权限控制 (Redis 缓存权限，MySQL 持久化权限)，建立权限模块 yaml 文件(permission_xxx_module.yaml)，自动加载`permissions`目录下各权限文件夹，
并提供 python/command 命令支持命令行初始化权限表
6. 基本业务模块 user (忘记密码、修改密码)、操作日志 logs、配置中心 (用于设置角色和权限、邮件通知、短信通知、钉钉通知等，默认 websocket通知)
7. 插件式通知模块
8. flask_sqlalchemy + flask_migrate 支持数据迁移，生成默认数据，如超级管理员数据
9. 配置管理，多环境配置
10. 容器化部署，Dockerfile + docker-compose.yml
11. 后台任务 celery
12. 请求生命周期管理 (hooks.py)
13. extensions.py 扩展


推荐项目结构
```
project/
├── app/
│   ├── __init__.py          # 应用工厂
│   ├── config.py            # 配置管理
│   ├── extensions.py        # 扩展初始化（DB, JWT等）
│   ├── commands/            # 自定义命令
│   │   └── init_data.py     # 初始化数据命令
│   ├── api/
│   │   ├── v1/              # API 版本目录
│   │   │   ├── __init__.py 
│   │   │   ├── user.py      # 用户模块
│   │   │   └── auth.py      # 认证模块
│   │   └── v2/              # 新版本示例
│   ├── models/              # 数据模型
│   │   └── user.py
│   ├── schemas/             # Marshmallow 模式
│   │   └── user_schema.py
│   ├── services/            # 业务逻辑层
│   │   └── user_service.py
│   ├── utils/               # 工具类
│   │   ├── jwt_utils.py
│   │   └── redis_utils.py
│   └── tasks/               # 异步任务
│       └── email_tasks.py
├── migrations/              # 数据库迁移脚本
├── tests/                   # 测试用例
├── .env                     # 环境变量
├── docker-compose.yml       # 容器编排
├── Dockerfile               # Docker 构建
├── requirements.txt         # 依赖清单
└── run.py                   # 启动脚本
```

## 实际结构
```
flask_restful_api
├── __init__.py
├── app
│   ├── __init__.py
│   ├── api
│   │   ├── __init__.py
│   │   ├── v1
│   │   │   ├── __init__.py
│   │   │   └── user.py
│   │   └── v2
│   │       └── __init__.py
│   ├── commands
│   │   ├── __init__.py
│   │   ├── init_db.py
│   │   └── init_permissions.py
│   ├── extensions.py
│   ├── hooks.py
│   ├── models
│   │   ├── __init__.py
│   │   └── user.py
│   ├── permissions
│   │   └── __init__.py
│   ├── schemas
│   │   ├── __init__.py
│   │   └── user.py
│   ├── services
│   │   └── __init__.py
│   ├── tasks.py
│   └── utils.py
├── config.py
├── docker-compose.yml
├── Dockerfile
├── README.md
├── requirements.txt
└── run.py
```

### 权限控制设计

- 后端代码中定义 permissions.yml 文件(可以是多个 yml 文件，看系统架构，是否分为多个模块，如管理后台，业务管理，资源控制台，用户中心等)
- 支持用户在启动 Flask 程序之前，可以通过命令行 flask shell init_permissions 去将 permissions.yml 读取并存储到 MySQL 的 functions 表中
- 角色默认只有超级管理员，超级管理员拥有所有权限
- 当程序启动时，第一时间去 functions 表中将超级管理员的权限树生成（也就是将数据库中的 扁平化权限转为树形权限并缓存到 Redis 中）
- 超级管理员登录系统后，从 Redis 中读取超级管理员的权限树
- 在管理页面为指定管理员或普通用户创建角色，并为该角色勾选权限树设置权限，点击确定后，后端将树形权限转为扁平化权限后，
  数据在保存到数据库的同时（保存至角色和 functions 的第三张表中，角色和 functions 表两者是多对多关系），
  将该角色的权限树重新生成（扁平化权限转为树形权限）并缓存到 Redis 中
- 当管理员登录之后，从 Redis 中读取管理员的权限树，注意管理员的权限树是超级管理员给勾选的，很可能不是完全的权限树
- 管理员可以为普通用户创建角色，并对该角色勾选设置管理员拥有的权限树，点击确定后，后端将树形权限转为扁平化权限后，
  数据在保存到数据库的同时（保存至角色和 functions 的第三张表中，角色和 functions 表两者是多对多关系），
  将该角色的权限树重新生成（扁平化权限转为树形权限）并缓存到 Redis 中
- 注意，树形权限是为了方便展示在页面，方便超级管理员或普通管理员勾选才设计的，在数据库中 functions 表是扁平化权限

- 在修改权限（如角色更新）后，主动更新对应 Redis 缓存
- 后端校验创建角色时分配的权限必须属于当前用户自身权限子集

- 由超级管理员在管理页面去创建管理员、普通用户，创建角色，分配权限。管理员也可以登录之后去创建普通用户（只能创建普通用户），创建角色，分配权限
- 用户进入用户中心自行修改邮箱、密码等

## 运行/调试说明
**1. 创建独立虚拟环境并安装依赖库**
```bash
cd flask_restful_api/
python3 -m venv venv
source venv/bin/activate
python3 -m pip install -r requirements.txt
```

**2. 运行**
```bash
# 确保在`flask_restful_api`目录下，且进入虚拟环境内
flask run
```
