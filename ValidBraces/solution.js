function validBraces(braces){
  stack = [];
  for(let i = 0; i < braces.length; i++) {
      if(stack.length == 0 || braces[i] == '[' || braces[i] == '{' || braces[i] == '('){
          stack.push(braces[i]);
      } else {
          character = stack.pop();
          if((braces[i] == ']' && character != '[')
          || (braces[i] == '}' && character != '{')
          || (braces[i] == ')' && character != '(')
          )
            return false;
      }
  }
  return stack.length == 0;
}