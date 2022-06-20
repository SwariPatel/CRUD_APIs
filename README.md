# CRUD_APIs
A simple project to create, read, update and delete data in database through API using Django REST framework of Python. 
-----
### Technology/Framework used  
* Python - 3.10.1
    - [Pycharm Community Edition](https://www.jetbrains.com/pycharm/download/#section=windows)
* Django - 4.0.1
* Django REST framework - 3.13.1
* SQLite3
* requests - 2.27.0
* [Postman Tool](https://www.postman.com/downloads/) to check APIs

### Features  
This project includes basic **CRUD**(Create, Read, Update, Delete) operations done on database through API.  
**1. Read**  
Read operation is done when we get **GET** http request and the request is handled to respond back.  
Code of Read operation (views.py):
```
    if request.method == 'GET':
        records = studentRecord.objects.all()
        records_serializer = studentRecordSerializer(records,many=True)
        return JsonResponse(records_serializer.data,safe=False)
```  
This code simply fetch the data from database and shows it to user.    
**2. Create**  
Create operation is executed when we get **POST** http request and a new data row is added in the database.  
Code of Create operation (views.py):
```
    elif request.method == 'POST':
        insert_data = JSONParser().parse(request)
        records_serializer = studentRecordSerializer(data=insert_data)
        if records_serializer.is_valid():
            records_serializer.save()
            return JsonResponse("Data added successfully",safe=False)
        return JsonResponse("Failed to add data",safe=False)
```
**3. Update**  
Update operation is handled under **PUT** http request. The data is updated/changed under this opeartion.  
Code of Update operation (views.py):
```
    elif request.method == 'PUT':
        update_data = JSONParser().parse(request)
        record = studentRecord.objects.get(rollnumber=update_data['rollnumber'])
        records_serializer = studentRecordSerializer(record,data=update_data)
        if records_serializer.is_valid():
            records_serializer.save()
            return JsonResponse("Updated successfully",safe=False)
        return JsonResponse("Failed to update data",safe=False)
```  
**4. Delete**  
Delete operation is operated under **DELETE** http request. It is done by sending ___UniqueID___ to find the data row and delete from the database.  
Code of Delete operation (views.py):
```
    elif request.method == 'DELETE':
        record = studentRecord.objects.get(rollnumber = id)
        record.delete()
        return JsonResponse("Deleted successfully",safe=False)
    return JsonResponse("Failed to delete data",safe=False)
```
-----
### Screenshots  
1. GET request (Read data)  
![image](https://user-images.githubusercontent.com/87166314/174583506-dee42b8f-ee2e-41d1-bd99-20bc6b8c49a8.png)  
2. POST request (Create data)  
![image](https://user-images.githubusercontent.com/87166314/174584543-1d232755-f710-4784-a460-cfca6d7d471b.png)  
3. PUT request (Update data)  
![image](https://user-images.githubusercontent.com/87166314/174584958-a4f3474e-61d3-40c9-b6e0-e3f2c1a501be.png)  
4. DELETE request (Delete data)  
![image](https://user-images.githubusercontent.com/87166314/174590810-c024b342-3176-400f-99ad-167fedd2011a.png)  
5. After applying CRUD operations  
![image](https://user-images.githubusercontent.com/87166314/174590983-82504ade-fdbc-481b-a514-1ae9eafd639a.png)  

### Task list  
- [x] Create API
- [x] Read API
- [x] Update API
- [x] Delete API
- [x] End-point of Create API
- [x] End-point of Read API
- [ ] End-point of Update API
- [x] End-point of Delete API
- [ ] Front-end
