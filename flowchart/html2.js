function generateFlowchart() {
    // Get the user input from the textarea
    const stepsInput = document.getElementById('stepsInput').value;
    
    // Split the input string into an array of steps
    const steps = stepsInput.split(',').map(step => step.trim());
    
    // Get the container where the flowchart will be displayed
    const flowchartContainer = document.getElementById('flowchartContainer');
    
    // Clear previous flowchart content
    flowchartContainer.innerHTML = '';
    
    // Create the flowchart by iterating over the steps array
    steps.forEach((step, index) => {
        // Create a div for each step
        const stepDiv = document.createElement('div');
        stepDiv.className = 'step';
        stepDiv.innerText = step;
        flowchartContainer.appendChild(stepDiv);
        
        // Add an arrow between steps, except after the last step
        if (index < steps.length - 1) {
            const arrowDiv = document.createElement('div');
            arrowDiv.className = 'arrow';
            flowchartContainer.appendChild(arrowDiv);
        }
    });
}
