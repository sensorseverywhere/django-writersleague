class CompetitionEditor {
    constructor(wordCount) {
        this.wordCount = wordCount;
        this.isCompetition = false;
        document.addEventListener('DOMContentLoaded', () => {
            this.logKeys();
        });
        this.comp();
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
                if(this.wordCount >= 10 && this.wordCount <= 50) {
                    // if the number of spaces >= 500, disable the editor
                    this.disableElement();
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
            let timer = new CountDownTimer(3602);
            if(this.isCompetition == false) {
                this.isCompetition = true;
                if(this.isCompetition == true){
                    console.log('showing')
                    document.getElementById('competition-topbar').style.display = "block";
                    document.getElementById('word-count').innerHTML = this.wordCount;
                }
                
            } else {
                this.isCompetition = false;
                if(this.isCompetition == false){
                    console.log('hidden')
                    document.getElementById('competition-topbar').style.display = "none";
                    document.getElementById('word-count').innerHTML = this.wordCount;
                }
            }
            
        });

        
 

    }
}



class CountDownTimer {

    constructor(startTime) {
        this.startTime, this.timeRemaining = startTime
        this.seconds = 0;
        this.minutes = 0;
        this.hours = 0;
        this.days = 0;
        this.initialiseClock(startTime);
    }

    initialiseClock(startTime) {
        const timer = setInterval(() => {
            // timeRemaining is the seconds counter
            this.timeRemaining -= 1;
            // log hours, minutes, seconds 
            this.seconds = this.timeRemaining % 60;
            this.minutes = Math.floor(this.timeRemaining / 60);
            this.hours = Math.floor(this.timeRemaining / 3600);
            this.days = Math.floor((this.timeRemaining / 3600) / 24);
            // console.log(Math.floor(this.timeRemaining / 3600), Math.floor(this.timeRemaining / 60), this.timeRemaining % 60)

            if(this.timeRemaining == 0) {
                clearInterval(timer);
                console.log('Boom!')
            }
        }, 1000)
    } 
}


let editor = new CompetitionEditor(0);



