//app_display.js

document.addEventListener('DOMContentLoaded', function () {
    const incomeInput = document.getElementById('income');
    const dateInput = document.getElementById('date');
    const jobSelect = document.getElementById('job');
    const incomeList = document.getElementById('income-list');
    const addButton = document.getElementById('add-income');
    const exportButton = document.getElementById('export-data');
    const pieChartCanvas = document.getElementById('pie-chart');
    
    addButton.addEventListener('click', function () {
        const incomeValue = parseFloat(incomeInput.value.trim());
        const dateValue = dateInput.value.trim();
        const jobValue = jobSelect.value.trim();

        if (!incomeValue || isNaN(incomeValue) || !dateValue || !jobValue) {
            alert('Invalid value. Please enter a valid income and fill in all fields.');
            return;
        }

        const listItem = document.createElement('li');
        listItem.textContent = `Income: $${incomeValue.toFixed(2)}, Date: ${dateValue}, Job: ${jobValue}`;
        incomeList.appendChild(listItem);

        incomeInput.value = '';
        dateInput.value = '';
        jobSelect.value = '';
        updatePieChart();
    });

exportButton.addEventListener('click', function () {
    // Create a string with the content and indices
    let content = '';
    const items = incomeList.children;

    for (let i = 0; i < items.length; i++) {
        content += `${i + 1}. ${items[i].textContent}\n`;
    }
    // Create a Blob with the content
    const blob = new Blob([content], { type: 'text/plain' });

    // Create a link element
    const link = document.createElement('a');
    link.href = URL.createObjectURL(blob);

    // Set the filename for the download
    link.download = 'income_data.txt';

    // Append the link to the document
    document.body.appendChild(link);

    // Trigger a click on the link to start the download
    link.click();

    // Remove the link from the document
    document.body.removeChild(link);

    });
});


function updatePieChart() {
    const jobLabels = Object.keys(incomesByJob);
    const incomeValues = Object.values(incomesByJob);

    // Check if the pie chart has been initialized
    if (!window.myPieChart) {
        // Initialize the pie chart
        window.myPieChart = new Chart(pieChartCanvas, {
            type: 'pie',
            data: {
                labels: jobLabels,
                datasets: [{
                    data: incomeValues,
                    backgroundColor: getRandomColors(jobLabels.length),
                }],
            },
        });
    } else {
        // Update the data of the existing pie chart
        window.myPieChart.data.labels = jobLabels;
        window.myPieChart.data.datasets[0].data = incomeValues;
        window.myPieChart.data.datasets[0].backgroundColor = getRandomColors(jobLabels.length);
        window.myPieChart.update();
    }
}

function getRandomColors(count) {
    const colors = [];
    for (let i = 0; i < count; i++) {
        const randomColor = '#' + Math.floor(Math.random()*16777215).toString(16);
        colors.push(randomColor);
    }
    return colors;
};

