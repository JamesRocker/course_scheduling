import {courseInit} from './course/course.js';
import {addCourseLayoutToDOM} from './course/course_DOM.js';

import {calendarInit} from './calendar/calendar.js';
import {addCalendarLayoutToDOM} from './calendar/calendar_DOM.js';

const COURSE_FORM = 0;
const CALENDAR_FORM = 1;
// const STUDENT_CONSTRAINT_FORM = 2;

var currentState = undefined;
// var currentState = 0;

window.onload = () => {
    changeState();
    
};

export function changeState() {

    if (typeof currentState === 'undefined') {
        currentState = COURSE_FORM;
    }
    else if (currentState === COURSE_FORM) {
        currentState = CALENDAR_FORM;
    }
    else {
        console.log('Form has been completed. Thank you very much for your time!');
        window.location.href = "form_submitted.html";
    }

    
    if (currentState === COURSE_FORM) {
        document.getElementsByTagName('link')[0].href = "css/course.css";
        document.getElementsByTagName('body')[0].innerHTML = addCourseLayoutToDOM();
        courseInit();

    }
    else if (currentState === CALENDAR_FORM) {
        document.getElementsByTagName('link')[0].href = "css/calendar.css";
        document.getElementsByTagName('body')[0].innerHTML = addCalendarLayoutToDOM();
        calendarInit();
    }
    
}
