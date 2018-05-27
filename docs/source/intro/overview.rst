.. _intro-overview:

====
概览
====

`MoHand`_ 插件，用以提供根据传入的 ``secret`` 返回实时 **OTP** 密码的功能，
并可以根据用户实际需求进行最终输出密码的再拼接。

基于 `pyotp`_ 包做的封装实现，并提供了两个接口，分别为 :meth:`.now` 和 :meth:`.format` 。
后者支持以传入的指定模板&字串返回最终动态密码作为输出。