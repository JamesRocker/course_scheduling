export function addCalendarLayoutToDOM() {
    return (
        `
        <header>
            <h1 class="title">Available Time</h1>
        </header>

        <div class="flex-container">

            <div class="flex-child">
                <table>
                    <thead>
                        <tr>
                            <th scope="col"></th>
                            <th scope="col">M</th>
                            <th scope="col">T</th>
                            <th scope="col">W</th>
                            <th scope="col">R</th>
                            <th scope="col">F</th>
                        </tr>
                    </thead>
                    <tbody id="calendarTBody">
                    
                    </tbody>
                </table>
            </div>
            
            <div class="flex-child">


                <div class="choices-label-container">
                    <p>Blocks</p>
                    <p>Priority</p>
                </div> 

                <div class="choices" id="choices">
                    
                </div>

                <div class="btn-div">
                    <a class="submit-btn" id="submitBtn">Submit</a>
                </div>

            </div>
            
        </div>
        
        `
    );
}


export function addTimeSlotsDOM (time) {
    return (
        `
        <tr>
            <th>${time}</th>
            <td id="day_M_time_${time}"></td>
            <td id="day_T_time_${time}"></td>
            <td id="day_W_time_${time}"></td>
            <td id="day_R_time_${time}"></td>
            <td id="day_F_time_${time}"></td>
        </tr>
        `
    );
}

export function addTimeChoicesDOM(timeBlock) {


    let dayStr = "";
    for (let day of timeBlock.dayArr) {
        dayStr += day;
    }

    return (
        `
        <div class="time-blocks" id='time_block_${timeBlock.code}'>
            <input class="time-blocks-child" type="checkbox" id='checkbox_${timeBlock.code}' onclick='updateAvailableTime("${timeBlock.code}")'>
            <label class="time-blocks-child" for='checkbox_${timeBlock.code}'>${timeBlock.code}: ${dayStr} ${timeBlock.timeFrom}-${timeBlock.timeTo}</label>
            <div class="time-blocks-child">
                <select id="selectbox_${timeBlock.code}" onchange='updatePriority("${timeBlock.code}")'>
                    <option value="1">1</option>
                    <option value="2">2</option>
                    <option value="3">3</option>
                </select>
            </div>
        </div>
        `
    )
}


export function disableEnableTimeBlockDOM(timeBlock, isDisabled) {

    
    // disable / enable checkbox
    toggleDisable(`checkbox_${timeBlock.code}`, isDisabled);

    // change class  so that div toggles between opaque and not opaque
    showHideClassName(`time_block_${timeBlock.code}`, 'overlapped', isDisabled); 

    // disable / enable selectbox
    toggleDisable(`selectbox_${timeBlock.code}`, isDisabled);

}

function toggleDisable(elementID, isDisabled) {
    let element = document.getElementById(elementID);
    // if (element.disabled) {
    //     element.disabled = false
    // }
    // else {
    //     element.disabled = true;
    // }

    if (isDisabled) {
        element.disabled = true;
    }
    else {
        element.disabled = false;
    }
    
}

function showHideClassName(elementID, className, isDisabled) {
    
    let element = document.getElementById(elementID);
    // if (element.classList.contains(className)) {
    //     element.classList.remove(className);
    // }
    // else {
    //     element.classList.add(className);
    // }
    if (isDisabled) {
        element.classList.add(className);
    }
    else {
        if (element.classList.contains(className)) {
            element.classList.remove(className);
        }
    }
    
}

/*** for showing or not showing time taken blocks on calendar  ***/
export function showHideBlocksOnCalendarDOM(timeBlock, timeObj) {
    let numArr = timeBlock.numArr;
    let dayArr = timeBlock.dayArr;

    // let backgroundColor = randomBackgroundColor();
    // timeBlock.backgroundColor = backgroundColor

    for (let day of dayArr) {
        for (let num of numArr) {
            const [startTime, endTime]= timeObj[num];

            if (timeBlock.selected) {

                let tdElement1 = document.getElementById(`day_${day}_time_${startTime}`);
                
                trackColoredSlots(tdElement1, timeBlock);
               
                
                tdElement1.classList.add('colored-slot');
                // tdElement1.style.backgroundColor = backgroundColor;


                let tdElement2 = document.getElementById(`day_${day}_time_${endTime}`);
                
                trackColoredSlots(tdElement2, timeBlock);
                tdElement2.classList.add('colored-slot');
                // tdElement2.style.backgroundColor = backgroundColor;
            }
            else {
                let tdElement1 = document.getElementById(`day_${day}_time_${startTime}`);

                delete tdElement1.dataset[`${timeBlock.code.toLowerCase()}`];
                
                if (Object.keys(tdElement1.dataset).length === 0) {
                    tdElement1.classList.remove('colored-slot');
                    // tdElement1.style.backgroundColor = 'white';
                }
              

                let tdElement2 = document.getElementById(`day_${day}_time_${endTime}`);
                
                delete tdElement2.dataset[`${timeBlock.code.toLowerCase()}`];
                
                if (Object.keys(tdElement2.dataset).length === 0) {
                    // tdElement2.style.backgroundColor = 'white';
                    tdElement2.classList.remove('colored-slot');
                }
            }

        }
    }
}


export function trackColoredSlots(element, timeBlock) {
    if (Object.keys(element.dataset).length === 0) {
        element.dataset[`${timeBlock.code.toLowerCase()}`]= true;
    }
    else {

        for (let key of Object.keys(element.dataset)) {
            if (key !== timeBlock.code.toLowerCase()) {
                element.dataset[`${timeBlock.code.toLowerCase()}`]= true;
            }

        }
    }
}


function randomBackgroundColor() {
    let rValue = Math.floor(Math.random() * 256);
    let gValue = Math.floor(Math.random() * 256);
    let bValue = Math.floor(Math.random() * 256);

    // for distinguishing text color and background color
    // let colorValue = Math.round(((rValue * 299) + (gValue * 587) + (bValue * 114)) / 1000);
    // let textColor;
    // if (colorValu)

    let backgroundColor = `rgb(${rValue}, ${gValue}, ${bValue})`;

    return backgroundColor;

}