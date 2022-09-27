# PyPorto (Software Architectural Pattern)

## Welcome to PyPorto


- [Introduction](#Introduction)
- [Getting Started](#Getting-Started)
	- [Basic Project Structure](#Project-Structure)
	- [Basic Containers Structure](#Containers-Structure)
- [Components](#Components)
	- [Main Components](#Main-Components)
	- [Framework components](#Framework-Components)
- [Feedback & Questions](#Feedback)


</br>

<a id="Introduction"></a>
# Introduction

**Porto** is a modern software architectural pattern, consisting of guidelines, principles and patterns to help developers organize their code in a highly maintainable and reusable way.

See more about [Porto](https://github.com/Mahmoudz/Porto)

**PyPorto** is an implementing Porto architectural pattern for [DRF](https://www.django-rest-framework.org)

Why do we need to use **PyPorto**?

Usually in Django or DRF we have business logic in next files

`views/my_view.py`\
`serializers/some_serializer.py`\
`models/my_model.py`\
`services/my_business_logic_n1.py`

it is usefull for Minimum Viable Product (MVP) projects, but if you are going to split your project into a microservice architecture (in the future), you will have to deal with wild connection in your business logic, also you can't extract the business logic layer from the framework layer.

Сomes to the help **Porto** and **PyPorto**

</br>

<a id="Getting-Started"></a>
# Getting Started


<a id="Project-Structure"></a>
## Basic Project Structure

`dj/` - holds all configurations for your Django project.\
`core/` - holds the infrastructure code (your shared code between all Containers).\
`containers/` - holds all your application and business logic code.\
`manage.py`

These layers `core` and `containers` can be created anywhere inside Django framework.

</br>


<a id="Containers-Structure"></a>
## Basic Containers Structure


```bash
containers
├── dj
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
├── core
│   ├── __init__.py
│   ├── configs
│   │   ├── __init__.py
│   │   └── ...
│   ├── helpers
│   │   ├── __init__.py
│   │   └── ...
│   └── parents
│   │   ├── __init__.py
│   │   ├── actions
│   │   │   ├── __init__.py
│   │   │   ├── subaction.py
│   │   │   └── action.py
│   │   ├── entities
│   │   │   ├── __init__.py
│   │   │   └── entity.py
│   │   ├── dto
│   │   │   ├── __init__.py
│   │   │   └── dto.py
│   │   ├── repositories
│   │   │   ├── __init__.py
│   │   │   └── repository.py
│   │   ├── tasks
│   │   │   ├── __init__.py
│   │   │   └── task.py
│   │   ├── values
│   │   │   ├── __init__.py
│   │   │   └── value.py
├── containers
│   ├── __init__.py
│   ├── container_1
│   │   ├── actions
│   │   │   ├── __init__.py
│   │   │   ├── get_product_list_action.py
│   │   │   └── retrieve_product_action.py
│   │   ├── api
│   │   │   ├── __init__.py
│   │   │   ├── urls
│   │   │   │   ├── __init__.py
│   │   │   │   ├── product_list_v1.py
│   │   │   │   └── product_retrieve_v1.py
│   │   │   ├── views
│   │   │   │   ├── __init__.py
│   │   │   │   ├── product_list_view.py
│   │   │   │   └── product_retrieve_view.py
│   │   ├── dto
│   │   │   ├── __init__.py
│   │   │   ├── product_list_dto.py
│   │   │   └── product_retrieve_dto.py
│   │   ├── entities
│   │   │   ├── __init__.py
│   │   │   └── product_entity.py
│   │   ├── migrations
│   │   │   ├── __init__.py
│   │   │   └── ...
│   │   ├── models
│   │   │   ├── __init__.py
│   │   │   └── product.py
│   │   ├── paginations
│   │   │   ├── __init__.py
│   │   │   └── product_list_pagination.py
│   │   ├── repositories
│   │   │   ├── __init__.py
│   │   │   └── product_repository.py
│   │   ├── serializers
│   │   │   ├── __init__.py
│   │   │   └── product_list_serializer.py
│   │   ├── tasks
│   │   │   ├── __init__.py
│   │   │   ├── get_product_list_task.py
│   │   │   └── retrieve_product_task.py
│   │   ├── tests
│   │   │   ├── __init__.py
│   │   │   └── test_get_product_list.py
│   │   ├── types
│   │   │   ├── __init__.py
│   │   │   └── product_id_type.py
│   │   ├── values
│   │   │   ├── __init__.py
│   │   │   └── product_list_row.py
│   │   ├── constants
│   │   │   ├── __init__.py
│   │   │   │   const_x.py
│   │   │   └── const_y.py
│   │   ├── __init__.py
│   │   └── apps.py
│   ├── container_2
│   │   ├── actions
│   │   │   ├── __init__.py
│   │   │   └── ...
│   │   ├── api
│   │   │   ├── __init__.py
│   │   │   ├── urls
│   │   │   │   ├── __init__.py
│   │   │   │   └── ...
│   │   │   ├── views
│   │   │   │   ├── __init__.py
│   │   │   │   └── ...
│   │   ├── dto
│   │   │   ├── __init__.py
│   │   │   └── ...
│   │   ├── entities
│   │   │   └── ...
│   │   ├── tasks
│   │   │   ├── __init__.py
│   │   │   └── ...
│   │   ├── tests
│   │   │   ├── __init__.py
│   │   │   └── ...
│   │   └── __init__.py
│   ├── foo_section
│   │   ├── foo
│   │   │   ├── api
│   │   │   │   ├── __init__.py
│   │   │   │   ├── urls
│   │   │   │   │   ├── __init__.py
│   │   │   │   │   └── ...
│   │   │   │   ├── views
│   │   │   │   │   ├── __init__.py
│   │   │   │   │   └── ...
│   │   │   ├── actions
│   │   │   │   ├── __init__.py
│   │   │   │   └── ...
│   │   │   ├── tasks
│   │   │   │   ├── __init__.py
│   │   │   │   └── ...
│   │   │   ├── tests
│   │   │   │   ├── __init__.py
│   │   │   │   └── ...
│   │   │   └── __init__.py
│   │   ├── bar
│   │   │   ├── api
│   │   │   │   ├── __init__.py
│   │   │   │   ├── urls
│   │   │   │   │   ├── __init__.py
│   │   │   │   │   └── ...
│   │   │   │   ├── views
│   │   │   │   │   ├── __init__.py
│   │   │   │   │   └── ...
│   │   │   ├── actions
│   │   │   │   ├── __init__.py
│   │   │   │   └── ...
│   │   │   ├── tasks
│   │   │   │   ├── __init__.py
│   │   │   │   └── ...
│   │   │   ├── tests
│   │   │   │   ├── __init__.py
│   │   │   │   └── ...
│   │   │   └── __init__.py
│   │   └── apps.py
├── static
│   └── ...
├── media
│   └── ...
└──manage.py
```


</br>


<a id="Components"></a>
# Components


Every Container consists of a number of Components, in **Porto** one Component can be buit from these types of conmponents:
`Main Components` and `Framework Components`.

</br>

<a id="Main-Components"></a>
## Main-components


#### Common entities
`constants/` - holds all constants.\
`dto/` - holds all Data Transfer Objects (it does not include in Porto, it is new for PyPorto).\
`types/` - holds all types.\
`tasks/` - holds all tasks.\
`values/` - holds all values.\
`actions/` - holds all actions.\
`subactions/` - holds all subactions.\
`entities/` - holds all entities.\
`repositories/` - holds all repositories.\

</br>

<a id="Framework-Components"></a>
## Framework-components

#### Django Rest Framework entities
`api (urls, views)/` - holds all constants.\
`migrations/` - holds all migrations.\
`models/` - holds all models.\
`paginations/` - holds all paginations.\
`serializers/` - holds all serializers.\
`tests/` - holds all tests.\



*You can make new components, if you need it.*

</br>

<a id="Feedback"></a>
# Get in Touch

> Your feedback is important.

For feedbacks, questions, or suggestions? We are on [**telegram**](t.me/discoroveryx).


<a name="License"></a>
# License

[MIT](https://opensource.org/licenses/MIT)
