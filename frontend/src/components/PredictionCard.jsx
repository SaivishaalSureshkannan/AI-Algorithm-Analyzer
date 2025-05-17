import React from 'react';

const PredictionCard = ({ analysis }) => {
    if (!analysis) return null;

    return (
        <div className="bg-white border rounded shadow p-4 mb-4">
            {/* Traditional Analysis */}
            <div className="mb-4">
                <h3 className="font-semibold text-lg mb-2">Traditional Analysis</h3>
                <div className="text-center mb-2">
                    <span className="font-semibold">Time Complexity: </span>
                    <span className="text-blue-600">{analysis.complexity}</span>
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
                        <span className="text-green-600">{analysis.mlPrediction.complexity}</span>
                    </div>
                    <div className="text-center mb-2">
                        <span className="font-semibold">Confidence: </span>
                        <span className="text-purple-600">
                            {(analysis.mlPrediction.confidence * 100).toFixed(1)}%
                        </span>
                    </div>
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
