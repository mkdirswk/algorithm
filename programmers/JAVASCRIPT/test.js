var day = ["FRI","SAT","SUN","MON","TUE","WED","THU"];
var daynumInMonth = [31,29,31,30,31,30,31,31,30,31,30,31];

var a = 1
var b = 7
function solution(a, b) {
    var totalday = 0;

    for(var x = 0; x < a - 1; x++){
        totalday += daynumInMonth[x];
    }
    
    totalday += b;
    var answer = (totalday % 7) - 1
    if (answer == -1){
        answer = 6;
    }
    return day[answer];
}

console.log(solution(a,b))