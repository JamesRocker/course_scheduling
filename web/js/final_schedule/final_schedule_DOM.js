export function calendarDOM(name) {

    return (
        `
        <div id="${name}_schedule">
            <table>
                <thead>
                    <tr>
                        <th colspan="6">${name}</th>
                    </tr>
                    <tr>
                        <th></th>
                        <th>M</th>
                        <th>T</th>
                        <th>W</th>
                        <th>R</th>
                        <th>F</th>
                    </tr>
                </thead>
                <tbody id="${name}_tbody">
                </tbody>
            </table>
        </div>
        `
    );
}


export function timeSlotsDOM (name, time) {
    return (
        `
        <tr>
            <th>${time}</th>
            <td id="${name}_day_M_time_${time}" style="background-color: white;"></td>
            <td id="${name}_day_T_time_${time}" style="background-color: white;"></td>
            <td id="${name}_day_W_time_${time}" style="background-color: white;"></td>
            <td id="${name}_day_R_time_${time}" style="background-color: white;"></td>
            <td id="${name}_day_F_time_${time}" style="background-color: white;"></td>
        </tr>
        `
    );
}

export function nameLinkDOM(name) {
    return (
        `
        <li>
            <a href="#${name}_schedule">${name}</a>
        </li>
        `
    );
}