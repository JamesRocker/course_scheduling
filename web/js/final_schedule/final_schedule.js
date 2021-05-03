import { timeIntervals, timeObj, allTimeBlocksObj } from '../calendar/time_interval.js';
import { calendarDOM, timeSlotsDOM, nameLinkDOM } from './final_schedule_DOM.js';

window.onload = init;

// const allFacultyObj = {
//     'AL': [
//         {'courseCode': 'MATH 109 A', 'timeCode': 'A', 'priority': 1},
//         {'courseCode': 'MATH 109 B', 'timeCode': 'B', 'priority': 1},
//         {'courseCode': 'MATH 364', 'timeCode': 'C', 'priority': 1}
//     ],
//     'BP': [
//         {'courseCode': 'MATH 110 A', 'timeCode': 'L', 'priority': 1},
//         {'courseCode': 'MATH 110 B', 'timeCode': 'M', 'priority': 1},
//         {'courseCode': 'MATH 340', 'timeCode': 'N', 'priority': 1}
//     ],
//     'DRM': [
//         {'courseCode': 'CHEM 303', 'timeCode': 'L', 'priority': 1},
//         {'courseCode': 'CHEM 306', 'timeCode': 'B', 'priority': 1},
//         {'courseCode': 'MATH 303 Lab', 'timeCode': 'S', 'priority': 1}
//     ]
// };

let allFacultyObj = undefined;

const PRIORITY_COLOR = {
    '1': 'blue',
    '2': 'green',
    '3': 'orange'
};

function init() {
    console.log('welcome from final solution page');
    console.log(timeObj);
    console.log(allTimeBlocksObj);
    
    getData();
    
}

function createNameLinks() {
    let names =  Object.keys(allFacultyObj);

    const parentElement = document.getElementById('namesContainer');

    for (let name of names) {
        parentElement.insertAdjacentHTML('beforeend', nameLinkDOM(name));
    }
}


function createCalendars() {

    let names =  Object.keys(allFacultyObj);

    const parentElement = document.getElementById('schedulesContainer');

    for (let name of names) {
        parentElement.insertAdjacentHTML('beforeend', calendarDOM(name));
        createOneTbody(name);
    }
   

}

function createOneTbody(name) {
    const tbodyParentElement = document.getElementById(`${name}_tbody`);
     
    for (let timeInterval of timeIntervals) {
        tbodyParentElement.insertAdjacentHTML('beforeend', timeSlotsDOM(name, timeInterval));
    }
}

function createAssignedTimeBlocks() {
    let names =  Object.keys(allFacultyObj);

    for (let name of names) {
        let facultyCourses = allFacultyObj[name];

        for (let facultyCourse of facultyCourses) {
            let timeCode = facultyCourse['timeCode'];

            let timeBlock = allTimeBlocksObj[timeCode];

            assignFacultyTimeBlocks(name, facultyCourse, timeBlock);
        }
        
    }
}


function assignFacultyTimeBlocks(name, facultyCourse, timeBlock) {
    let courseCode = facultyCourse.courseCode;
    let priority = facultyCourse.priority;
    console.log(priority);
    let backgroundColor = PRIORITY_COLOR[priority.toString()];

    let dayArr = timeBlock['dayArr'];
    let numArr = timeBlock['numArr'];
    console.log(timeBlock);

    for (let day of dayArr) {
        let counter = 0
        for (let num of numArr) {
            const [startTime, endTime]= timeObj[num];

            let tdElement1 = document.getElementById(`${name}_day_${day}_time_${startTime}`);

            if (counter === 0) {
                // start of course
                // put the course code
                tdElement1.innerText = courseCode;
            }
            
                
           
            // tdElement1.classList.add('colored-slot');
            
            tdElement1.style.backgroundColor = backgroundColor;
            tdElement1.style.borderTop = "none";
            tdElement1.style.borderBottom = "none";
            tdElement1.style.color = 'white';


            let tdElement2 = document.getElementById(`${name}_day_${day}_time_${endTime}`);
            
            if (tdElement2.style.backgroundColor === 'white') {
                tdElement2.style.backgroundColor = backgroundColor;
            }
            // tdElement2.style.backgroundColor = backgroundColor;
            tdElement2.style.borderTop = "none";
            tdElement2.style.borderBottom = "none";
            tdElement2.style.color = 'white';


            counter ++;
        }
    }
}


function getData() {
    let xmlhttp;
    if (window.XMLHttpRequest) {
        xmlhttp = new XMLHttpRequest();
    }
    else {
        xmlhttp = new ActiveXObject("Microsoft.XMLHTTP");
    }

    xmlhttp.open('GET', 'files/output_solution.json', true);
    xmlhttp.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');

    
    xmlhttp.onreadystatechange = function() {
        if (this.readyState === 4 && this.status === 200) {
            console.log('here in final schedule js');
            console.log(xmlhttp.responseText);

            let scheduleDataJSON = xmlhttp.responseText;
            allFacultyObj = JSON.parse(scheduleDataJSON);
            // console.log(allFacultyObj);


            // createNameLinks();
            createCalendars();
            createAssignedTimeBlocks();
            
        }
    };

    xmlhttp.send();
}