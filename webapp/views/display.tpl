<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/tr/html4/strict.dtd">
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
	<title>20 most common words</title>

        <script language="javascript" type="text/javascript" src="js/jquery-2.0.3.min.js"></script>
        <script language="javascript" type="text/javascript" src="js/flot/jquery.flot.js"></script>
        <script language="javascript" type="text/javascript" src="js/flot/jquery.flot.categories.js"></script>

        <script type="text/javascript">
            $(function() {
               var topwords = {{!topwords}};
               var wordcounts = {{wordcounts}};

               var rawData = [];
               var ticks = [];
               for (var i = 0; i < wordcounts.length; i++) {
                   rawData[i] = [wordcounts[i], i];
                   ticks[i] = [i, topwords[i]];
               }
               var dataSet = [ { data: rawData } ];
                                                                       
               $.plot("#topwords", dataSet, { 
                                     series: { bars: { show: true } },
                                     bars: { barWidth: 0.6, align: "center", horizontal: true },
                                     //xaxis: { tickLength: 0 },
                                     yaxis: { mode: "categories", ticks: ticks }
                                    });
            });
        </script>
    </head>
    <body>
        <p>Files loaded: {{files}}</p>
        <p>20 most common words:</p>
        {{topwords}}
        <p>and their wordcounts:</p>
        {{wordcounts}}

        <div id="topwords" style="width:600px;height:600px"></div>
    </body>
</html>
