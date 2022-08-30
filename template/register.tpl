<!DOCTYPE html>
<html lang="en">
<head>
    <title>voting.thing registration form</title>
    <link rel="stylesheet" type="text/css" href="http://twitter.github.com/bootstrap/assets/css/bootstrap.css">
</head>
<body>
    <form action="/register" method="post">
        <fieldset>
            <legend>Register for electronic voting</legend>
            label <input type="text" id="label" name="label"><br>
            firstname <input type="text" id="fname" name="fname"><br>
            lastname <input type="text" id="lname" name="lname"><br>
            enable electronic voting <input type="checkbox" id="EV" name="EV" value="yes"><br>
            <input type="submit" value="Register">
        </fieldset>
    </form>
</body>
</html>
