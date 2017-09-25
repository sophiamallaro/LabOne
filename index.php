<!DOCTYPE html>
<html lang="en">
<head>
</head>
<body>
    <style>
        body {
            background-color: lightblue;
        }
    </style>
    <canvas id="myChart" width="200" height="400"></canvas>
    Phone Number: <input type="text" name="model" id="phoneNum" /><br>
    Carrier: <select id="carrier">
        <option value="verizon">Verizon</option>
        <option value="uscell">US Cellular</option>
        <option value="att">AT&T</option>
        <option value="tmobile">T Mobile</option>
        <option value="spring">Sprint</option>
    </select><br>
    <button onclick="myFunction()">Button</button>
    <script>
        function myFunction() {
            var e = document.getElementById("carrier");
            var value = e.options[e.selectedIndex].value;
            var text = e.options[e.selectedIndex].text;
            var phoneNumber = document.getElementById('phoneNum').value;
            if(value == "verizon") {
                var email = phoneNumber + "@vtext.com";
            } else if(value == "uscell") {
                var email = phoneNumber + "@email.uscc.net";
            } else if(value == "att") {
                var email = phoneNumber + "@txt.att.net";
            } else if(value == "tmobile") {
                var email = phoneNumber + "@tmomail.net";
            } else if(value + "sprint") {
                var email = phoneNumber + "@messaging.sprintpcs.com";
            }
        }
        <?php
            $tmp = exec("py.py");
            echo $tmp;
        ?>
    </script>
</body>
<script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/2.1.4/Chart.min.js"></script>
<script src="https://www.gstatic.com/firebasejs/4.3.0/firebase.js"></script>
<script src="https://www.gstatic.com/firebasejs/4.3.0/firebase-database.js"></script>
<script src="Lab1/scripts/Chart.js"></script>
<script src="Lab1/scripts/firebaseAccess.js"></script>
</html>
