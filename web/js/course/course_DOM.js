export function addCourseFieldToDOM(indx) {

    return (
        `<fieldset id="fieldset_${indx}">
            <legend>Course ${indx}</legend>

            <div class="fields">
                <label class="fields-items">Subject Code (<span class="required">*</span>):</label>
                <div class="fields-items multiple">
                    <div class="multiple-checkboxes">
                        <input data-name='BIO' class="subject-code-checkbox-${indx}" type="checkbox" id='BIO_${indx}'/>
                        <label for='BIO_${indx}'>BIO</label>
                    </div>

                    <div class="multiple-checkboxes">
                        <input data-name='CHEM' class="subject-code-checkbox-${indx}" type="checkbox" id='CHEM_${indx}'/>
                        <label for='CHEM_${indx}'>CHEM</label>
                    </div>

                    <div class="multiple-checkboxes">
                        <input data-name='CMPT' class="subject-code-checkbox-${indx}" type="checkbox" id='CMPT_${indx}'/>
                        <label for='CMPT_${indx}'>CMPT</label>
                    </div>

                    <div class="multiple-checkboxes">
                        <input data-name='ENVS' class="subject-code-checkbox-${indx}" type="checkbox" id='ENVS_${indx}'/>
                        <label for='ENVS_${indx}'>ENVS</label>
                    </div>

                    <div class="multiple-checkboxes">
                        <input data-name='MATH' class="subject-code-checkbox-${indx}" type="checkbox" id='MATH_${indx}'/>
                        <label for='MATH_${indx}'>MATH</label>
                    </div>

                    <div class="multiple-checkboxes">
                        <input data-name='NATS' class="subject-code-checkbox-${indx}" type="checkbox" id='NATS_${indx}'/>
                        <label for='NATS_${indx}'>NATS</label>
                    </div>

                    <div class="multiple-checkboxes">
                        <input data-name='PHYS' class="subject-code-checkbox-${indx}" type="checkbox" id='PHYS_${indx}'/>
                        <label for='PHYS_${indx}'>PHYS</label>
                    </div>
                    
                </div>
            </div>

            <div class="fields">
                <label class="fields-items">Level (<span class="required">*</span>):</label>
                <div class="fields-items multiple">
                    <div class="multiple-checkboxes">
                        <input data-name='1' class="level-checkbox-${indx}" type="checkbox" id='1_${indx}'/>
                        <label for='1_${indx}'>1</label>
                    </div> 
                    <div class="multiple-checkboxes">
                        <input data-name='2' class="level-checkbox-${indx}" type="checkbox" id='2_${indx}'/>
                        <label for='2_${indx}'>2</label>
                    </div> 
                    <div class="multiple-checkboxes">
                        <input data-name='3' class="level-checkbox-${indx}" type="checkbox" id='3_${indx}'/>
                        <label for='3_${indx}'>3</label>
                    </div> 
                    <div class="multiple-checkboxes">
                        <input data-name='4' class="level-checkbox-${indx}" type="checkbox" id='4_${indx}'/>
                        <label for='4_${indx}'>4</label>
                    </div> 
                </div>
            </div>

            <div class="fields">
                <label class="fields-items">Is Lab:</label>
                <div class="fields-items multiple">
                    <div class="multiple-checkboxes">
                        <input data-name='isLab' type="checkbox" id="isLabCheckBox${indx}"/>
                    </div> 
                </div>
            </div>

            <div class="fields">
                <label class="fields-items">Course Code (<span class="required">*</span>):</label>
                <input data-name='courseCode' class="fields-items" type="text" placeholder="eg. CMPT 243" id="courseCodeText${indx}"/>
            </div>

            <div class="fields">
                <label class="fields-items">Course Name (<span class="required">*</span>):</label>
                <input data-name='courseName' class="fields-items" type="text" placeholder="eg. Algorithms and Data Structures" id="courseNameText${indx}"/>
            </div>

            <div>
                <img class="icon" src="icon/delete.svg" alt="Delete Course" id='delete_${indx}' onclick="removeCourseField(${indx})"/>
            </div>

        </fieldset>`
    );
    
}


export function addCourseLayoutToDOM() {
    return (
        `
        <header>
            <h1 class="title">Courses</h1>
        </header>
        
        <div class="container">
            <div class="fields">
                <label class="fields-items" for="facultyName">Faculty Name (<span class="required">*</span>):</label>
                <input data-name='facultyName' class="fields-items" type="text" id="facultyName" placeholder="eg. Marina">
            </div>

            <form id="courseForm">

            </form>

            <div>
                <img class="icon" src="icon/add_box.svg" alt="Add Course" id="addBtn"/>
            </div>

            <div class="btn-div">
                <a class="next-btn" id="nextBtn">
                    Next
                </a>
            </div>

            
        </div>
        `
    );
}


