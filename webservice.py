#!/usr/bin/python3
# encoding: utf-8

class HelloWorldService():  #this is a web service
   @soap(String,_returns=String)    #声明一个服务，标识方法的参数以及返回值
   def say_hello(self,name):
      return 'hello %s!'%name