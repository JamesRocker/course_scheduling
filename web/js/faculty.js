class Faculty {
    constructor() {
        this.facultyName = "";
        this.courses = [];
        this.availableTime = {};
    }

    setName(name) {
        this.facultyName = name;
    }

    getName() {
        return this.facultyName;
    }

    addCourse(course) {
        this.courses.push(course);
    }

    removeCourse(key) {
        for (let indx=0; indx < this.courses.length; indx ++) {
            let course = this.courses[indx];
            if (course.courseId === key) {
                this.courses.splice(indx, 1);
                break;
            }
        }
        
    }

    getCoursesLength() {
        return this.courses.length;
    }
}

export default Faculty;