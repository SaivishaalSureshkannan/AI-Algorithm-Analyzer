const API_URL = 'http://localhost:8000';

export const analyzeCode = async (code) => {
    try {
        // Get both traditional analysis and ML prediction
        const [analysisResponse, mlResponse] = await Promise.all([
            fetch(`${API_URL}/analyze`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ code }),
            }),
            fetch(`${API_URL}/predict`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ code }),
            })
        ]);

        if (!analysisResponse.ok || !mlResponse.ok) {
            throw new Error('Failed to analyze code');
        }

        const analysis = await analysisResponse.json();
        const mlPrediction = await mlResponse.json();

        // Combine both results
        return {
            ...analysis,
            mlPrediction: {
                complexity: mlPrediction.predicted_complexity,
                confidence: mlPrediction.confidence,
                features: mlPrediction.features
            }
        };
    } catch (error) {
        console.error('Error analyzing code:', error);
        throw error;
    }
}; 