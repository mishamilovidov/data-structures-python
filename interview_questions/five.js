// Create a function that flattens nested lists.

// For example, if you have the following list
//   a = [1, 2, [3, [4, 5]], 6]

// flatten (a) returns:
//  [1, 2, 3, 4, 5, 6]

const flatten = (data, arr) => {  
  data.forEach(item => {
    if (typeof item === 'object') {
      flatten(item, arr)
    } else {
      arr.push(item)
    }
  });
  
  return arr;
};

a = [1, 2, [3, [4, 5]], 6]
console.log(flatten(a, []));