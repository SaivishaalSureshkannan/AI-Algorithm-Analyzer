import React from 'react';

const PredictionCard = ({ analysis }) => {
    if (!analysis) return null;

    return (
        <div className="bg-white border rounded shadow p-4 mb-4">
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
    );
};

export default PredictionCard;
