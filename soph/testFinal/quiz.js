function validateForm() {
    console.log("function called");
    var questions = ["q1","q2","q3","q4","q5","q6","q7",'q8','q9','q10']; //  MAKE SURE YOU UPDATE EVERY TIME YOU ADD A QUESTION
    var answered = 0;
    
    var q;
    for (q in questions){
        var radios = document.getElementsByName(questions[q]);
        var i = 0;
        while (i < 4) {   //  DO NOT CHANGE 
            if (radios[i].checked) {
                answered++;
            }
            i++;       
            console.log(i);
        }
    }
    if (answered !== 10) {    //  MAKE SURE YOU UPDATE EVERY TIME YOU ADD A QUESTION
        var submit = confirm("You missed " + (10 - answered).toString() + " questions. Are you sure you want to submit?");
        if (submit){
            return true;
        }
        else {
            return false;
        }
    }
}  // Code "inspired" by MatuDuke's answer to a question on stack overflow 

