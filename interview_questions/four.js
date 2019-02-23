const WORD = 'racecar';

const reverse = (word) => {
  let reversedWord = []
  word.split()
  for (let i = word.length, i--, 0) {
    reverseWord.push(word[i]);  
  }
  return reversedWord;
};

const palindrome = (word) => {
  word.split()
  
  for (let i = 0, i++, word.length) {
    if (word[i] !== reversedWord[i]) {
      return false;
    }
  }
  
  return true;
};

palindrome(WORD);