// Initialize Firebase
var config = {
    apiKey: "AIzaSyD4Px2vgieA7bKPnjjI1CEPW5AbBg_lbXY",
    authDomain: "peed-0xdeadbeef-lab-1.firebaseapp.com",
    databaseURL: "https://peed-0xdeadbeef-lab-1.firebaseio.com",
    projectId: "peed-0xdeadbeef-lab-1",
    storageBucket: "peed-0xdeadbeef-lab-1.appspot.com",
    messagingSenderId: "867302589401"
};
firebase.initializeApp(config);

var dbRef = firebase.database().ref().child('Temperatures');

dbRef.on('child_added', function(data) {
    addData(data.key, parseFloat(data.val()));
});

dbRef.on('child_changed', function(data) {
    addData(data.key, parseFloat(data.val()));
});

function activateSensor() {
    firebase.database().ref().child("Button").set(1);
}

function deactivateSensor() {
    firebase.database().ref().child("Button").set(0);
}