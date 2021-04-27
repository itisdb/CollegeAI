// creating an array and passing the number, questions, options, and answers
let questions = [{
  question: "Which one is your main focus while choosing your college ?",
  numb: 1,
  options: [{
    answer: "Placement",
    weights: {
      academic: 0,
      placement: 1,
      infrastructure: 0
    }
  },
  {
    answer: "Academic",
    weights:{
      academic: 1,
      placement: 0,
      infrastructure: 0
    }
  },
  {
    answer: "Infrastructure",
    weights:{
      academic: 0,
      placement: 0,
      infrastructure: 1
    }
  }]
},
{
  question: "Would you like to go for higher studies ?",
  numb: 2,
  options: [{
    answer: "Yes",
    weights: {
      academic: 0.5,
      placement: 0.25,
      infrastructure: 0.25
    }
  },
  {
    answer: "No",
    weights: {
      academic: 0.33,
      placement: 0.33,
      infrastructure: 0.33
    }
  }]
},
{
  question: "Would you like to go for entrepreneurship activities ?",
  numb: 3,
  options: [{
    answer: "Yes",
    weights: {
      academic: 0.25,
      placement: 0.25,
      infrastructure: 0.5,
    }
  },
  {
  answer: "No",
  weights: {
    academic: 0.33,
    placement: 0.33,
    infrastructure: 0.33
  }
}]
},
{
  question: "What is your dream college hostel life ?",
  numb: 4,
  options: [{
    answer: "Clean rooms with proper food is must.",
    weights: {
      academic: 0.125,
      placement: 0.125,
      infrastructure: 0.75
    }
  },
{
  answer: "Does not matter that much as long as academics are good.",
  weights: {
    academic: 0.75,
    placement: 0.125,
    infrastructure: 0.125
  }
},
{
  answer: "My main motivation is placement so I will adjust to anything.",
  weights: {
    academic: 0.125,
    placement: 0.75,
    infrastructure: 0.125
  }
}]
},
{
  question: "What is your dream college sports life ?",
  numb: 5,
    options: [{
    answer: "Good sports facilities is must.",
    weights: {
      academic: 0.125,
      placement: 0.125,
      infrastructure: 0.75
    }
  },
{
  answer: "Does not matter that much as long as academics are good.",
  weights: {
    academic: 0.75,
    placement: 0.125,
    infrastructure: 0.125
  }
},
{
  answer: "My main motivation is placement so I will adjust to anything.",
  weights: {
    academic: 0.125,
    placement: 0.75,
    infrastructure: 0.125
  }
}]
}];

// let questions1 = [
//     {
//     numb: 1,
//     question: "What does HTML stand for?",
//     answer: "Hyper Text Markup Language",
//     options: [
//       "Hyper Text Preprocessor",
//       "Hyper Text Markup Language",
//       "Hyper Text Multiple Language",
//       "Hyper Tool Multi Language"
//     ]
//   },
//     {
//     numb: 2,
//     question: "What does CSS stand for?",
//     answer: "Cascading Style Sheet",
//     options: [
//       "Common Style Sheet",
//       "Cascading Style Sheet"
//     ]
//   },
//     {
//     numb: 3,
//     question: "What does PHP stand for?",
//     answer: "Hypertext Preprocessor",
//     options: [
//       "Hypertext Preprocessor",
//       "Hypertext Programming",
//       "Hypertext Preprogramming",
//       "Hometext Preprocessor"
//     ]
//   },
//     {
//     numb: 4,
//     question: "What does SQL stand for?",
//     answer: "Structured Query Language",
//     options: [
//       "Stylish Question Language",
//       "Stylesheet Query Language",
//       "Statement Question Language",
//       "Structured Query Language"
//     ]
//   },
//     {
//     numb: 5,
//     question: "What does XML stand for?",
//     answer: "eXtensible Markup Language",
//     options: [
//       "eXtensible Markup Language",
//       "eXecutable Multiple Language",
//       "eXTra Multi-Program Language",
//       "eXamine Multiple Language"
//     ]
//   },
//   // you can uncomment the below codes and make duplicate as more as you want to add question
//   // but remember you need to give the numb value serialize like 1,2,3,5,6,7,8,9.....

//   //   {
//   //   numb: 6,
//   //   question: "Your Question is Here",
//   //   answer: "Correct answer of the question is here",
//   //   options: [
//   //     "Option 1",
//   //     "option 2",
//   //     "option 3",
//   //     "option 4"
//   //   ]
//   // },
// ];
