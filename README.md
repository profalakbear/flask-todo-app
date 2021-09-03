# **in local**

> mkdir flaskapp && cd flaskapp

> python -m venv venv

> git clone https://github.com/rasimogluali/flask-todo-app.git

To activate virtual environment 
> **in linux:** source venv/bin/activate
> **in windows:** venv\Scripts\activate

> pip install -r requirements.txt 

> python main.py 

> to see swagger api documentation send request to **/swagger/**
> to run unit tests locate to the project root directory and just type **pytest**

# **with docker**

after doing steps above 
> docker-compose build && docker-compose up


# YOU CAN SEE DEMO EXAMPLE PHOTOS BELOW


## SWAGGER API DOCUMENTATION

![swagger_ui](https://user-images.githubusercontent.com/78125347/131435113-a672dc9a-471a-4942-b96f-35c9f29f9b84.png)
![get](https://user-images.githubusercontent.com/78125347/131435108-0f5909a7-710e-4e30-9eed-3425ef7938ba.png)
![get by id](https://user-images.githubusercontent.com/78125347/131435106-4f8f8825-cf40-4ef6-b72b-c010f0955058.png)
![create](https://user-images.githubusercontent.com/78125347/131435101-b9dd10b6-3bf8-4ec8-85d1-ca0c1add0f0d.png)
![update](https://user-images.githubusercontent.com/78125347/131435116-a5509238-8dc8-4d9b-80f4-0d8f29fe692b.png)
![delete](https://user-images.githubusercontent.com/78125347/131435103-ff1e56a8-cdf2-4082-8900-54a0c41f5959.png)
![schemas](https://user-images.githubusercontent.com/78125347/131435112-d67df133-630b-4913-a098-18fcc951456b.png)


## UNIT TESTS RESULT

![unit_test_results](https://user-images.githubusercontent.com/78125347/131435115-66377d73-c861-4571-b688-fdd989a39555.png)


## ENDPOINT TESTS

![get_all_endpoint](https://user-images.githubusercontent.com/78125347/131435109-90aca276-c93a-4246-acc7-9176688fbec3.png)
![get_by_id_endpoint](https://user-images.githubusercontent.com/78125347/131435111-56a351b8-f3c5-42d0-a157-639301d8e335.png)
![create_endpoint](https://user-images.githubusercontent.com/78125347/131435102-82fb42ec-ef0f-4a6e-83f9-510761e033ba.png)
![delete_endpoint](https://user-images.githubusercontent.com/78125347/131435104-86f13212-3cee-48c9-b7ca-ef08bc49213e.png)
![update_endpoint](https://user-images.githubusercontent.com/78125347/131435117-28f8e0f3-2654-4370-8317-f32deb1d1c8a.png)
