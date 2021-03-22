# BooKProject
BOOK STORE PROJECT USING REST API

Admin/Superuser - can register, login, authenticate and perform all CRUD operations including search operations.
Normal Users - can login, Authenticate and view list of books, Details of a specific book, Details of author and perform search operations.
Normal users are added through admin interface

Using Class Based Views (generic views)

APIs - Requests and Responses

Request Method : GET (Search Fields - Author,Book name)
Url - http://127.0.0.1:8000/books/list (Complete List of Books)
Response - status 200 ok
Body:
[
    {
        "book_name": "Anna Karenina",
        "author_name": [
            {
                "author_name": "Leo Tolstoy",
                "url": "http://127.0.0.1:8000/books/authordetails/1"
            }
        ],
        "pub_year": 1878,
        "price": 500,
        "summary": "The story centers on an extramarital affair between Anna and dashing cavalry officer Count Alexei Kirillovich Vronsky that scandalizes the social circles of Saint Petersburg and forces the young lovers to flee to Italy in a search for happiness, but after they return to Russia, their lives further unravel."
    }
]










Url - http://127.0.0.1:8000/books/detail/<int:pk> (Details of a particular book)
Response - status 200 ok
Body:
{
    "book_name": "Anna Karenina",
    "author_name": [
        {
            "author_name": "Leo Tolstoy",
            "url": "http://127.0.0.1:8000/books/authordetails/1"
        }
    ],
    "pub_year": 1878,
    "price": 500,
    "summary": "The story centers on an extramarital affair between Anna and dashing cavalry officer Count Alexei Kirillovich Vronsky that scandalizes the social circles of Saint Petersburg and forces the young lovers to flee to Italy in a search for happiness, but after they return to Russia, their lives further unravel."
}
url: http://127.0.0.1:8000/books/authordetails/<int:pk>(To Retrieve author details)
Response - status 200 ok
Body:
{
    "id": 1,
    "author_name": "Leo Tolstoy",
    "Born": "9 September 1828 Yasnaya Polyana",
    "About": "Leo Tolstoy, was a Russian writer who is regarded as one of the greatest authors of all time. He received nominations for the Nobel Prize in Literature every year from 1902 to 1906 and for the Nobel Peace Prize in 1901, 1902, and 1909. That he never won is a major controversy."
}

 
 







Request Method : POST
Url - http://127.0.0.1:8000/books/create (To add a new book)

Body -
{
"book_name": "Anna Karenina",
        	"author_name": [
            	{
               	 "author_name": "Leo Tolstoy"
               
           	 }
      	  ],
	"pub_year": 1878,
	"price": 500,
 "summary": "The story centers on an extramarital affair between Anna and dashing cavalry officer Count Alexei Kirillovich Vronsky that scandalizes the social circles of Saint Petersburg and forces the young lovers to flee to Italy in a search for happiness, but after they return to Russia, their lives further unravel."
    }
	Response - status 201 created



        	
Request Method : PUT
Url - http://127.0.0.1:8000/books/update/<int:pk> 
(To update a particular book’s details)

Body - 
{
"book_name": "Anna Karenina",
        	"author_name": [
            	{
               	 "author_name": "Leo Tolstoy"
               
           	 }
      	  ],
       	 "pub_year": 1878,
       	 "price": 500,
 "summary": "The story centers on an extramarital affair between Anna and dashing cavalry officer Count Alexei Kirillovich Vronsky that scandalizes the social circles of Saint Petersburg."
    }
Response - status 200 ok











Request Method : PATCH
Url - http://127.0.0.1:8000/books/update/<int:pk>
(To update a particular book’s details)


Body - 
{
       	 "price": 550
     }
Response - status 200 ok

Url - http://127.0.0.1:8000/books/authorupdate/<int:pk>
(To update a particular author’s details)

Request Body-
{
       "About": "Leo Tolstoy, was a Russian writer who is regarded as one of the greatest authors of all time. He received nominations for the Nobel Prize in Literature every year from 1902 to 1906 ."
}

Response - status 200 ok

 





Request Method : DELETE (To Delete a book)
Url -Url - http://127.0.0.1:8000/books/delete/<int:pk>
Response - status 204 no content




Additional Features - Searching list of books with search filters applied in GET method above that searches availability of books using author name or book name.
