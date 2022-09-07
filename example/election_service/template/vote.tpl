<html>
Ballot paper
<body>
    <form action="/vote/{{anon_voter_id}}" method="post">
        <fieldset>
            <legend>Vote for</legend>
            Turniphead <input type="checkbox" name="value" value="yes">
            <input type="submit" value="Vote">
        </fieldset>
    </form>
</body>
</html>
