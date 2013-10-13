<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/tr/html4/strict.dtd">
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
	<title>Files</title>

        <script language="javascript" type="text/javascript" src="js/jquery-2.0.3.min.js"></script>

	<script type="text/javascript">
            $(function() {
                var files = {{!files}};

                for (var i = 0; i < files.length; i++) {
                    $(filelinks).append("<a href='/displayfile/" + files[i] + "'>" + files[i] + "</a><br/>");
                }
            });
        </script>
    </head>
    <body>
        <p>Uploaded files:</p>

        <div id="filelinks"></div>

	<br/>

        <form action="/displayfiles" method="post" enctype="multipart/form-data">
            Upload new file: <input name="data" type="file" />
                             <input value="upload" type="submit" />
        </form>
    </body>
</html>
