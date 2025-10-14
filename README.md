# 2023 Medical Project

## 项目信息

这是一个基于Django的医疗项目。

## 开发者信息

- **姓名**: 蒋松厚
- **学号**: 20231201058

## 项目结构

```
2023medical/
├── .venv/                 # Python虚拟环境
├── mysite/                # Django项目目录
│   ├── __init__.py
│   ├── settings.py        # 项目配置
│   ├── urls.py           # URL路由配置
│   └── wsgi.py           # WSGI配置
├── manage.py              # Django管理脚本
├── db.sqlite3            # SQLite数据库文件
└── LICENSE               # 许可证文件
```

## 安装和运行

1. 激活虚拟环境：
   ```powershell
   .venv\Scripts\Activate.ps1
   ```

2. 安装依赖（如果需要）：
   ```powershell
   pip install -r requirements.txt
   ```

3. 运行开发服务器：
   ```powershell
   python manage.py runserver
   ```

4. 在浏览器中访问：http://127.0.0.1:8000/

## 功能特性

- Django框架
- SQLite数据库
- 医疗相关功能（待开发）

---

*项目创建时间：2023年*