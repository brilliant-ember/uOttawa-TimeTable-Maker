'use strict';

//
// This function takes an array of format [[courseName, courseData], ...]
// and returns an array of all possible valid course timetables
//
var TableBuilder = function(data){

    //
    // lookup for day offset
    //
    const offset = {
        'mon': 0,
        'tue': 9,
        'wed': 18,
        'thu': 27,
        'fri': 36
    };

    //
    // list of courses, n long, each element will be all possible time arrangements for course i
    //
    let course_tables = [];
    data.forEach((v, i) => {
        course_tables.push([]);
    });

    data.forEach((course, c) => {
        const courseName = course[0];
        course = course[1];

        for(let section in course){
            //
            // collect LEC, LAB, DGD, and TUT
            //

            //
            // LEC
            //
            let lec_list = [];
            course[section]["LEC"].forEach((lec, l) => {
                lec["periods"].forEach((period, p) => {
                    const metadata = {
                        'courseName': courseName,
                        'section': section,
                        'period': period,
                        'day': lec["day"],
                        'starttime': lec['starttime'],
                        'endtime': lec['endtime'],
                        'location': lec['location'],
                        'prof': lec['prof'],
                        'type': "LEC",
                        'id': undefined // ex. lab/tut/dgd identifier
                    };
                    lec_list.push( [parseInt(period, 10) + offset[lec["day"]], metadata ] );

                });
            });

            //
            // LAB
            //
            let lab_list = []; // ensure least one element so loops work below
            if( course[section].hasOwnProperty("LAB") ){
                for(let lab in course[section]["LAB"]){
                    const labNumber = lab;
                    lab = course[section]["LAB"][lab];

                    let temp = [];
                    for(let period in lab["periods"]){
                        let p = lab["periods"][period]
                        const metadata = {
                            'courseName': courseName,
                            'section': section,
                            'period': p,
                            'day': lab["day"],
                            'starttime': lab['starttime'],
                            'endtime': lab['endtime'],
                            'location': lab['location'],
                            'prof': lab['prof'],
                            'type': "LAB",
                            'id': labNumber
                        };
                        temp.push( [parseInt(p, 10) + offset[lab["day"]], metadata] );
                    }
                    lab_list.push(temp);
                }
            }

            //
            // DGD
            //
            let dgd_list = [];
            if( course[section].hasOwnProperty("DGD") ){
                for(let dgd in course[section]["DGD"]){
                    const dgdNumber = dgd;
                    dgd = course[section]["DGD"][dgd];

                    let temp = [];
                    for(let period in dgd["periods"]){
                        let p = dgd["periods"][period]
                        const metadata = {
                            'courseName': courseName,
                            'section': section,
                            'period': p,
                            'day': dgd["day"],
                            'starttime': dgd['starttime'],
                            'endtime': dgd['endtime'],
                            'location': dgd['location'],
                            'prof': dgd['prof'],
                            'type': "DGD",
                            'id': dgdNumber
                        };
                        temp.push( [parseInt(p, 10) + offset[dgd["day"]], metadata] );
                    }
                    dgd_list.push(temp);

                }
            }

            //
            // TUT
            //
            let tut_list = [];
            if( course[section].hasOwnProperty("TUT") ){
                for(let tut in course[section]["TUT"]){
                    const tutNumber = tut;
                    tut = course[section]["TUT"][tut];

                    let temp = [];
                    for(let period in tut["periods"]){
                        let p = tut["periods"][period]
                        const metadata = {
                            'courseName': courseName,
                            'section': section,
                            'period': p,
                            'day': tut["day"],
                            'starttime': tut['starttime'],
                            'endtime': tut['endtime'],
                            'location': tut['location'],
                            'prof': tut['prof'],
                            'type': "TUT",
                            'id': tutNumber
                        };
                        temp.push( [parseInt(p, 10) + offset[tut["day"]], metadata] );
                    }
                    tut_list.push(temp);

                }
            }

            //
            // ensure all arrays have at least one element
            //
            if(lab_list.length == 0){ lab_list.push(false) }
            if(dgd_list.length == 0){ dgd_list.push(false) }
            if(tut_list.length == 0){ tut_list.push(false) }

            //
            // make all possible combinations of LEC + other for this section
            //
            let combos = [];
            lab_list.forEach((a) => {
                dgd_list.forEach((b) => {
                    tut_list.forEach((c) => {

                        let temp = lec_list.slice();
                        if(lab_list.indexOf(false) == -1){ temp = temp.concat(a) }
                        if(dgd_list.indexOf(false) == -1){ temp = temp.concat(b) }
                        if(tut_list.indexOf(false) == -1){ temp = temp.concat(c) }
                        combos.push( temp );

                    });
                });
            });

            //
            // save this batch of possible course timetables
            // (course_tables is a n course list of all course combos)
            //
            course_tables[c] = course_tables[c].concat(combos);

        } // course ends
    }); // data ends

    //
    // pick one valid time set from each course
    //
    let index = [];
    course_tables.forEach((v, i) => {
        index.push( 0 );
    });

    //
    // add all timetables to array
    //
    let possible = [];
    do{
        let temp = [];
        for(let i in index){
            temp = temp.concat( course_tables[i][ index[i] ] );
        }
        possible.push(temp.slice());
    }while( (index = next(index)) != false );

    //
    // returns next index solution, or false
    //
    function next(index){
        for(let i = index.length-1; i>=0; i--){

            // cannot increment further
            if(i == 0 && index[i] == course_tables[i].length-1){
                return false;
            }

            // reached max for current index
            if(index[i] == course_tables[i].length-1){
                index[i] = 0;

            // increment by one and return
            }else{
                index[i] += 1;
                return index;
            }
        }
    }

    //
    // filter out invalid schedules
    //
    let valid_tables = possible.filter((timetable) => valid(timetable));

    function valid(timetable){ // true if timetable has no duplicates
        timetable = timetable.sort((a, b) => parseInt(a[0], 10) - parseInt(b[0], 10));
        for(let i=0; i<timetable.length-1; i++){
            if(timetable[i][0] == timetable[i+1][0]){
                return false;
            }
        }
        return true;
    }

    return valid_tables;

};
