## 1. Understanding `MTV (Model-Template-View) `pattern.

- Django follows the MTV (Model-Template-View) pattern.

The responsibilities in the Django MTV pattern are divided as follows:

• `Model`: This defines the logical data structure and is the data handler between the database
and the view.
• `Template`: This is the presentation layer. Django uses a plain-text template system that keeps
everything that the browser renders.
• `View`: This communicates with the database via the model and transfers the data to the template
for viewing.

When developing any Django project, you will always work with `models`, `views`, `templates`, and `URLs`.

![MTV (Model-Template-View)](images/mvt-arch.png)


# models

### django ORMORM stands for Object-Relational Mapper — and Django’s ORM is the system that:

> 📌 Connects your Python objects (classes) to relational database tables (like in PostgreSQL, MySQL, SQLite, etc.)

- create a model 
- tell django you're going to use those models by adding app in installed apps
- `python manage.py makemigrations` 
- run `python manage.py migrate`, 

usual requirements

- field name and it's type  [Model field reference](https://docs.djangoproject.com/en/5.2/ref/models/fields/)

- cardinalities 

### `makemigrations` - The Planner
- What it does:
- Looks at your models.py files
- Compares them to your last migration
- Creates a migration file that describes what needs to change in the database

> `makemigrations` doesn't touch your database - it just creates instructions.

### `migrate` - The Executor
What it does:
- Takes the migration files
- Actually applies the changes to your database
- Updates the database schema

### Admin
- create a super-user
- register your models in `admin.py`
- then you can use the django built in admin app to manage your models
- This is intened for managment purpose . **The admin’s recommended use is limited to an organization’s internal management tool. It’s not intended for building your entire front end around.**
- play with "QuerySet API" this will help in views

## Views

- A Django **`view`** is just a Python function that receives a web request and returns a web response. All the logic to return the desired response goes inside the view.

it is just a Python function (or class) where you use querysets and logic to get data, then pass that data to a template to render HTML.

- create your application views

example 

```python

views.py
from .models import Post
def post_list(request):
posts = Post.published.all()

```
