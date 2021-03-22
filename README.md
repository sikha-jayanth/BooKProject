# BooKProject
BOOK STORE PROJECT USING REST API

APIs - Requests and Responses

Request Method : GET (Search Fields - Author,Book name)
Url - http://127.0.0.1:8000/books/list (Complete List of Books)

Url - http://127.0.0.1:8000/books/detail/<int:pk> (Details of a particular book)

url: http://127.0.0.1:8000/books/authordetails/<int:pk>(To Retrieve author details)



Request Method : POST
Url - http://127.0.0.1:8000/books/create (To add a new book)

        	
Request Method : PUT(To update a particular book’s details)

Url - http://127.0.0.1:8000/books/update/<int:pk> 




Request Method : PATCH
Url - http://127.0.0.1:8000/books/update/<int:pk>
(To update a particular book’s details)




Url - http://127.0.0.1:8000/books/authorupdate/<int:pk>
(To update a particular author’s details)



Request Method : DELETE (To Delete a book)
Url -Url - http://127.0.0.1:8000/books/delete/<int:pk>
Response - status 204 no content


Additional Features - Searching list of books with search filters applied in GET method above that searches availability of books using author name or book name.
