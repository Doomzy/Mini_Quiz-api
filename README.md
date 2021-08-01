# Mini_Quiz-api
Quiz Restful API 

  **Admin:** 
  - username= admin 
  - password= djangoquizapp

 **Note:** 
 you have to send the user credentials in the headers like:
 ```
 - Authorization Basic (encoded with Base64)
```
**Student user creation**  (Admin users only) the url is:<br />
- account/create
 ```
 {
  "username": "",
  "password": "",
  "name": "",
  "academic_year": "" opt(1st,2nd,3rd)
}
 ```
 
Now onto the app I'm using two sets of urls :

- /subject  ***(Admin users only)***

 >- /create <br />
  **To send a Subject creation request**
 ```
 {
  "name": "",
  "academic_year": ""  opt(st1,2nd,3rd)
 }
 ```
 >- /delete <br />
  **To send a Subject deletion request**
 ```
 {
  "name": "",
 }
 ```
 >- /q_create <br />
  **To send a question creation request**
 ```
 {
    "subject": "" subject id
    "content": "",
    "ans1": "",
    "ans2": "",
    "ans3": "",
    "ans4": "",
    "correct_answer":""
}
 ```
 >- /q_delete <br />
  **To send a question deletion request**
 ```
 {
    "subject": "" subject id
    "content": "",
}

 ```
 
- /test  ***(Student users only)*** <br />
  **Note:** int is a placeholder for the subject id

>- /get/(int) <br />
  **To send a get Subject test request**
 ```
 No Data
 ```
 >- /post/(int) <br />
  **To send a post request with the test answers**
 ```
 [
    {
        "question_id": ,
        "chosen_answer": ""
    },
    {
        "question_id": ,
        "chosen_answer": ""
    },
    {
        "question_id": ,
        "chosen_answer": ""
    }
]
 ```
 >- /result/(int) <br />
  **To send a get request to get the Subjects test results**
 ```
 No Data
 ```
