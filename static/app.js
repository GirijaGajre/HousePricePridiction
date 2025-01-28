async function predictPrice() {
    // Get user inputs from the HTML form
    const sqft = document.getElementById('sqft').value;
    const bhk = document.getElementById('bhk').value;
    const bath = document.getElementById('bath').value;
    const location = document.getElementById('location').value;

    // Send the input data to the Flask backend
    const response = await fetch('http://127.0.0.1:5000/predict', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            total_sqft: parseFloat(sqft),
            bhk: parseInt(bhk),
            bath: parseInt(bath),
            location: location
        })
    });

    // Parse the response and display the predicted price
    const result = await response.json();
    document.getElementById('result').innerText = `Predicted Price: ₹${result.predicted_price}`;
}
