/**
 * Created by jasonryan on 9/24/17.
 */
function $(id) {
    return document.getElementById(id);
}

function onActivateButtonClick() {
    var button = $("activate");
    if (button.innerText == "Activate Sensor") {
        activateSensor();
        button.innerText = "Deactivate Sensor";
    } else if (button.innerText == "Deactivate Sensor") {
        deactivateSensor();
        button.innerText = "Activate Sensor";
    }
}