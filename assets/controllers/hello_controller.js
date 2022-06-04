import { Controller } from '@hotwired/stimulus';

/*
 * This is an example Stimulus controller!
 *
 * Any element with a data-controller="hello" attribute will cause
 * this controller to be executed. The name "hello" comes from the filename:
 * hello_controller.js -> "hello"
 *
 * Delete this file or adapt it for your use!
 */
export default class extends Controller {
    connect() {
        this.element.textContent = 'Hello Stimulus! Edit me in assets/controllers/hello_controller.js';
        //https://content-sheets.googleapis.com/v4/spreadsheets/1vUJektC3SB15tTF1rYKPmsAIzxVoHidl1wpNB18gQdc?includeGridData=true&key=AIzaSyAa8yy0GdcGPHdtD083HiGGx_S0vMPScDM
    }
}
