wifi_form = """<!DOCTYPE html>
<html>
    <head> 
        <title>Everymote</title> 
        <link rel="stylesheet" href="/styles.css">
    </head>
    <body>
        <h1>Everymote</h1>
        <form action="/connect" method="get">
            SSID: <input type="text" name="ssid" required><br>
            Password: <input type="password" name="password"><br>
            <input type="submit" value="Connect">
        </form>
    </body>
</html>
"""
css = """/* styles.css */
* {
    margin: 1%;
    padding: 1%;
    box-sizing: border-box;
}
body {
    font-family: Arial, sans-serif;
    line-height: 1.6;
    color: #333;
}
h1 {
    margin: 15px;
    color: #446;
    text-align: center;
    font-size: 60px;
}
.pile {
    display: flex;
    flex-direction: row;
    flex-wrap: wrap;
}
input {
    font-size: 30px;
    flex: 1 1 100px;
    margin: 10px;
    align-items: center;
    justify-content: center;
    line-height: 50px; 
}
"""
def build_remotes():
    import buttons
    page = """<!DOCTYPE html>
<html>
    <head> 
        <title>Everymote</title> 
        <link rel="stylesheet" href="/styles.css">
    </head>
    <body>
        <h1>Your Remotes</h1>
        <form action="/remotes" method="get">
            <div class="pile">
            <input type="submit" name="page" value="NEW Remote"><input type="submit" name="page" value="REMOVE Remote"><input type="submit" name="page" value="UPDATE">
            </div>
            <div class="pile">
"""
    for remote in buttons.get_remotes():
        page+=f'\n                <input type="submit" name="page" value="{remote}">'
    page +="""
            </div>
        </form>
    </body>
</html>
"""
    return page
def build_buttons(remote):
    import buttons
    page = f"""<!DOCTYPE html>
<html>
    <head> 
        <title>Everymote</title> 
        <link rel="stylesheet" href="/styles.css">
    </head>
    <body>
        <h1>{remote}</h1>
        <form action="/remotes" method="get">
            <input type="hidden" name="remote" value="{remote}">
            <div class="pile"><input type="submit" name="page" value="HOME"><input type="submit" name="page" value="EDIT or ADD buttons"><input type="submit" name="page" value="REMOVE buttons"></div>
            <div class="pile">
"""
    for button in buttons.get_buttons(remote):
        page+=f'\n                <input type="submit" name="button" value="{button[0]}">'
    page +="""
            </div>
        </form>
    </body>
</html>
"""
    return page
remote_form = """<!DOCTYPE html>
<html>
    <head> 
        <title>Everymote</title> 
        <link rel="stylesheet" href="/styles.css">
    </head>
    <body>
        <h1>Add new Remote</h1>
        <form action="/remotes/add" method="get">
            <input type="text" name="remote" required>
            <input type="submit" value="Create">
        </form>
    </body>
</html>
"""
def build_remoteRM_form():
    import buttons
    page = """<!DOCTYPE html>
<html>
    <head> 
        <title>Everymote</title> 
        <link rel="stylesheet" href="/styles.css">
    </head>
    <body>
        <h1>Remove Remote</h1>
        <form action="/remotes/rm" method="get">
            <div class="pile">
"""
    for remote in buttons.get_remotes():
        page+=f'\n                <input type="submit" name="remote" value="{remote}">'
    page +="""
            </div>
        </form>
    </body>
</html>
"""
    return page
def build_button_form(remote):
    import buttons
    page = f"""<!DOCTYPE html>
<html>
    <head> 
        <title>Everymote</title> 
        <link rel="stylesheet" href="/styles.css">
    </head>
    <body>
        <h1>Change buttons of {remote}</h1>
        <form action="/buttons/add" method="get">
            <input type="hidden" name="remote" value="{remote}">
            <div class="pile">
                <input type="text" name="button">
                <input type="submit" value="ADD">
            </div>
        </form>
        <form action="/buttons/add" method="get">
            <input type="hidden" name="remote" value="{remote}">
            <div class="pile">
            """
    for button in buttons.get_buttons(remote):
        page+=f'\n                <input type="submit" name="button" value="{button[0]}">'
    page +="""
            </div>
        </form>
    </body>
</html>
"""
    return page
def build_buttonRM_form(remote):
    import buttons
    page = f"""<!DOCTYPE html>
<html>
    <head> 
        <title>Everymote</title> 
        <link rel="stylesheet" href="/styles.css">
    </head>
    <body>
        <h1>Remove button from {remote}</h1>
        <form action="/buttons/rm" method="get">
            <input type="hidden" name="remote" value="{remote}">
            <div class="pile">
            """
    for button in buttons.get_buttons(remote):
        page+=f'\n                <input type="submit" name="button" value="{button[0]}">'
    page +="""
            </div>
        </form>
    </body>
</html>
"""
    return page
def build_redirect(url):
    page=f"""<!DOCTYPE html>
<html>
    <head> 
        <title>Everymote</title> 
        <meta http-equiv="refresh" content="0; url={url}" />
    </head>
    <body>
        <form action="{url}" method="get">
            <input type="submit" value="Redirect">
        </form>
    </body>
</html>

"""
    return(page)
update_page="""<!DOCTYPE html>
<html>
    <head> 
        <title>Everymote</title> 
        <link rel="stylesheet" href="/styles.css">
    </head>
    <body>
        <h1>UPDATING... Restart device when LED lights up</h1>
    </body>
</html>
"""