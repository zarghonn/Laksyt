
const readline = require("readline");

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

let numbers = [];

function askNumber() {
    rl.question("Enter a number (0 to stop): ", (answer) => {
        let number = Number(answer);

        if (number === 0) {
            numbers.sort((a, b) => b - a);

            console.log("Numbers from largest to smallest:");
            console.log(numbers);

            rl.close();
        } else {
            numbers.push(number);
            askNumber();
        }
    });
}

askNumber();
