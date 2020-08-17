var timerdur = 10000;
var timerstarted = false;
var startdate = new Date();
var currdate = new Date();
var myVar;
const phase = document.getElementById("phase");
const starttime = document.getElementById("time");
const timerdisplay = document.getElementById("timer");

function main() {
    console.log("Hello");
    if(timerstarted) {
        currdate = new Date();
        console.log("huhu");
        timer = currdate - startdate;
        console.log(timer);
        if (timer >= 10000) {
            timerstarted = false;
            turn0();
        }
        timerdisplay.innerHTML = timersting(timer);
    } else {
        if(phase.innerHTML === "Phase: In_Round") {
            timerstarted = true;
            startdate = new Date(starttime.innerHTML);
        }
    }
    return 0;
};


function turn0() {

};

function timersting(timer) {
    let ourtimer = 10000 - timer;
    let seconds = Math.floor(ourtimer / 1000);
    let milliseconds = ((ourtimer - seconds*1000).toFixed(2))*100;

    return seconds.toString() + ":" + milliseconds.toString();
};

//main()
//setInterval(function (){console.log("ALARM!")}, 100);
setInterval(main, 100);


