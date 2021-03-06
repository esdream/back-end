# -*- coding: utf-8 -*-
from datetime import datetime
MONGO_HOST = 'localhost'
MONGO_PORT = 27017
MONGO_DBNAME = 'apitest'

SOFT_DELETE = True
HATEOAS = False

RESOURCE_METHODS = ['GET', 'POST']
ITEM_METHODS = ['GET', 'PATCH', 'DELETE']
PAGINATION_DEFAULT = 30
X_DOMAINS = '*'
X_HEADERS = ['If-Match', 'Content-Type']

# 订单：
#    - phone_number:
#       手机号码
#    - name:
#       姓名
#    - lilybbs_id:
#       小百合 ID
#    - campus:
#       校区
#    - machine_model:
#       机器型号
#    - description:
#       问题描述
#    - status:
#       订单状态: 等待处理，正在处理，处理完成。
#    - comments:
#       订单回复
#    - handled_by:
#       处理该订单的 IT 侠用户名
order_schema = {
    'phone_number': {
        'type': 'string',
        'regex': '^(13|14|15|17|18)[0-9]{9}$',
        'required': True,
    },
    'name': {
        'type': 'string',
        'minlength': 1,
        'maxlength': 15,
        'required': True,
    },
    'lilybbs_id': {
        'type': 'string',
    },
    'campus': {
        'type': 'string',
        'required': True,
        'allowed': ['gulou', 'xianlin'],
    },
    'machine_model': {
        'type': 'string',
        'required': True,
    },
    'OS': {
        'type': 'string',
        'required': True,
    },
    'description': {
        'type': 'string',
        'required': True,
    },
    'status': {
        'type': 'string',
        'allowed': ['waiting', 'working', 'done'],
        'default': 'waiting',
    },
    'comments': {
        'type': 'list',
        'required': False,
        'schema': {
            'type': 'dict',
            'schema': {
                'username': {'type': 'string'},
                'created_at': {'type': 'datetime', 'default': datetime.utcnow()},
                'content': {'type': 'string', 'empty': False},
            },
        },
    },
    'handled_by': {
        'type': 'string',
    },
}


# IT 侠：
#    - name:
#       姓名
#    - username:
#       帐号名
#    - password:
#       密码
#    - email:
#       电子邮箱
#    - campus:
#       所在校区
#    - role:
#       IT 侠，网站管理员
itxia_schema = {
    'name': {
        'type': 'string',
        'required': True,
    },
    'username': {
        'type': 'string',
        'required': True,
    },
    'password': {
        'type': 'string',
        'required': True,
    },
    'email': {
        'type': 'string',
        'required': True,
    },
    'compus': {
        'type': 'string',
        'required': True,
        'allowed': ['gulou', 'xianlin'],
    },
    'role': {
        'type': 'string',
        'required': True,
        'allowed': ['itxia', 'admin'],
    },
}

orders = {
    'schema': order_schema,
    'datasource': {
        'default_sort': [('_created', -1)]
    }
}

itxia = {
    'schema': itxia_schema,
    'datasource': {
        'projection': {'password': 0}
    }
}

DOMAIN = {
    'orders': orders,
    'itxia': itxia,
}
