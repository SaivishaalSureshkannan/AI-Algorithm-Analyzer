const API_URL = 'http://localhost:8000';

export const analyzeCode = async (code) => {
    try {
        const response = await fetch(`${API_URL}/analyze`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ code }),
        });

        if (!response.ok) {
            throw new Error('Failed to analyze code');
        }

        return await response.json();
    } catch (error) {
        console.error('Error analyzing code:', error);
        throw error;
    }
}; 