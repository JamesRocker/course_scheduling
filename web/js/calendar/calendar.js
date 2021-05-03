import Faculty from '../faculty.js';
import {addTimeSlotsDOM, addTimeChoicesDOM, disableEnableTimeBlockDOM, showHideBlocksOnCalendarDOM} from './calendar_DOM.js';
import {faculty} from '../course/course.js';
import {timeIntervals, timeObj, allTimeBlocksObj} from './time_interval.js';
import {changeState} from '../form.js';



export function calendarInit() {
    console.log('welcome to Calendar form!');

    // console.log(faculty);

    setUpEventListeners();

    window.updateAvailableTime = updateAvailableTime;
    window.updatePriority = updatePriority;

    createCalendar();
    createTimeChoices();

    
    //console.log(timeObj);
    
}


function setUpEventListeners() {
    let submitBtnElement = document.getElementById('submitBtn');
    submitBtnElement.addEventListener('click', formCheck);
}


function createCalendar() {

    const parentElement = document.getElementById('calendarTBody');

    for (let timeInterval of timeIntervals) {
        parentElement.insertAdjacentHTML('beforeend', addTimeSlotsDOM(timeInterval));
    }
}

function createTimeChoices() {
    const parentElement = document.getElementById('choices');
    
    for (let key in allTimeBlocksObj) {
        parentElement.insertAdjacentHTML('beforeend', addTimeChoicesDOM(allTimeBlocksObj[key]));
    }
    
}

function updateAvailableTime(code) {
    // use some() method to check if at least one element in the array passes a test.

    console.log('update available time');
    console.log(code);

    let timeBlockObj = allTimeBlocksObj[code];
    

    if (document.getElementById(`checkbox_${code}`).checked) {
        timeBlockObj.setSelected(true);
        timeBlockObj.toggleAvailability();
        // the checkbox has been checked
        
        updateTimeBlocksOverlap(timeBlockObj, true);
    }
    else {
        timeBlockObj.setSelected(false);
        timeBlockObj.toggleAvailability();
        // the checkbox has been unchecked

        // first, disable overlap with the current unselected time block
        updateTimeBlocksOverlap(timeBlockObj, false);
        // then, check with all selected blocks in case two or more blocks share same overlap
        checkWithSelectedBlocks();
    }


    showHideBlocksOnCalendarDOM(timeBlockObj, timeObj);

}

function updateTimeBlocksOverlap(currentTimeBlock, isChecked) {
    console.log('-------------- overlapped blocks ------------');
    for (let key in allTimeBlocksObj) {
        let timeBlock = allTimeBlocksObj[key];
        if (timeBlock.code !== currentTimeBlock.code) {
            if (checkAtLeastOneElementSame(currentTimeBlock.dayArr, timeBlock.dayArr)) {
                // if at least one day is the same, check if at least one time interval is same
                const isOverlapped = checkAtLeastOneElementSame(currentTimeBlock.numArr, timeBlock.numArr);
                if (isOverlapped) {
                    // at least one day is same and time interval is same.
                    // In other words, the two time blocks overlap
                    
                    if (isChecked) {
                        timeBlock.available = false;
                        console.log(timeBlock);

                        disableEnableTimeBlockDOM(timeBlock, true);
                    }
                    else {
                        timeBlock.available = true;
                        disableEnableTimeBlockDOM(timeBlock, false);
                    }
                }
            }
        }
    }
}

// basically, select again when overlap
// can be done more efficiently than this
function checkWithSelectedBlocks() {
    for (let key in allTimeBlocksObj) {
        let timeBlock = allTimeBlocksObj[key];
        if (timeBlock.selected) {
            updateTimeBlocksOverlap(timeBlock, true);
        }
    }
}

function checkAtLeastOneElementSame(currentArr, otherArr) {
    return currentArr.some(ele => otherArr.includes(ele));
}


// for priority checkbox
function updatePriority(code) {
    let timeBlockObj = allTimeBlocksObj[code];
    timeBlockObj.priority = document.getElementById(`selectbox_${timeBlockObj.code}`).value;
    
}


function formCheck() {
    console.log('form checked for calendar');

    let chosenTimeBlocks = {};
    for (let key in allTimeBlocksObj) {
        let timeBlock = allTimeBlocksObj[key];
        if (timeBlock.selected) {
            chosenTimeBlocks[key] = timeBlock;
        }
    }
    console.log(chosenTimeBlocks);

    // set the property in faculty
    faculty.availableTime = chosenTimeBlocks;

    console.log(JSON.stringify(faculty));


    let facultyDataJSON = JSON.stringify(faculty);

    sendData(facultyDataJSON);

}



function sendData(data) {
    let xmlhttp;
    if (window.XMLHttpRequest) {
        xmlhttp = new XMLHttpRequest();
    }
    else {
        xmlhttp = new ActiveXObject("Microsoft.XMLHTTP");
    }

    xmlhttp.open("POST", 'php/calendar.php', true);
    xmlhttp.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');

    let params = "data=" + data;

    xmlhttp.onreadystatechange = function() {
        if (this.readyState === 4 && this.status === 200) {
            console.log('here in js');
            console.log(xmlhttp.responseText);

            changeState();
        }
    };

    xmlhttp.send(params);
}