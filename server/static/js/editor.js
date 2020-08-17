class Editor {
    constructor(count) {
        this.count = count;
        this.comp();
        this.isCompetition = false;
        document.addEventListener('DOMContentLoaded', () => {
            this.logKeys();
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
                this.count++;
                if(this.count >= 5) {
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

        let compButton = document.createElement("button");
        compButton.appendChild(document.createTextNode("Comp"));

        menu.parentNode.insertBefore(compButton, menu)

   

    }


}

let editor = new Editor(0);



