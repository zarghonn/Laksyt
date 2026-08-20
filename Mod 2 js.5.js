
const readline = require("readline");

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

let numbers = [];

function askNumber() {
    rl.question("Enter a number: ", (answer) => {
        let number = Number(answer);

        if (numbers.includes(number)) {
            console.log("This number has already been given!");

            numbers.sort((a, b) => a - b);

            console.log("Numbers in ascending order:");
            console.log(numbers);

            rl.close();
        } else {
            numbers.push(number);
            askNumber();
        }
    });
}

askNumber();
