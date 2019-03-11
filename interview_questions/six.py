const logInfo = (arr) => {
  arr.forEach(item => {
    if (parseInt(item) % 4 === 0) {
      console.log('divisible by 4')
    } else if (parseInt(item) % 2 === 0) {
      console.log('divisible by 2')
    } else if (String(item).charAt(0) === '5') {
      console.log('starts with 5')
    }
  });
};

logInfo([20, 13843, 271, 15, 4032, 6188, 60105]);