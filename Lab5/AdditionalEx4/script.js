const questions = [
    {
      question: "What is the capital of France?",
      answers: [
        { text: "Paris", correct: true },
        { text: "London", correct: false },
        { text: "Berlin", correct: false },
        { text: "Madrid", correct: false }
      ]
    },
    {
      question: "Which language is used for web apps?",
      answers: [
        { text: "Python", correct: false },
        { text: "JavaScript", correct: true },
        { text: "C++", correct: false },
        { text: "Java", correct: false }
      ]
    },
    {
      question: "What does HTML stand for?",
      answers: [
        { text: "HyperText Markup Language", correct: true },
        { text: "HighText Machine Language", correct: false },
        { text: "HyperTransfer Machine Language", correct: false },
        { text: "None of the above", correct: false }
      ]
    }
  ];
  
  let currentQuestion = 0;
  let score = 0;
  
  const questionEl = document.getElementById("question");
  const answersEl = document.getElementById("answers");
  const nextBtn = document.getElementById("nextBtn");
  const scoreContainer = document.getElementById("score-container");
  const scoreEl = document.getElementById("score");
  
  function startQuiz() {
    showQuestion();
  }
  
  function showQuestion() {
    const q = questions[currentQuestion];
    questionEl.textContent = q.question;
    answersEl.innerHTML = "";
  
    q.answers.forEach(answer => {
      const btn = document.createElement("button");
      btn.textContent = answer.text;
      btn.classList.add("answer");
      btn.onclick = () => {
        if (answer.correct) score++;
        nextBtn.style.display = "inline-block";
        document.querySelectorAll(".answer").forEach(b => (b.disabled = true));
      };
      answersEl.appendChild(btn);
    });
  }
  
  nextBtn.onclick = () => {
    currentQuestion++;
    if (currentQuestion < questions.length) {
      showQuestion();
      nextBtn.style.display = "none";
    } else {
      document.getElementById("question-container").classList.add("hide");
      scoreContainer.classList.remove("hide");
      scoreEl.textContent = score + "/" + questions.length;
    }
  };
  
  startQuiz();
  