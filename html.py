__author__ = 'zavidan'
startpage = """
<html>
<head>
    <script type="text/javascript" src="/js/jquery-2.1.4.min.js"></script>
</head>
<body>
    <div>
        <a href="/test">Demo page</a>
        <a href="/edit">Make/Edit your house</a>
        <a href="/dataentry">Manual Data entry</a>
    </div>
</body>
</html>
"""

housemade = """
<html>
<head>
    <link rel="stylesheet" type="text/css" href="/css/edit.css">
    <script type="text/javascript" src="/js/house.js"></script>
    <script type="text/javascript" src="/js/jquery-2.1.4.min.js"></script>
</head>
<body onload="makehouse()">
    <table id="tab" cellspacing="0"></table>
    <form action="/edit" method="post">
        <input type="hidden" name="floorplan" value="{house}" id="floorplan">
        <input type="submit" id="submit" value="Save House">
    </form>
    <input type="button" onclick="toggle()" value"Toggle draw">
    <a href="/">Back to main page</a>
</body>
</html>
"""

dataentry = """
<html>
<head>
    <!--<link rel="stylesheet" type="text/css" href="/css/edit.css">-->
    <script type="text/javascript" src="/js/jquery-2.1.4.min.js"></script>
    <script type="text/javascript" src="/js/dataentry.js"></script>
</head>
<body>
    <div>
        <a href="/">Back to main page</a>
    </div>
    <form action="/dataentry" method="post" id="house">
        <!--<p>Room Names</p>-->
        <!--<table id="name"></table>-->
        <!--<p>Initial Temperatures</p>-->
        <!--<table id="temps"></table>-->
        <!--<p>U-Values of the Walls</p>-->
        <!--<table id="conductance"></table>-->
        <!--<p>Width of the Walls</p>-->
        <table id="area"></table>
        <!--<p>Room names</p>-->
        <!--<table id="capacity"></table>-->
        <!--<p>Room names</p>-->
        <input type="hidden" id="tarea" name="tarea">
        <input type="submit">
    </form>
    <input type="hidden" id="pyarea" name="pyarea" value="{pyarea}">
    <div id="click">
    bob
    </div>
</body>
</html>
"""