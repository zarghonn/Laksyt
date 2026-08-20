
const readline = require("readline");

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

let numbers = [];

function askNumber() {
    if (numbers.length < 5) {
        rl.question("Enter a number: ", (answer) => {
            numbers.push(Number(answer));
            askNumber();
        });
    } else {
        console.log("Numbers in reverse order:");

        for (let i = numbers.length - 1; i >= 0; i--) {
            console.log(numbers[i]);
        }

        rl.close();
    }
}

askNumber();
