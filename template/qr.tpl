<!DOCTYPE html>
<html lang="en">
<head>
    <title>voting.thing/qr</title>
    <link rel="stylesheet" type="text/css" href="http://twitter.github.com/bootstrap/assets/css/bootstrap.css">
</head>
<body>
        <form action="/qr" method="post">
            <fieldset>
                <legend>Generate a QR code</legend>
            <!--    key <input type="text" id="key" name="key" {{key_input}}>   -->
                data <input type="text" id="value" name="value">
                <input type="submit" value="Generate QR code">
            </fieldset>
        </form>
</body>
</html>