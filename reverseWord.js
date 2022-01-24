//function to reverse the word
function reverseWord(str){
    //split it into char array
    str = str.split("");
    //j is reverse word(revWord) variable index
    var j=0;
    //declaring a new array to hold the reverse stuff
    var revWord=[];

    //since we can't use reverse(), just manually store each element from
    // the back to the new array
    for(var i=str.length-1;i>=0;i--){
        revWord[j] = str[i];
        j++;
    }

    //join it into a string
    revWord = revWord.join("");

    //part 2
    //split it again
    revWord= revWord.split(" ");

    //reset j
    j=0;
    //new array to basically do the same steps again
    var revWord2=[]
    //same reversing
    for(var i=revWord.length-1;i>=0;i--){
        revWord2[j] = revWord[i];
        j++;
    }
    //only difference this time is having space in "" to split it between words
    revWord2 = revWord2.join(" ");

    //return the array
    return revWord2;
}

//call the function and console.log or print it
console.log(reverseWord("reverse the word"));
// this reverse the entire string but if you just want to reverse the string
// then just add space inside the "" of split("") and join("") to do it.
// but code added in part 2 will be what we wanted in this puzzle, 
//removing it will be the other result.

//All this can be summed up as:
// return str.split("").reverse().join("").split(" ").reverse().join(" ")


