async function analyzeNews(text) {
    const response = await fetch('/api/analyze', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ text })
    });
    return await response.json();
}

function displayResults(result) {
    const resultElement = document.getElementById('result-container');
    resultElement.className = result.is_fake ? 
        'result-container result-fake' : 'result-container result-true';
    
    document.getElementById('confidence-bar').style.width = `${result.confidence * 100}%`;
    document.getElementById('result-text').textContent = result.is_fake ?
        'This content appears to be misleading or false.' : 
        'This content appears to be credible.';
    
    // Render indicators
    renderIndicators(result.indicators);
}
