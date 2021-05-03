import Faculty from '../faculty.js';
import Course from './course_class.js';
import {addCourseFieldToDOM} from './course_DOM.js';
import {changeState} from '../form.js';

export var faculty = null;

export function courseInit() {
    console.log('welcome');

    setUpEventListeners();

    faculty = new Faculty();

    // create one course
    addCourseField();

    // expose to window object so that we can access in html
    window.removeCourseField = removeCourseField;
}




function setUpEventListeners() {
    let addBtnElement = document.getElementById('addBtn');
    addBtnElement.addEventListener('click', addCourseField);

    let nextBtnElement = document.getElementById('nextBtn');
    nextBtnElement.addEventListener('click', formCheck);
}



function addCourseField() {
    const newCourseID = Course.generateNewID();
    console.log(newCourseID);

    let course = new Course(newCourseID);

    let courseFormElement = document.getElementById('courseForm');
    courseFormElement.insertAdjacentHTML('beforeend', addCourseFieldToDOM(newCourseID));


    faculty.addCourse(course);
    
}

function removeCourseField(indx) {

    console.log(`delete button ${indx} clicked`);

    let childNode = document.getElementById(`fieldset_${indx}`);
    childNode.remove();

    faculty.removeCourse(indx);
}




function handleMultipleCheckBoxesData(className) {
    let result = [];

    const elements = document.getElementsByClassName(className);
    for (let element of elements) {
        if (element.checked) {
            result.push(element.dataset.name);
        }
    }

    return result;
}

function fillCourseData(indx) {

    let subjectCodeArr = handleMultipleCheckBoxesData(`subject-code-checkbox-${indx}`);
    if (subjectCodeArr.length === 0) {
        alert('Subject Code required! All marked with * are required.');
        return false;
    }

    let levelArr = handleMultipleCheckBoxesData(`level-checkbox-${indx}`);
    if (levelArr.length === 0) {
        alert('Level required! All marked with * are required.');
        return false;
    }


    let isLab = false;
    let isLabElement = document.getElementById(`isLabCheckBox${indx}`);
    if (isLabElement.checked) {
        isLab = true;
    }

    let courseCodeElement = document.getElementById(`courseCodeText${indx}`);
    let courseCode = "";
    if (courseCodeElement.value.length > 0) {
        courseCode = courseCodeElement.value;
    } 
    else {
        alert('Course Code required! All marked with * are required.');
        return false;
    }

    let courseNameElement = document.getElementById(`courseNameText${indx}`);
    let courseName = "";
    if (courseNameElement.value.length > 0) {
        courseName = courseNameElement.value;
    }
    else {
        alert('Course Name required! All marked with * are required.');
        return false;
    }

    let courseObj = {subjectCodeArr, levelArr, isLab, courseCode, courseName};
    console.log(courseObj);

    return courseObj;
}


function formCheck() {
    // assign name to faculty
    let facultyNameElement = document.getElementById('facultyName');
    let facultyName = "";
    if (facultyNameElement.value.length > 0) {
        facultyName = facultyNameElement.value;
    }
    else {
        alert('Faculty Name required! All marked with * are required.');
        return;
    }
    faculty.setName(facultyName);


    // courses data
    for (let course of faculty.courses) {
        const courseId = course.courseId;
        console.log(courseId);

        let courseDataObj = fillCourseData(courseId);
        if (courseDataObj === false) {
            return;
        }
        course.updateData(courseDataObj);

    }
    

    console.log(faculty);

    changeState();

}




// let testObj = {
//     subjectCodeArr: ["CMPT", "MATH"],
//     levelArr: [3, 4],
//     isLab: false,
//     courseCode: "CMPT 243",
//     courseName: "Algorithms and Data Structures"
// };
