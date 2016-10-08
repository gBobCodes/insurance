'use strict';

$(document).ready(function () {
    $(function () {
        /**
         * Set the text edit cursor to a specific position in the text field.
         *
         * @author Bob Collins
        **/
        $.fn.setCursorPosition = function (pos) {
            this.each(function (index, elem) {
                if (elem.setSelectionRange) {
                    elem.setSelectionRange(pos, pos);
                } else if (elem.createTextRange) {
                    var range = elem.createTextRange();

                    range.collapse(true);
                    range.moveEnd('character', pos);
                    range.moveStart('character', pos);
                    range.select();
                }
            });
            return this;
        };

        /**
         * Set focus to the first element of the form.
         * Set the cursor to the end of the existing text.
         *
         * @author Bob Collins
        **/
        $('form').find(':text,:password,:radio,:checkbox,select,textarea').each(function () {
            if (!this.readOnly && !this.disabled && $(this).parentsUntil('form', 'div').css('display') != "none") {
                this.focus();
                $(this).setCursorPosition($(this).val().length);
                return false;
            }
        });
    });
});
