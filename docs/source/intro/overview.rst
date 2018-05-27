.. _intro-overview:

====
概览
====

`MoHand`_ 插件，用以提供根据传入的 ``secret`` 返回实时 **OTP** 密码的功能，
并可以根据用户实际需求进行最终输出密码的再拼接。

基于 `pyotp`_ 包做的封装实现，并提供了两个接口，分别为 :meth:`.now` 和 :meth:`.format` 。
后者支持以传入的指定模板&字串返回最终动态密码作为输出。

安装方法
========

您可以通过 ``pip`` 进行安装，本包仅在 ``Python 3.X`` 下测试通过::

    pip3 install mohand-plugin-otp

.. hint::

    从 ``v1.0.0`` 版本开始，增加了对 ``Python 2.X`` 的支持，但由于我主要在 **Py3**
    环境下使用，所以强烈建议您在 **Py3** 下使用。如果您在 **Py2** 环境下遇到任何异常，
    可以及时提 `Issues`_ 给我，我会努力在搬砖的间隙进行修复。。。

.. note::

    建议使用 `virtualenv`_ 来安装，避免与其他包产生依赖冲突。

    如果您感兴趣的话，可以了解下 `virtualenvwrapper`_ ，用其来管理虚拟环境可谓丝般顺滑！

使用说明
========

此插件的使用十分简单，首先您需要拿到您 **OTP** 的秘钥，一般网站都是通过一个二维码提供的，如下：

.. image:: images/chart.png
   :align: center

您可以先使用 ``Google Authenticator`` 等工具扫描上述秘钥，将其添加。
然后您可以通过通用的二维码扫描工具获取该二维码的内容为
``otpauth://totp/alice@google.com?secret=JBSWY3DPEHPK3PXP``
然后我们就可以从中找到 ``secret`` 为 ``JBSWY3DPEHPK3PXP`` 。

在您的 ``handfile.py`` 文件中添加内容如下::

    # encoding=utf8
    from mohand.hands import hand

    @hand.otp(secret='JBSWY3DPEHPK3PXP')
    def otp(o):
        """获取动态密码"""
        hand._click.echo(o.now())

然后我们就可以通过 ``mohand`` 命令来在终端执行该子命令::

    $ mohand
    Usage: mohand [OPTIONS] COMMAND [ARGS]...

      通用自动化处理工具

      详情参考 `GitHub <https://github.com/littlemo/mohand>`_

    Options:
      --author   作者信息
      --version  版本信息
      --help     Show this message and exit.

    Commands:
      otp       获取动态密码

    $ mohand otp
    218548

此时可以将返回的动态密码与您手机中添加相同秘钥的工具中的密码进行对比，不出意外应该是相同的，
以上即为最基本的使用，如果您对 ``handfile.py`` 的使用不是很清楚，可以参见 `MoHand`_
的文档说明。

然而在实际使用时还会有一种需求，即将动态的 **OTP** 密码与一个指定的 **PIN**
码进行指定样式的拼接，此时我们就可以使用 :meth:`.format` 接口来方便的实现该需求::

    # encoding=utf8
    from mohand.hands import hand

    @hand.otp(secret='JBSWY3DPEHPK3PXP')
    def otp(o):
        """获取动态密码"""
        hand._click.echo(o.format('{pin}{otp}', pin='xxooxx'))

将上述的修改后 **otp** 方法更新到 ``handfile.py`` 文件中，然后我们就可以执行下看看效果::

    $ mohand otp
    xxooxx513255

这样我们就获取到了一个在 **otp** 前拼接了一个 **pin** 的动态密码了。

当然还有更高阶的使用方式，比如大部分的动态密码都是用于网站登录，如果您有频繁的认证需求，
不妨将其 *HTTP* 请求抓下来，并以模拟请求的方式实现于 ``handfile.py`` 中，
如此便可以很便捷的实现动态密码站点的自动登录了，省去了复制粘贴密码的工作。


.. _MoHand: http://mohand.rtfd.io/
.. _pyotp: http://pyotp.readthedocs.io/
.. _virtualenv: http://virtualenv.pypa.io/
.. _virtualenvwrapper: https://virtualenvwrapper.readthedocs.io/
.. _Issues: https://github.com/littlemo/mohand-plugin-otp/issues
