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
