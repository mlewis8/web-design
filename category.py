import index


def newCategory_html():
    # /html/forms/news_category_insert.html
    return None


def catAdmin_html():
    # Create the body of the category administration page
    return None


def modify_category_html():
    return None


def modify_news_article_html():
    return None


def category_index_html():
    return None


def create_news_category_code(requestObject):
    # switch request objecgt
    if 'create_cat' in requestObject:
        index.include_header("Add_news_category")

        # Make sure the category name and description is posted before inserted into the database.

        # Insert the category name and description into the table news_category

        # Post the results and add a link for creating a new category

    elif 'new_cat' in requestObject:
        index.header_html("Create news category")
        newCategory_html()

    else:
        index.header_html("New Category Admnistration")
        catAdmin_html()
        index.footer_html()


def modify_news_category_code(requestObject):
    # switch request objecgt
    index.layout_code()
    index.adminCheck()
    # Create a dynamic form menu from the select  - page 156

    index.header_html("MOdify or delete category news")

    if 'mod_category' in requestObject:
        index.include_header("Add_news_category")

        # Make sure the category name and description is posted before inserted into the database.

        # Insert the category name and description into the table news_category

        # Post the results and add a link for creating a new category

    elif 'update_category' in requestObject:
        index.header_html("Create news category")
        newCategory_html()

    elif 'confirm_delete_category' in requestObject:
        # Print are you sure you want to

        # the yes link goes to modify_category_code with request object 'delete_category' - _POST['cat_id']
        # the no link goes to the modify_category_code with no request object
        print()
    elif 'delete_category' in requestObject:
        # mysql query to delete the rows based on _POST['cat_id']
        # provide feedback that the category was deleted
        print()
    else:
        category_index_html()

    index.footer_html()


def article_code(requestObject):
    index.layout_html()
    index.admin_check()
    return None
