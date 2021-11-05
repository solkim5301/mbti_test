$(document).ready(function () {
    quizData();
});

function quizData() {
    $.ajax({
        type: "GET",
        url: "/quizdata",
        data: {},
        success: function (response) {
            let quiz = response['all_quiz']
            for (let i = 0; i < quiz.length; i++) {
                let question = quiz[i]['question']
                let answer1 = quiz[i]['answer1']
                let answer2 = quiz[i]['answer2']

                let temp_html = `<h1 class="intro-title">question</h1>
                                <h5 class="main-text">${question}</h5>
                                <button class="main-btn red-font" type="button">${answer1}</button>
                                <button class="main-btn red-font" type="button">${answer2}</button>`
                $('#sample').append(temp_html)
            }
        }
    })
}
