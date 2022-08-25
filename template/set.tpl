<!DOCTYPE html>
<html lang="en">
<head>
    <title>voting.thing/set</title>
    <link rel="stylesheet" type="text/css" href="http://twitter.github.com/bootstrap/assets/css/bootstrap.css">
</head>
<body>
<!-- this really needs to be set dynamically with javascript -->
<!-- better, rewrite the set endpoint so that both values are POSTed -->
        <form action="/set" method="post">
            <fieldset>
                <legend>Set a key value</legend>
                key <input type="text" id="key" name="key" {{key_input}}>
                value <input type="text" id="value" name="value">
                <input type="submit" value="Set">
            </fieldset>
        </form>
</body>
</html>