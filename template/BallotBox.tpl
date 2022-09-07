<html>
<h2>BallotBox</h2>
<p>v{{ version }}

<p>Private Property, keep out</p>

<form action="/lodge" method="POST">
    <input type="text" name="apikey" value="{{ apikey }}" hidden>
    <input type="text" name="electionkey" value="{{ electionkey }}" hidden>
    <input type="text" name="ballotpaper">
    <input type=submit>
</form>

<form action="/dump" method="POST">
    <input type="text" name="apikey" value="{{ apikey }}" hidden>
    <input type=submit value="display box contents">
</form>


<p>This BallotBox is provided by 'Jim's Cloud Practitioners'
<p>under supervision of the Government Democracy Commissioner.
</html>