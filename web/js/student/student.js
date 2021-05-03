
// // import {addCourseFieldToDOM} from './course_DOM.js';
import {addConstraintHeadingDOM, addRowsAndColumnsDOM} from './student_DOM.js';


window.onload = init;

var studentConstraints = {};
var combinedCoursesArr;

const colors = ['red','blue', 'white']; // here white refers to none
// blue = not desirable to overlap
// red -> no two courses can be overlapped
const colorConstraint = {'red': 'hard', 'blue': 'soft', 'white': 'none'};


function init() {
    console.log('welcome to student form!');

    window.handleCellClick = handleCellClick;
    
    setUpEventListeners();

    sendGetData('GET');
}


function setUpEventListeners() {
    let submitBtnElement = document.getElementById('studentSubmitBtn');
    submitBtnElement.addEventListener('click', formCheck);
}



function sendGetData(request, params="") {
    let xmlhttp;
    if (window.XMLHttpRequest) {
        xmlhttp = new XMLHttpRequest();
    }
    else {
        xmlhttp = new ActiveXObject("Microsoft.XMLHTTP");
    }

    xmlhttp.open(request, 'php/student_constraint.php', true);
    xmlhttp.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');

    
    xmlhttp.onreadystatechange = function() {
        if (this.readyState === 4 && this.status === 200) {

            if (request === "GET") {
                console.log('here in js');
                console.log(xmlhttp.responseText);

                let scheduleDataJSON = xmlhttp.responseText;
                let scheduleDataObj = JSON.parse(scheduleDataJSON);
                console.log(scheduleDataObj);

                combinedCoursesArr = combineCourses(scheduleDataObj);

                initializeStudentConstraints();
                
                generateTable(combinedCoursesArr);
            }
            else if (request === "POST") {
                console.log('here in js');
                console.log(xmlhttp.responseText);
                console.log('Submitted!! Thank you very much for your time.');

                window.location.href = "form_submitted.html";
            }
            
        }
    };

    xmlhttp.send(params);
}

function combineCourses(scheduleDataObj) {
    let combinedCoursesArr = [];

    for (let scheduleObj of scheduleDataObj) {
        for (let courseObj of scheduleObj.courses) {
            combinedCoursesArr.push(courseObj);
        }
    }

    // update course id: this course id is not a real course id. It's just for temporary. It's better to use uuid rather than this but I will use this for simplicity.
    let counter = 0;
    for (let course of combinedCoursesArr) {
        course.courseId = counter;
        counter += 1;
    }


    console.log(combinedCoursesArr);

    return combinedCoursesArr;
}

function initializeStudentConstraints() {
    for (let courseObj of combinedCoursesArr) {
        studentConstraints[courseObj.courseCode] = [];
    }
}

function generateTable(combinedCoursesArr) {

    let rowHeadingElement = document.getElementById('rowHeading');

    for (let courseObj of combinedCoursesArr) {
        rowHeadingElement.insertAdjacentHTML('beforeend', addConstraintHeadingDOM(courseObj.courseCode));
    }

    let tableBodyElement = document.getElementsByTagName('tbody')[0];
    for (let courseObj of combinedCoursesArr) {
        tableBodyElement.insertAdjacentHTML('beforeend', addRowsAndColumnsDOM(courseObj));
       
        for (let anothercourseObj of combinedCoursesArr) {
            let tdElement = document.createElement('td');
            tdElement.id = `row_${courseObj.courseId}_col_${anothercourseObj.courseId}`;
            tdElement.dataset.row = courseObj.courseId;
            tdElement.dataset.col = anothercourseObj.courseId;
            tdElement.dataset.colorindx = colors.length - 1; // refers to white
            tdElement.setAttribute('onclick', `handleCellClick(${courseObj.courseId}, ${anothercourseObj.courseId})`);

            // push to student constraint obj
            studentConstraints[courseObj.courseCode].push({
                courseCode: anothercourseObj.courseCode,
                constraint: colorConstraint[colors[colors.length - 1]]
            });


            document.getElementById(`${courseObj.courseId}`).appendChild(tdElement);
        }
        
    }

}

function handleCellClick(firstCourseID, secondCourseID) {
    console.log(firstCourseID, secondCourseID);

    // handle the color
    let tdElement = document.getElementById(`row_${firstCourseID}_col_${secondCourseID}`);
    let colorInt = parseInt(tdElement.dataset.colorindx);
    colorInt ++;
    let newColorIndx = colorInt % colors.length;

    let tdElement2 = document.getElementById(`row_${secondCourseID}_col_${firstCourseID}`);

    tdElement.dataset.colorindx = newColorIndx;
    tdElement2.dataset.colorindx = newColorIndx;

    tdElement.style.backgroundColor = colors[newColorIndx];
    tdElement2.style.backgroundColor = colors[newColorIndx];

    // 
    let firstCourseCode = getCourseCodeFromId(firstCourseID);
    let secondCourseCode = getCourseCodeFromId(secondCourseID);
    console.log(firstCourseCode);
    console.log(secondCourseCode);

    let otherCoursesArr = studentConstraints[firstCourseCode];
    for (let otherCourse of otherCoursesArr) {
        if (otherCourse.courseCode === secondCourseCode) {
            otherCourse.constraint = colorConstraint[colors[newColorIndx]];
        }
    }

    let otherCoursesArr2 = studentConstraints[secondCourseCode];
    for (let otherCourse of otherCoursesArr2) {
        if (otherCourse.courseCode === firstCourseCode) {
            otherCourse.constraint = colorConstraint[colors[newColorIndx]];
        }
    }


}

function getCourseCodeFromId(id) {
    for (let course of combinedCoursesArr) {
        if (course.courseId === id) {
            return course.courseCode;
        }
    }
}

function restructureDataFormat () {
    let sorted_keys = Object.keys(studentConstraints).sort();

    console.log(sorted_keys);
    let constraints = [];

    for (let key of sorted_keys) {
        let studentConstraintArr = studentConstraints[key];
        for (let constraintObj of studentConstraintArr) {
            if (constraintObj.courseCode !== key && constraintObj.constraint !== 'none' && key < constraintObj.courseCode) {
                constraints.push({
                    "course_1": key,
                    "course_2": constraintObj.courseCode,
                    "type": constraintObj.constraint
                });
            }
        }
    }

    return constraints;
}

function formCheck() {
    console.log('form checked for student');

    console.log(studentConstraints);

    let structuredConstraints = restructureDataFormat();

    let studentConstraintsJSON = JSON.stringify(structuredConstraints);
    console.log(studentConstraintsJSON);

    let params = `constraints_data=${studentConstraintsJSON}`;
    
    sendGetData('POST', params);
}




