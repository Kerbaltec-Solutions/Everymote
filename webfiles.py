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

    button_list = ''
    for button in buttons.get_buttons(remote):
        button_list+=f'"{button[0]}",'
    page  = f"""<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Button Grid</title>
    <link rel="stylesheet" href="./styles.css">
</head>

<body>
    <h1>{remote}</h1>
    <div id="grid" class="grid"></div>
    <script>
        const grid = document.getElementById("grid");
        const predefinedButtons = [{button_list[:-1]}];

        function saveGridState() {{
            const state = {{}};
            [...grid.children].forEach((cell, index) => {{
                if (cell.firstChild) {{
                    state[cell.firstChild.id] = index;
                }}
            }});
            localStorage.setItem("grid_{remote}", JSON.stringify(state));
        }}

        function createDraggableButton(label) {{
            const btn = document.createElement("button");
            btn.textContent = label;
            btn.draggable = true;
            btn.id = "btn-" + label;
            btn.addEventListener("dragstart", (e) => {{
                e.dataTransfer.setData("text", e.target.id);
                e.dataTransfer.effectAllowed = "move";
            }});
            btn.addEventListener("click", () => {{
                fetch(`/remotes?remote="{remote}"&button=${{label}}`)
            }});
            return btn;
        }}

        function loadGridState() {{
            const state = JSON.parse(localStorage.getItem("grid_{remote}")) || {{}};
            const occupied = new Set(Object.values(state));
            let nextEmpty = 0;

            predefinedButtons.forEach(label => {{
                const btn = createDraggableButton(label);

                const position = state[btn.id];
                while (occupied.has(nextEmpty)) nextEmpty++;
                const targetIndex = position !== undefined ? position : nextEmpty;
                occupied.add(targetIndex);
                grid.children[targetIndex].appendChild(btn);
            }});
        }}

        for (let i = 0; i < 60; i++) {{
            const cell = document.createElement("div");
            cell.dataset.index = i;
            cell.addEventListener("dragover", (e) => e.preventDefault());
            cell.addEventListener("drop", (e) => {{
                e.preventDefault();
                const id = e.dataTransfer.getData("text");
                const draggedElement = document.getElementById(id);
                if (draggedElement && !cell.firstChild) {{
                    cell.appendChild(draggedElement);
                    saveGridState();
                }}
            }});
            grid.appendChild(cell);
        }}

        loadGridState();
    </script>
</body>

</html>"""
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