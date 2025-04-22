function FirstFactorial(num) { 

    for (i=num-1 ; i > 0 ; i-- ) {
        num = num * i
        console.log(i)
    }
    
    return num; 
  
  }
     
  // keep this function call here 
  //console.log(FirstFactorial(readline()));
  console.log(FirstFactorial(4));