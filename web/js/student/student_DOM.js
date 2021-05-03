export function addConstraintHeadingDOM(courseCode) {
    return (
        `
        <th>${courseCode}</th>

        `
    );
}


export function addRowsAndColumnsDOM(rowCourseObj) {
    return (
        `
        <tr id=${rowCourseObj.courseId}>
            <th>${rowCourseObj.courseCode}</th>
        </tr>
        `
    );
}