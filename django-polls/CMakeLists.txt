cmake_minimum_required(VERSION 3.5)
project(django-polls)

set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++11")

set(SOURCE_FILES
    mysite/mysite/__init__.py
    mysite/mysite/settings.py
    mysite/mysite/urls.py
    mysite/mysite/wsgi.py
    mysite/manage.py)

#add_executable(django_1 ${SOURCE_FILES})