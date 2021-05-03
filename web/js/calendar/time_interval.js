import {timeBlocks} from './all_time_blocks.js';

export const timeIntervals = [
    "08:30",
    "09:00",
    "09:30",
    "10:00",
    "10:30",
    "11:00",
    "11:30",
    "12:00",
    "12:30",
    "13:00",
    "13:30",
    "14:00",
    "14:30",
    "15:00",
    "15:30",
    "16:00",
    "16:30",
    "17:00",
    "17:30",
    "18:00",
    "18:30",
    "19:00",
    "19:30",
    "20:00",
    "20:30",
    "21:00",
    "21:30"
];


// eg. 0 -> ["08:30", "09:00"]
// 0 -> time id that starts from 8:30 and ends at 9:00

export let timeObj = {};

for (let count=0; count < timeIntervals.length - 1; count ++) {
    timeObj[count] = [timeIntervals[count], timeIntervals[count+1]];
}


// const classBlocks = [
//     {
//         num: 1,
//         timeFrom: "08:30",
//         timeTo: "09:00",
//         day: ['M', 'W']
//     },
//     {
//         num: 2,
//         timeFrom: "09:00",
//         timeTo: "09:30",
//         day: ['M']
//     }
// ]




class TimeBlock {
    constructor({numArr, timeFrom, timeTo, dayArr, code}) {
        this.numArr = numArr;
        
        this.timeFrom = timeFrom;
        this.timeTo = timeTo;
        this.dayArr = dayArr;
        this.code = code;

        this.available = true;
        this.selected = false;
        this.priority = 1;

        // this.backgroundColor = "white";
        
    }

    setSelected(status) {
        this.selected = status;
    }

    toggleAvailability() {
        this.available = !this.available;
    }

}


export let allTimeBlocksObj = {};
for (let timeBlock of timeBlocks) {
    let timeBlockObj = new TimeBlock(timeBlock);
    allTimeBlocksObj[timeBlockObj.code] = timeBlockObj;
}

