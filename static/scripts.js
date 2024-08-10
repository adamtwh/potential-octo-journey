function insertSampleInputPart1() {
    const sampleInput = "10 10\n1 2 N\nFFRFFFRRLF";
    document.getElementById('input1').value = sampleInput;
}

function insertSampleInputPart2() {
    const sampleInput = "10 10\n\nA\n1 2 N\nFFRFFFFRRL\n\nB\n7 8 W\nFFLFFFFFFF";
    document.getElementById('input2').value = sampleInput;
}

document.getElementById('part1Form').addEventListener('submit', function(event) {
    event.preventDefault();
    const form = event.target;
    const formData = new FormData(form);

    fetch('/simulate_part1', {
        method: 'POST',
        body: formData
    })
        .then(response => response.text())
        .then(text => {
            document.getElementById('output1').innerText = text;
        })
        .catch(error => {
            console.error('Error:', error);
            document.getElementById('output1').innerText = 'An error occurred.';
        });
});

document.getElementById('part2Form').addEventListener('submit', function(event) {
    event.preventDefault();
    const form = event.target;
    const formData = new FormData(form);

    fetch('/simulate_part2', {
        method: 'POST',
        body: formData
    })
        .then(response => response.text())
        .then(text => {
            document.getElementById('output2').innerText = text;
        })
        .catch(error => {
            console.error('Error:', error);
            document.getElementById('output2').innerText = 'An error occurred.';
        });
});