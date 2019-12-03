(function() {
  var questions = [
  {
    question: `Which of the following correctly declares an array?`,
    choices: [ 'int array[];', 'int[] array;', 'int array;','int array[10];'],
    correctAnswer: 3
  },
  {
    question: `
    <p>What is the output of following program?</p>
    <pre><code>
    #include <iostream> 
    using namespace std; 
    int main() 
    { 
        int i, j, k; 
        int sum[2][4]; 
        for (i = 0; i < 2; i++) { 
            for (j = 0; j < 3; j++) 
                sum[i][j] = i+j; 
        } 
        cout << sum[--i][--j] << endl; 
        cout << sum[++i][++j];
        return 0; 
    }
    </code></pre>`,
    choices: [ '6 0', '6 Garbage value', '3 Garbage value','3 5'],
    correctAnswer: 2
  },
  {
    question: `
    <p>What is the output of the following program?</p>
    <pre><code>
    #include <iostream> 
    #include <cstring> 
    using namespace std; 
    int main () 
    { 
      char string[50] = "hello"; 
      memset (string, '*', 3); 
      cout << string; 
      return 0; 
    }
    </code></pre>`,
    choices: [ 'hellohellohello', '***lo', 'hello*3','Error'],
    correctAnswer: 1
  },
  {
    question: `
    <p>In C++, Which of the following expressions will return the value 16.</p>`,
    choices: [ '4^2', '2**4', '256^^0.5','None of the above'],
    correctAnswer: 3
  },
  {
    question: `
    <p>What is the output of the following program?</p>
    <pre><code>
    #include<iostream>
    using namespace std;
    main() { 
       int x = 35%10+5*5-100/5;
       if(x>=5) { 
          if(x!=10);
            cout<<10;
          if(x==10)
            cout<<0; 
        }
    }
    </code></pre>`,
    choices: [ '0', '10', '100','Compile error'],
    correctAnswer: 2
  },
  {
    question: `
    <pre><code>int *A[10], B[10][10];</code></pre>
    <p>Which of the following expressions will not give compile-time errors?</p>
    <pre><code>
    I. A[2]
    II. A[2][3]
    III. B[1]
    IV. B[2][3]
    </code></pre>`,
    choices: [ 'I, II, and IV only', 'II, III, and IV only', 'II and IV only','IV only'],
    correctAnswer: 0
  },
  {
    question: `
    <p>A variable is defined within a block in a body of a function. Which of the following is true ?</p>`,
    choices: [ 'It is visible from the point of definition to the end of the program.', 'It is visible throughout the function.', 'It is visible throughout the block.','It is visible from the point of definition to the end of the block.'],
    correctAnswer: 2
  },
  {
    question: `
    <p>Which operator is used to define a member of a class from outside the class definition ?</p>`,
    choices: [ '->', '>>', '.','::'],
    correctAnswer: 3
  },
  {
    question: `
    <p>What will be the output of the following C++ code?</p>
    <pre><code>
    #include <iostream>
    using namespace std;
    void copy (int& a, int& b, int c)
    {
        a *= 2;
        b *= 2;
        c *= 2;
    }
    int main ()
    {
        int x = 1, y = 3, z = 7;
        copy (x, y, z);
        cout << x << " " << y << " " << z;
        return 0;
    }
    </code></pre>`,
    choices: [ '1 3 7', '2 6 14', '2 6 7','1 3 14'],
    correctAnswer: 2
  }, 
  {
    question: `
    <p>What will be the output of the following C++ code?</p>
    <pre><code>
    #include<iostream>
    using namespace std;
    class Test
    {
       private:
         static int count;
       public:
         Test& fun(); 
    };
    int Test::count = 0;
    Test& Test::fun()
    {
        Test::count++;
        cout << Test::count << " ";
        return *this;
    }
    int main()
    {
        Test t;
        t.fun().fun().fun().fun();
        return 0;
    }
    </code></pre>`,
    choices: [ '4 4 4 4', '1 2 3 4', '1 1 1 1','0 1 2 3'],
    correctAnswer: 1
  }, 
  {
    question: `
    <p>What will happen in the following C++ code snippet?</p>
    <pre><code>
    int a = 100, b = 200;
    int *p = &a, *q = &b;
    p = q;
    </code></pre>`,
    choices: [ 'b is assigned to a', 'p now points to b', 'a is assigned to b','q now points to a'],
    correctAnswer: 1
  },
  {
    question: `
    <p>What is the output of the following program?</p>
    <pre><code>
    #include<iostream>
    using namespace std;
    class Base {
    public:
       void f() {
          cout<<"Base";
       }
    };

    class Derived:public Base {
    public:
       void f() {
          cout<<"Derived";
       }
    };
    main() {
       Base *p = new Derived();    
       p->f();
    }
    </code></pre>`,
    choices: [ 'Base', 'Derived', 'Compile error','None of the above'],
    correctAnswer: 0
  },
  {
    question: `
    <p>Comment on the 2 arrays regarding P and Q:</p>
    <pre><code>
    int *a1[8];
    int *(a3[8]);
    </code></pre>
    <p>P. Array of pointers</p>
    <p>Q. Pointer to an array</p>`,
    choices: [ 'a1 is P, a2 is Q', 'a1 is P, a2 is P', 'a1 is Q, a2 is P','a1 is Q, a2 is Q'],
    correctAnswer: 1
  },
  {
    question: `
    <p>What will be the output of the following C++ code?</p>
    <pre><code>
    #include <iostream>
    #include <vector>
    using namespace std;
    int main ()
    {
        vector<int> myvector(5);
        int* p = myvector.data();
        *p = 10;
        ++p;
        *p = 20;
        p[2] = 100;
        for (unsigned i = 0; i < myvector.size(); ++i)
            cout << ' ' << myvector[i];
    }`,
    choices: [ '10 20', '10 20 0', '10 20 0 100','10 20 0 100 0'],
    correctAnswer: 3
  },
  {
    question: `
    <p>How structures and classes in C++ differ?</p>`,
    choices: [ 'In Structures, members are public by default whereas, in Classes, they are private by default', 'In Structures, members are private by default whereas, in Classes, they are public by default', 'Structures by default hide every member whereas classes do not','Structures cannot have private members whereas classes can have'],
    correctAnswer: 0
  },
  ];
  
  
  var questionCounter = 0; //Tracks question number
  var selections = []; //Array containing user choices
  var quiz = $('#quiz'); //Quiz div object
  
  // Display initial question
  displayNext();
  // Click handler for the 'next' button
  // $('#next').on('click', function (e) {
    var a=0; 
    var i=0;
  $('#next').click(function (e) {
    a=0;
    e.preventDefault();
    
    // Suspend click listener during fade animation
    if(quiz.is(':animated')) {        
      return false;
    }
    choose();
    
    // If no user selection, progress is stopped
    if (isNaN(selections[questionCounter])) {
      alert('Please make a selection!');
    } else {
      var ca = questions[i].correctAnswer;
      // selections[i] === questions[i].correctAnswer ? a=1 :a=0
      if (selections[i] === questions[i].correctAnswer) {
        a=1
      }
      else {
        a=0;
      }
      i++;

      $.ajax({
	      type:'POST',
          url: 'foo',
          data:{answer:a, canswer:ca},
	    });
       
      //alert('outside if loop');
      questionCounter++;
      displayNext();
    }
    

//
    // $.ajax({
    // 	type:'POST',
    // 	url: "{{ url_for('foo')}}",
    // 	dataType: "text",
    // 	success: function(response){
    // 		alert(response);
    // 	}
    // })
//

  });
  
  // Click handler for the 'prev' button
  $('#prev').on('click', function (e) {
    e.preventDefault();
    
    if(quiz.is(':animated')) {
      return false;
    }
    choose();
    questionCounter--;
    displayNext();
  });
  
  // Click handler for the 'Start Over' button
  $('#start').on('click', function (e) {
    e.preventDefault();
    
    if(quiz.is(':animated')) {
      return false;
    }
    questionCounter = 0;
    selections = [];
    displayNext();
    i=0;
    $('#start').hide();
  });
  
  // Animates buttons on hover
  $('.button').on('mouseenter', function () {
    $(this).addClass('active');
  });
  $('.button').on('mouseleave', function () {
    $(this).removeClass('active');
  });
  
  // Creates and returns the div that contains the questions and 
  // the answer selections
  function createQuestionElement(index) {
    var qElement = $('<div>', {
      id: 'question'
    });
    
    var header = $('<h4>Question ' + (index + 1) + ':</h4>');
    qElement.append(header);
    
    var question = $('<p>').append(questions[index].question);
    qElement.append(question);
    
    var radioButtons = createRadios(index);
    qElement.append(radioButtons);
    
    return qElement;
  }
  
  // Creates a list of the answer choices as radio inputs
  function createRadios(index) {
    var radioList = $('<ul>');
    var item;
    var input = '';
    for (var i = 0; i < 4; i++) {
      item = $('<li>');
      input = '<input type="radio" name="answer" value=' + i + ' />';
      input += questions[index].choices[i];
      item.append(input);
      radioList.append(item);
    }
    return radioList;
  }
  
  // Reads the user selection and pushes the value to an array
  function choose() {
    selections[questionCounter] = +$('input[name="answer"]:checked').val();
  }
  
  // Displays next requested element
  function displayNext() {
    quiz.fadeOut(function() {
      $('#question').remove();
      
      if(questionCounter < questions.length){
        var nextQuestion = createQuestionElement(questionCounter);
        quiz.append(nextQuestion).fadeIn();
        if (!(isNaN(selections[questionCounter]))) {
          $('input[value='+selections[questionCounter]+']').prop('checked', true);
        }
        
        // Controls display of 'prev' button
        if(questionCounter === 1){
          $('#prev').show();
        } else if(questionCounter === 0){
          
          $('#prev').hide();
          $('#next').show();
        }
      }else {
        var scoreElem = displayScore();
        quiz.append(scoreElem).fadeIn();
        $('#next').hide();
        $('#prev').hide();
        $('#start').show();
      }
    });
  }
  
  function answersend(){
    var a=0;
    var i=0;
    if (selections[i] === questions[i].correctAnswer) {
      a=1;
    }
    i++;
    return a
  }
  
  // Computes score and returns a paragraph element to be displayed
  function displayScore() {
    var score = $('<p>',{id: 'question'}); 
    var numCorrect = 0;
    for (var i = 0; i < selections.length; i++) {
      if (selections[i] === questions[i].correctAnswer) {
        numCorrect++;
      }
    }
    
    score.append('You got ' + numCorrect + ' questions out of ' +
                 questions.length + ' right!!!');
    return score;
  }
})();