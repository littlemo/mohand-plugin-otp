# encoding=utf8
from __future__ import unicode_literals

import sys
import logging

from mohand.hands import hand

if sys.version > '3':
    PY3 = True
else:
    PY3 = False

LOG_FORMAT = "[%(asctime)s][%(name)s:%(lineno)s][%(levelname)s] %(message)s"
logging.basicConfig(
    level=logging.WARN,
    format=LOG_FORMAT,
    stream=sys.stdout,
)
log = logging.getLogger(__name__)


def otp(*dargs, **dkwargs):
    """
    将被装饰函数封装为一个 :class:`click.core.Command` 类，成为 ``mohand`` 的子命令

    该装饰器被作为一个包含定制其行为的含参数装饰器使用（如： ``@hand.otp(secret='xxoo')`` ）

    .. note::

        该装饰器最终会通过插件系统被注册到 :data:`.hands.hand` 中。

        此处的 ``otp`` 装饰器本身是应该不支持无参数装饰的，但考虑到其作为样例实现，
        故将其实现为兼容两种传参的装饰器

    :param int log_level: 当前子命令的日志输出等级，默认为： ``logging.INFO``
    :param str secret: 用于构造基于时间的 OTP 的秘钥字串
    :return: 被封装后的函数
    :rtype: function
    """
    invoked = bool(len(dargs) == 1 and not dkwargs and callable(dargs[0]))
    if invoked:
        func = dargs[0]

    def wrapper(func):
        @hand._click.command(
            name=func.__name__.lower(),
            help=func.__doc__)
        def _wrapper(*args, **kwargs):
            log_level = dkwargs.pop('log_level', logging.INFO)
            log.setLevel(log_level)

            log.debug("decrator param: {} {}".format(dargs, dkwargs))
            log.debug("function param: {} {}".format(args, kwargs))

            with OTP(*dargs, **dkwargs) as o:
                func(o, *args, **kwargs)
        return _wrapper
    return wrapper if not invoked else wrapper(func)

