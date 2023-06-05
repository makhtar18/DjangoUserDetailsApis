# DjangoUserDetailsApis

This project consists of follwing APIs:

1)**Signup API**: : is used to add a user <br/>
  &emsp; Endpoint: /signup <br/>
  &emsp; Mandatory Fields: email, first_name, last_name, phone_number, password <br/>
  &emsp; Sample Request:  <br/>
  &emsp; { <br/>
  &emsp;&emsp; "email":"your_email@example.com",  <br/>
  &emsp;&emsp;  "first_name":"Your_First_Name", <br/>
  &emsp;&emsp;  "last_name":"Your_Last_Name", <br/>
  &emsp;&emsp;  "phone_number":"2123456789", <br/>
  &emsp;&emsp;  "password":"****" <br/>
  &emsp; } <br/>

&emsp; Sample Response: <br/>
&emsp; Status Code : 201 Created <br/>
&emsp; {"message":"Signed Up Successfully"} <br/>

2)**Login API**: is used to login a user <br/>

&emsp; Endpoint: /login <br/>
&emsp; Mandatory Fields: email, password <br/>
&emsp; Sample Request:  <br/>
&emsp; { <br/>
&emsp; &emsp; "email":"your_email@example.com", <br/>
&emsp; &emsp; "password":"****" <br/>
&emsp; } <br/>

&emsp; Sample Response: <br/>
&emsp; Status Code : 200 OK <br/>
&emsp; { <br/>
&emsp; &emsp; "refresh": "refresh_token", <br/>
&emsp; &emsp; "access": "access_token" <br/>
&emsp;} <br/>

3)**Add User Details API**: Is used to add details for a particular user <br/>

&emsp; Endpoint: /addUserDetails <br/>
&emsp; Request Header: Authorization: Bearer <access_token> <br/>
&emsp; Mandatory Fields: age, dob, profession, address, hobby <br/>
&emsp; Sample Request:  <br/>
  &emsp; { <br/>
	&emsp;&emsp; "age":25, <br/>
	&emsp;&emsp; "dob":"1997-08-05", <br/>
	&emsp;&emsp; "profession":"Cab Driver", <br/>
	&emsp;&emsp; "address":"Los Angeles, CA", <br/>
	&emsp;&emsp; "hobby":"Sleeping" <br/>
  &emsp; } <br/>

  &emsp;Sample Response: <br/>
  &emsp;Status Code : 200 OK <br/>
  &emsp;{ "message":"Added User Details Successfully" } <br/>
  
 4)**Update User Details API**: Is used to update details for a particular user <br/>

 &emsp; Endpoint: /updateUserDetails <br/>
 &emsp; Request Header: Authorization: Bearer <access_token> <br/>
 &emsp; Optional Fields: age, dob, profession, address, hobby <br/>
 &emsp; Sample Request:  <br/>
  &emsp; { <br/>
	&emsp;&emsp; "age":24, <br/>
	&emsp;&emsp; "dob":"1999-07-12", <br/>
	&emsp;&emsp; "profession":"Accountant", <br/>
	&emsp;&emsp; "address":"San Diego, CA", <br/>
	&emsp;&emsp; "hobby":"Swimming" <br/>
  &emsp; } <br/>

  &emsp; Sample Response: <br/>
  &emsp; Status Code : 200 OK <br/>
  &emsp; {"message":"Updated User Details Successfully"} <br/>

5)**Delete User**: Is used to delete a particular user from the system & hence delete it's corresponding details <br/>
&emsp; Endpoint: /deleteUsers <br/>
&emsp; Request Header: Authorization: Bearer <access_token> <br/>
&emsp; Status Code : 200 OK <br/>
&emsp; {"message":"Deleted Successfully"} <br/>
