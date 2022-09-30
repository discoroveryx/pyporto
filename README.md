# PyPorto is a design for building scalable and testable applications with Django.

## Welcome to PyPorto


- [Introduction](#Introduction)
- [Getting Started](#Getting-Started)
    - [Basic Project Structure](#Project-Structure)
    - [Basic Containers Structure](#Containers-Structure)
        - [Components](#Components)
            - [Main Components](#Main-Components)
            - [Framework components](#Framework-Components)
        - [Components Details](#Components-Details)
- [Project scheme](#Project-scheme)
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

It is usefull for Minimum Viable Product (MVP) projects, but if you are going to split your project into a microservice architecture (in the future), you will have to deal with wild connection in your business logic, also you can't extract the business logic layer from the framework layer.

Сomes to the help **Porto** and **PyPorto**

</br>

<a id="Getting-Started"></a>
# Getting Started


<a id="Project-Structure"></a>
## Basic Project Structure

`dj/` - holds all configurations for your Django project.\
`core/` - holds the infrastructure code (your shared code between all Containers).\
`containers/` - holds all your application and business logic code.\
`manage.py` - command-line utility for administrative tasks.

These layers `core` and `containers` can be created anywhere inside Django framework.

</br>


<a id="Containers-Structure"></a>
## Basic Containers Structure

</br>


<a id="Components"></a>
## Components


Every Container consists of a number of Components, in **Porto** one Component can be built from these types of components:
`Main Components` and `Framework Components`.

</br>

<a id="Main-Components"></a>
## Main Components

`actions/` - holds all actions.\
`subactions/` - holds all subactions.\
`tasks/` - holds all tasks.\
`repositories/` - holds all repositories.\
`dto/` - holds all Data Transfer Objects (it does not include in Porto, it is new for PyPorto).\
`types/` - holds all types.\
`values/` - holds all values.\
`entities/` - holds all entities.\
`constants/` - holds all constants.

</br>

<a id="Framework-Components"></a>
## Framework Components

`api (urls, views)/` - holds all urls and views.\
`migrations/` - holds all migrations.\
`models/` - holds all models.\
`paginations/` - holds all paginations.\
`serializers/` - holds all serializers.\
`tests/` - holds all tests.



*You can make new components, if you need it.*

</br>

<a id="Components-Details"></a>
### Main Components Definitions & Principles

> Click on the arrows below to read about each component.


<a id="DTO"></a>
<Details>
<Summary>Data Transfer Object (DTO)</Summary>
<br>

Data Transfer Object (DTO)

DTO is used for data transport between layers.
DTO is an immutable object, it does not have ID's, it does not have any logic.

Controller/View -> DTO -> Action

#### Example:
Usually we have something that in DRF view:
```python
from mainapp.services.my_serivice import get_all_products

def get(self, request, *args, **kwargs):
    product_list = get_all_products(
        user_id=request.user.id,
        filter_by={'price__gte': 20},
        sort_by='id',
        ...  # More other args.
    )

    serializer = ProductListSerializer(product_list, many=True)

    return Response(serializer.data)
```

You need to collect all arguments with `DTO` and send them as one argument to the business logic:
```python
from dataclasses import dataclass
from core.parents.dto.dto import DTO

@dataclass(init=True, eq=True, frozen=True)
class GetProductListDTO(DTO):
    user_id: int
    filter_by: dict
    sort_by: str
    ...  # More other fields.

params = GetProductListDTO(
    user_id=request.user.id,
    filter_by={'price__gte': 20},
    sort_by='id',
    ...
)

product_list = get_all_products(params)

serializer = ProductListSerializer(product_list, many=True)

return Response(serializer.data)
```

Bad idea to pass all `request` to `DTO` instead of to pass `request.user.id` or `request.user.is_authenticated` , why? because if you want to debug that part of business logic in console (for example: django shell), you have to buld all request:

Bad idea:
```python
def get(self, request, *args, **kwargs):
    # WRONG! You pass all HttpRequest objects, lika that [method, content_type, GET, POST, ...].
    # and you will have to build it during debugging or testing it.
    params = GetProductListDTO(
        request=request,  
    )

    ...
```

Good idea:
```python
def get(self, request, *args, **kwargs):
    # It's even easy to test and debug outside of the framework environment, because you have only int and bool types.
    params = GetProductListDTO(
        user_id=request.user.id,  # You pass only int.
        user_is_authenticated=request.user.is_authenticated  # You pass only bool.
        ...
    )

    ...
```

***

</Details>


<a id="Project-scheme"></a>
# Project-scheme


```bash
app
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

<a id="Components-Detail"></a>
# Main Components

<a id="Feedback"></a>
# Get in Touch

> Your feedback is important.

For feedbacks, questions, or suggestions? We are on [**telegram**](https://t.me/discoroveryx).


<a name="License"></a>
# License

[MIT](https://opensource.org/licenses/MIT)
