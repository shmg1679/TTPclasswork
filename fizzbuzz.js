
function fizzbuzz(num){
    //from 1 to num
    for(var i=1;i<=num;i++){
        //if i mod 3 is equal to 0, print fizz
        if(i%3===0){
            console.log("fizz")
            //if i mod 5 is equal to 0, print buzz as well right after
            //unless I create a string to link it, it'll print fizz \n buzz
            if(i%5===0){
                console.log("buzz")
            }
        }else{//otherwise print the number
            console.log(i)
        }
    }
}
//pass any number to the function in this case I pass 100 to the function
//note to self, to run this on vscode, open terminal, cd to where this file is
//and then enter : node name.js
fizzbuzz(100);

