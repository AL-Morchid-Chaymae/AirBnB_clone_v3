## Table of Contents

* [Description](#description)
* [Purpose](#purpose)
* [Requirements](#requirements)
* [File Descriptions](#file-descriptions)
* [Environmental Variables](#environmental-variables)
* [Usage](#usage)
* [Bugs](#bugs)
* [Authors](#authors)
* [License](#license)

## Description

**hbnb** is a full-stack clone of the web application [AirBnB](https://www.airbnb.com/). This clone was built in four iterative phases. This version includes completion of Phase 1 from [AirBnB_clone_v1: Console and web static](https://github.com/AL-Morchid-Chaymae/AirBnB_clone_v2),  which involves exposing stored objects via a JSON web interface and manipulating objects via a custom RESTful API.

### Create a custom RESTful API, expose stored objects via JSON web interface, manipulate objects via custom RESTful API
![restful_api](https://s3.amazonaws.com/intranet-projects-files/concepts/74/hbnb_step4.png)

**Links to other versions:**
* [AirBnB_clone_v1: Console and web static](https://github.com/AL-Morchid-Chaymae/AirBnB_clone)
* [AirBnB_clone_v2: MySQL, deploy web static, web framework](https://github.com/AL-Morchid-Chaymae/AirBnB_clone_v2)
* [AirBnB_clone_v4: Web dynamic](https://github.com/bchen528/) (Final version!)

## Purpose
The purpose of Phase 3 is to learn how to:
* create a RESTful API
* use CORS
* request RESTful API
* retrieve, create, update, delete a resource with HTTP methods

## Requirements
* All files compiled with Ubuntu 14.04 LTS
* Documentation
* Organized files in proper folders
* Python unit tests for all files
* All files must be pep8 compliant

## File Descriptions
        * `all` - returns the dictionary `__objects`
        * `new` - sets in `__objects` the obj with key `<obj class name>.id`
        * `save` - serializes `__objects` to the JSON file (path: `__file_path`)
        * `reload` - deserializes the JSON file to `__objects`
        * `delete` - delete object from `__objects` if exists
        * `close` - call reload
      * [db_storage.py](/models/engine/db_storage.py) - class DBStorage; 
        * `__init__` - initalize instances
        * `all` - return dictionary of instance attributes
        * `new` - add new object to current database session
        * `save` - commit all changes of the current database session
        * `delete` - delete from the current database session obj if not None
        * `reload` - create all tables in database and current database session
        * `close` - close session
        * `get` - retrieves an object
        * `count` - counts number of objects of a class (if given)
  * [api](api) - contains v1 and v1/views folders
    * [`__init__.py`](api/__init__.py) - empty `__init__.py` file
    * [v1](api/v1) - contains app file and views folder
      * [`__init__.py`](api/v1/__init__.py) - empty `__init__.py` file
      * [app.py](api/v1/app.py) - app file
        * `tear` - closes storage engine
        * `not_found` - handles 404 error and gives json formatted response
      * [views](api/v1/views) - contains views for AirBnB objects
        * [`__init__.py`](api/v1/views/__init__.py) - create blueprint
        * [amenities.py](api/v1/views/amenities.py) - view for Amenity objects that handles all default RestFul API actions
          * `list_amenities` - retrieves a list of all Amenity objects
          * `get_amenity` - retrieves an Amenity object
          * `delete_amenity` - deletes an Amenity object
          * `create_amenity` - creates an Amenity object
          * `updates_amenity` - updates an Amenity object
        * [cities.py](api/v1/views/cities.py) - view for City objects that handles all default RestFul API actions
          * `list_cities_of_state` - retrieves list of of City objects
          * `create_city` - creates a City
          * `get_city` - retrieves a City object
          * `delete_city` - deletes a City object
          * `updates_city` - updates a City object
        * [index.py](api/v1/views/index.py) - index file
          * `status` - routes to status page
          * `count` - retrieves number of each objects by type
        * [places.py](api/v1/views/places.py) - view for Place objects that handles all default RestFul API actions
          * `list_places_of_city` - retrieves list of of Place objects in city
          * `create_place` - creates a Place
          * `get_place` - retrieves a Place object
          * `delete_place` - deletes a Place object
          * `updates_place` - updates a Place object
        * [places_amenities.py](api/v1/views/places_amenities.py) - place-amenity view
          * `list_amenities_of_place` - retrieves a list of all Amenity objects of a Place
          * `create_place_amenity` - creates an Amenity
          * `delete_place_amenity` - deletes an Amenity object
          * `get_place_amenity` - retrieves an Amenity object
        * [places_reviews.py](api/v1/views/places_reviews.py) - place-review view
          * `list_reviews_of_place` - retrieves a list of all Review objects of a Place
          * `create_review` - creates a review
          * `get_review` - retrieves a Review object
          * `delete_review` - deletes a Review object
          * `updates_review` - updates a Review object
        * [states.py](api/v1/views/states.py) - view for State objects that handles all default RestFul API actions
          * `list_states` - retrieves a list of all State objects
          * `get_state` - retrieves a State object
          * `delete_state` - deletes a State object
          * `create_state` - creates a State
          * `updates_state` - updates a State object
        * [users.py](api/v1/views/users.py) - 
          * `list_users` - retrieves list of of User objects
          * `create_user` - creates a User
          * `get_user` - retrieves a User object
          * `delete_user` - deletes a User object
          * `updates_user` - updates a User object


