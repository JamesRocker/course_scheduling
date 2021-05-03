export const timeBlocks = [
    // for M,W,F
    {
        numArr: [1,2],
        timeFrom: "09:00",
        timeTo: "10:00",
        dayArr: ["M", "W", "F"],
        code: "A"
    },
    {
        numArr: [3,4],
        timeFrom: "10:00",
        timeTo: "11:00",
        dayArr: ["M", "W", "F"],
        code: "B"
    },
    {
        numArr: [5,6],
        timeFrom: "11:00",
        timeTo: "12:00",
        dayArr: ["M", "W", "F"],
        code: "C"
    },
    {
        numArr: [10,11],
        timeFrom: "13:30",
        timeTo: "14:30",
        dayArr: ["M", "W", "F"],
        code: "D"
    },
    {
        numArr: [12,13],
        timeFrom: "14:30",
        timeTo: "15:30",
        dayArr: ["M", "W", "F"],
        code: "E"
    },

    // for MW, WF, MF

    // G
    {
        numArr: [0,1,2],
        timeFrom: "08:30",
        timeTo: "10:00",
        dayArr: ["M", "W"],
        code: "G_1"
    },
    {
        numArr: [0,1,2],
        timeFrom: "08:30",
        timeTo: "10:00",
        dayArr: ["W", "F"],
        code: "G_2"
    },
    {
        numArr: [0,1,2],
        timeFrom: "08:30",
        timeTo: "10:00",
        dayArr: ["M", "F"],
        code: "G_3"
    },

    // H
    {
        numArr: [3,4,5],
        timeFrom: "10:00",
        timeTo: "11:30",
        dayArr: ["M", "W"],
        code: "H_1"
    },
    {
        numArr: [3,4,5],
        timeFrom: "10:00",
        timeTo: "11:30",
        dayArr: ["W", "F"],
        code: "H_2"
    },
    {
        numArr: [3,4,5],
        timeFrom: "10:00",
        timeTo: "11:30",
        dayArr: ["M", "F"],
        code: "H_3"
    },

    // I
    {
        numArr: [9,10,11],
        timeFrom: "13:00",
        timeTo: "14:30",
        dayArr: ["M", "W"],
        code: "I_1"
    },
    {
        numArr: [9,10,11],
        timeFrom: "13:00",
        timeTo: "14:30",
        dayArr: ["W", "F"],
        code: "I_2"
    },
    {
        numArr: [9,10,11],
        timeFrom: "13:00",
        timeTo: "14:30",
        dayArr: ["M", "F"],
        code: "I_3"
    },

    // J
    {
        numArr: [12,13,14],
        timeFrom: "14:30",
        timeTo: "16:00",
        dayArr: ["M", "W"],
        code: "J_1"
    },
    {
        numArr: [12,13,14],
        timeFrom: "14:30",
        timeTo: "16:00",
        dayArr: ["W", "F"],
        code: "J_2"
    },
    {
        numArr: [12,13,14],
        timeFrom: "14:30",
        timeTo: "16:00",
        dayArr: ["M", "F"],
        code: "J_3"
    },

    // JJ
    {
        numArr: [17],
        timeFrom: "17:00",
        timeTo: "17:30",
        dayArr: ["M", "F"],
        code: "JJ"
    },

    // K
    {
        numArr: [19,20,21],
        timeFrom: "18:00",
        timeTo: "19:30",
        dayArr: ["M", "W"],
        code: "K_1"
    },
    {
        numArr: [19,20,21],
        timeFrom: "18:00",
        timeTo: "19:30",
        dayArr: ["W", "F"],
        code: "K_2"
    },
    {
        numArr: [19,20,21],
        timeFrom: "18:00",
        timeTo: "19:30",
        dayArr: ["M", "F"],
        code: "K_3"
    },

    // for Tues, Thurs
    {
        numArr: [1,2,3],
        timeFrom: "09:00",
        timeTo: "10:30",
        dayArr: ["T", "R"],
        code: "L"
    },
    {
        numArr: [4,5,6],
        timeFrom: "10:30",
        timeTo: "12:00",
        dayArr: ["T", "R"],
        code: "M"
    },
    {
        numArr: [9,10,11],
        timeFrom: "13:00",
        timeTo: "14:30",
        dayArr: ["T", "R"],
        code: "N"
    },
    {
        numArr: [12,13,14],
        timeFrom: "14:30",
        timeTo: "16:00",
        dayArr: ["T", "R"],
        code: "O"
    },
    {
        numArr: [16,17],
        timeFrom: "16:30",
        timeTo: "17:30",
        dayArr: ["T", "R"],
        code: "P"
    },
    {
        numArr: [19,20,21],
        timeFrom: "18:00",
        timeTo: "19:30",
        dayArr: ["T", "R"],
        code: "Q"
    },
    {
        numArr: [22,23,24],
        timeFrom: "19:30",
        timeTo: "21:00",
        dayArr: ["T", "R"],
        code: "R"
    },

    // Labs

    // S
    {
        numArr: [16,17,18,19,20],
        timeFrom: "16:30",
        timeTo: "19:00",
        dayArr: ["M"],
        code: "S"
    },

    // T
    {
        numArr: [1,2,3,4,5,6],
        timeFrom: "09:00",
        timeTo: "12:00",
        dayArr: ["T"],
        code: "T"
    },

    // U
    {
        numArr: [12,13,14,15,16,17],
        timeFrom: "14:30",
        timeTo: "17:30",
        dayArr: ["T"],
        code: "U"
    },

    // X
    {
        numArr: [19,20,21,22,23,24],
        timeFrom: "18:00",
        timeTo: "21:00",
        dayArr: ["T"],
        code: "X"
    },

    // Y
    {
        numArr: [19,20,21,22,23,24],
        timeFrom: "18:00",
        timeTo: "21:00",
        dayArr: ["W"],
        code: "Y"
    },

    // Z
    {
        numArr: [1,2,3,4,5,6],
        timeFrom: "09:00",
        timeTo: "12:00",
        dayArr: ["R"],
        code: "Z"
    },

    // V
    {
        numArr: [12,13,14,15,16,17],
        timeFrom: "14:30",
        timeTo: "17:30",
        dayArr: ["R"],
        code: "V"
    },

    // AA
    {
        numArr: [19,20,21,22,23,24],
        timeFrom: "18:00",
        timeTo: "21:00",
        dayArr: ["R"],
        code: "AA"
    },

    // BB
    {
        numArr: [1,2,3,4,5,6],
        timeFrom: "09:00",
        timeTo: "12:00",
        dayArr: ["F"],
        code: "BB"
    },

    // W
    {
        numArr: [9,10,11,12,13,14],
        timeFrom: "13:00",
        timeTo: "16:00",
        dayArr: ["F"],
        code: "W"
    },

    // CC
    {
        numArr: [12,13,14,15,16,17],
        timeFrom: "14:30",
        timeTo: "17:30",
        dayArr: ["F"],
        code: "CC"
    },

]