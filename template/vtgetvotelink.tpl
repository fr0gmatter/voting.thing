<!DOCTYPE html>
<html lang="en">
<head>
    <title>voting.thing registration form</title>
    <link rel="stylesheet" type="text/css" href="http://twitter.github.com/bootstrap/assets/css/bootstrap.css">
</head>
<body>
    <form action="/votingthing/get_vote_link" method="post">
        <fieldset>
            <legend>Get election URL for</legend>
            label <input type="text" id="label" name="label"><br>
            firstname <input type="text" id="fname" name="fname" disabled><br>
            lastname <input type="text" id="lname" name="lname" disabled><br>
            enable electronic voting <input type="checkbox" id="EV" name="EV" value="yes" disabled><br>
            <input type="submit" value="Get voting url">
        </fieldset>
    </form>
</body>
</html>