import React from 'react';

const PredictionCard = ({ analysis }) => {
    if (!analysis) return null;

    const getComplexityColor = (complexity) => {
        switch (complexity) {
            case 'O(1)':
                return 'text-green-600';
            case 'O(n)':
                return 'text-blue-600';
            case 'O(n²)':
                return 'text-orange-600';
            case 'O(2ⁿ)':
                return 'text-red-600';
            case 'Unknown':
                return 'text-gray-600';
            default:
                return 'text-blue-600';
        }
    };

    const getConfidenceColor = (confidence, complexity) => {
        if (complexity === 'Unknown') {
            return 'text-gray-600';
        }
        if (confidence >= 0.8) {
            return 'text-green-600';
        } else if (confidence >= 0.6) {
            return 'text-yellow-600';
        } else {
            return 'text-orange-600';
        }
    };

    return (
        <div className="bg-white border rounded shadow p-4 mb-4">
            {/* Traditional Analysis */}
            <div className="mb-4">
                <h3 className="font-semibold text-lg mb-2">Traditional Analysis</h3>
                <div className="text-center mb-2">
                    <span className="font-semibold">Time Complexity: </span>
                    <span className={getComplexityColor(analysis.complexity)}>
                        {analysis.complexity}
                    </span>
                </div>
                <div className="text-sm text-gray-600">
                    <div>For Loops: {analysis.loops.for_loops}</div>
                    <div>While Loops: {analysis.loops.while_loops}</div>
                    <div>Recursion: {analysis.recursion ? 'Yes' : 'No'}</div>
                </div>
                {analysis.suggestions.length > 0 && (
                    <div className="mt-2">
                        <div className="font-semibold">Suggestions:</div>
                        <ul className="list-disc list-inside">
                            {analysis.suggestions.map((suggestion, index) => (
                                <li key={index} className="text-sm text-gray-600">{suggestion}</li>
                            ))}
                        </ul>
                    </div>
                )}
            </div>

            {/* ML Prediction */}
            {analysis.mlPrediction && (
                <div className="border-t pt-4">
                    <h3 className="font-semibold text-lg mb-2">ML Prediction</h3>
                    <div className="text-center mb-2">
                        <span className="font-semibold">Predicted Complexity: </span>
                        <span className={getComplexityColor(analysis.mlPrediction.complexity)}>
                            {analysis.mlPrediction.complexity}
                        </span>
                    </div>
                    <div className="text-center mb-2">
                        <span className="font-semibold">Confidence: </span>
                        <span className={getConfidenceColor(analysis.mlPrediction.confidence, analysis.mlPrediction.complexity)}>
                            {(analysis.mlPrediction.confidence * 100).toFixed(1)}%
                        </span>
                    </div>
                    {analysis.mlPrediction.complexity === 'Unknown' && (
                        <div className="text-center text-sm text-gray-600 mb-2">
                            The algorithm's complexity pattern doesn't match our known patterns or the confidence is too low.
                        </div>
                    )}
                    <div className="text-sm text-gray-600">
                        <div className="font-semibold mb-1">Key Features:</div>
                        <div>Input Variables: {analysis.mlPrediction.features.input_vars}</div>
                        <div>Nested Loops: {analysis.mlPrediction.features.nested_loops}</div>
                        <div>Recursive Calls: {analysis.mlPrediction.features.recursive_calls}</div>
                    </div>
                </div>
            )}
        </div>
    );
};

export default PredictionCard;
