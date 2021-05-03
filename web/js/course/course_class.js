class Course {

    static courseID = -1; // for simplicity, using num but better to use uuid

    constructor(id) {
        this.courseId = id; // just to keep track of unique course

        this.subjectCode = [];
        this.level = [];
        this.isLab = false;
        this.courseCode = "";
        this.courseName = "";
    }

    updateData({subjectCodeArr, levelArr, isLab, courseCode, courseName}) {
        this.subjectCode = subjectCodeArr;
        this.level = levelArr;
        this.isLab = isLab;
        this.courseCode = courseCode;
        this.courseName = courseName;
    }

    static generateNewID() {
        this.courseID = this.courseID + 1;
        return this.courseID;
    }

}

export default Course;