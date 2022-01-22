//code from youtube
// https://www.youtube.com/watch?v=M15LVmGe8-w

function cypherDecode(str, num){
    //convert string to lowercase
    var lowerCaseStr = str.toLowerCase();
    //split the string of alphabets into separate elements
    var alphabet= 'abcdefghijklmnopqrstuvwxyz'.split('');
    //string to hold new string
    var newStr='';

    //for loop to going through the string and then convert
    for(var i =0; i < lowerCaseStr.length;i++){
        //get current letter of the string we passed through
        var currentLetter = lowerCaseStr[i];
        //if its a space, add current letter to it and continue with the loop
        if(currentLetter===' '){
            newStr+=currentLetter;
            continue;
        }
        //basically making all the alphabet be assigned to a number eg: a=0 or a is at index 0
        //and will increase or decrease the placement 
        var currentIndex=alphabet.indexOf(currentLetter);
        //increasing the index of what the letters currently holds
        var newIndex = currentIndex +num;
        //if its greater than index 25, wrap around using modulus so z at index 25 and plus 2 for example
        // to become 27, minus 26 and it'll become 1 or b
        if(newIndex > 25) newIndex=newIndex-26;
        //if negative number, add 26 to get it
        if(newIndex<0) newIndex = newIndex+26;
        //if its upper case, add to the letter to newstr as uppercase
        if(str[i]===str[i].toUpperCase()){
            newStr +=alphabet[newIndex].toUpperCase();
            //otherwise add it it newStr as is
        }else newStr+= alphabet[newIndex];   
    }
    //return the decoded string
    return newStr
}
//send this to the function, the key is 2
console.log(cypherDecode('Rfyr uyq dsl zsr Gk rpwgl em cyr qmkc ZZO afgaicl',2))