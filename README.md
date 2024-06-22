# my_site
This is a Django project

### This is the project I'm working to learn Django and develop my skills as a backend developer.

## Technologies Used:
- Python
- Django
- HTML
- CSS

## Apps in this project:
# Implemented
- Blog App

# To be implemented in a future project:
- Store App (E-commerce)


## Still in consideration for implementation:
- A very efficient and basic search engine for the blog app
- A user authentication system for the blog app
- An Update System for posts in the blog app


## New terminal things learnt
create a .gitignore file
To untrack the files that shouldn't be commited :
git rm -r --cached env/

## HTML Form Encoding Types and Issue I had
With regards to allowing my forms collect both text and file data at the same time, I had an issue with the enctype attribute in my HTML form. I was using the default value of "application/x-www-form-urlencoded" which meant that the file data was not being sent to the server.

To fix this, I had to change the enctype attribute to "multipart/form-data" which allows for file data to be sent along with text data.

Here's an example of how to do this in HTML:

```html
<form method="post" enctype="multipart/form-data">
  <input type="file" name="myFile">
  <input type="text" name="myText">
  <input type="submit" value="Submit">
</form>
```

In this example, the form has two input fields: one for the file and one for the text. The enctype attribute is set to "multipart/form-data" to allow for file data to be sent along with text data. When the form is submitted, both the file and text data will be sent to the server.

Note: If you have a form that only has text fields, you can use the default value of "application/x-www-form-urlencoded" and skip the enctype attribute.
