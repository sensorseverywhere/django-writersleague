class CompetitionEditor {
    constructor(wordCount) {
        this.wordCount = wordCount;
        this.isCompetition = false;
        this.cdt = {};
        document.addEventListener('DOMContentLoaded', () => {
            this.comp();
        });
    }

    logKeys() {
        // listen for keystrokes in editor
        document.getElementById('martor-content').addEventListener("keypress", (e) => {
            let keyCode = e.hasOwnProperty('which') ? e.which : e.keyCode;
            // working on regexp
            let regexp = new RegExp("(?:^|\\s)").test();
            if(keyCode === 32) {
                // add number of spaces to a count
                this.wordCount++;
                if(this.wordCount >= 0 && this.wordCount <= 1000) {
                    // if the number of spaces >= 500, disable the editor
                    document.getElementById('word-count').innerHTML = this.wordCount;
                    // this.disableElement();
                }
            }
        });
    }

    disableElement() {
        document.querySelector('.ace_text-input').setAttribute('disabled', 'disabled');
    }

    comp() {

        let el = document.querySelector('.martor-toolbar');
        let menu = el.childNodes[0].nextSibling;

        let compButton = document.createElement("div");
        compButton.classList.add("btn");
        compButton.classList.add("btn-comp");
        compButton.appendChild(document.createTextNode("Comp"));

        menu.parentNode.insertBefore(compButton, menu);

        compButton.addEventListener("click", (e) => {
            e.stopPropagation();
            this.isCompetition ? this.isCompetition == false : this.isCompetition == true;
            if(this.isCompetition == false) {
                this.isCompetition = true;
                document.getElementById('competition-topbar').style.display = "block";
                this.logKeys();
                this.cdt = new CountDownTimer(20);
                 document.getElementById('word-count').innerHTML = this.wordCount;
            } else {
                this.isCompetition = false;
                document.getElementById('competition-topbar').style.display = "none";
                this.cdt.stopTimer();
              }
        });
    }
}



class CountDownTimer {

    constructor(startTime) {
        this.timeRemaining = startTime
        this.seconds = 0;
        this.minutes = 0;
        this.hours = 0;
        this.days = 0;
        this.timer = {};
        this.initialiseClock();
    }

    initialiseClock() {
        this.timer = setInterval(() => {
            // timeRemaining is the seconds counter
            this.timeRemaining -= 1;
            // log hours, minutes, seconds 
            this.seconds = this.timeRemaining % 60;
            this.minutes = Math.floor(this.timeRemaining / 60);
            this.hours = Math.floor(this.timeRemaining / 3600);
            this.days = Math.floor((this.timeRemaining / 3600) / 24);

            document.getElementById('days').innerHTML = this.days;
            document.getElementById('hours').innerHTML = this.hours;
            document.getElementById('minutes').innerHTML = this.minutes;
            document.getElementById('seconds').innerHTML = this.seconds;
 
            
            if(this.timeRemaining == 0) {
                this.stopTimer(this.timer)
            }
        }, 1000)
    }

    stopTimer() {
        clearInterval(this.timer);
        console.log('KaBoom!')
    }
 }


let editor = new CompetitionEditor(0);



