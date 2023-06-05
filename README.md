# DjangoUserDetailsApis

This project consists of follwing APIs:

1)**Signup API**: : is used to add a user <br/>
  Endpoint: /signup <br/>
  Mandatory Fields: email, first_name, last_name, phone_number, password <br/>
  Sample Request:  <br/>
  { <br/>
    "email":"your_email@example.com",  <br/>
    "first_name":"Your_First_Name", <br/>
    "last_name":"Your_Last_Name", <br/>
    "phone_number":"2123456789", <br/>
    "password":"****" <br/>
  } <br/>

Sample Response: <br/>
  Status Code : 201 Created <br/>
  {"message":"Signed Up Successfully"} <br/>

2)**Login API**: is used to login a user <br/>

Endpoint: /login <br/>
Mandatory Fields: email, password <br/>
  Sample Request:  <br/>
  { <br/>
	"email":"your_email@example.com", <br/>
	"password":"****" <br/>
  } <br/>

  Sample Response: <br/>
  Status Code : 200 OK <br/>
  { <br/>
    "refresh": "refresh_token", <br/>
    "access": "access_token"
  } <br/>

3)**Add User Details API**: Is used to add details for a particular user <br/>

Endpoint: /addUserDetails <br/>
Request Header: Authorization: Bearer <access_token> <br/>
Mandatory Fields: age, dob, profession, address, hobby <br/>
  Sample Request:  <br/>
  { <br/>
	"age":25, <br/>
	"dob":"1997-08-05", <br/>
	"profession":"Cab Driver", <br/>
	"address":"Los Angeles, CA", <br/>
	"hobby":"Sleeping" <br/>
  } <br/>

  Sample Response: <br/>
  Status Code : 200 OK <br/>
  { "message":"Added User Details Successfully" } <br/>
  
 4)**Update User Details API**: Is used to update details for a particular user <br/>

 Endpoint: /updateUserDetails <br/>
 Request Header: Authorization: Bearer <access_token> <br/>
 Optional Fields: age, dob, profession, address, hobby <br/>
 Sample Request:  <br/>
  { <br/>
	"age":24, <br/>
	"dob":"1999-07-12", <br/>
	"profession":"Accountant", <br/>
	"address":"San Diego, CA", <br/>
	"hobby":"Swimming" <br/>
  } <br/>

  Sample Response: <br/>
  Status Code : 200 OK <br/>
  {"message":"Updated User Details Successfully"} <br/>

5)**Delete User**: Is used to delete a particular user from the system & hence delete it's corresponding details <br/>
Endpoint: /deleteUsers <br/>
Request Header: Authorization: Bearer <access_token> <br/>
Status Code : 200 OK <br/>
{"message":"Deleted Successfully"} <br/>
