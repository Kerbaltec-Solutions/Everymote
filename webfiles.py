STYLESHEET = "https://bjoern-schnabel.de/Everymote/styles.css"

wifi_form = f"""<!DOCTYPE html>
<html>
    <head> 
        <title>Everymote</title> 
        <link rel="stylesheet" href="{STYLESHEET}">
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
def build_remotes():
    import buttons
    page = f"""<!DOCTYPE html>
<html>
    <head> 
        <title>Everymote</title> 
        <link rel="stylesheet" href="{STYLESHEET}">
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
        <link rel="stylesheet" href="{STYLESHEET}">
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
remote_form = f"""<!DOCTYPE html>
<html>
    <head> 
        <title>Everymote</title> 
        <link rel="stylesheet" href="{STYLESHEET}">
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
    page = f"""<!DOCTYPE html>
<html>
    <head> 
        <title>Everymote</title> 
        <link rel="stylesheet" href="{STYLESHEET}">
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
        <link rel="stylesheet" href="{STYLESHEET}">
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
        <link rel="stylesheet" href="{STYLESHEET}">
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
        <link rel="stylesheet" href="{STYLESHEET}">
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
update_page=f"""<!DOCTYPE html>
<html>
    <head> 
        <title>Everymote</title> 
        <link rel="stylesheet" href="{STYLESHEET}">
        <meta http-equiv="refresh" content="0; url=/" />
    </head>
    <body>
        <h1>UPDATING... Device will restart when LED lights up</h1>
    </body>
</html>
"""