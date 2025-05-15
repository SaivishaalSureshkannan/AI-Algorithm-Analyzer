import React from 'react';

const CalculateButton = ({ onClick, loading }) => {
    return (
        <button 
            className="w-full bg-red-500 text-white py-2 rounded shadow mb-8 hover:bg-red-600 transition-colors disabled:bg-red-300"
            onClick={onClick}
            disabled={loading}
        >
            {loading ? 'Analyzing...' : 'Calculate'}
        </button>
    );
};

export default CalculateButton;

