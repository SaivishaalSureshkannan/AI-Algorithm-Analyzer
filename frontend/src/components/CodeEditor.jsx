import React from 'react';

const CodeEditor = ({ code, onCodeChange }) => (
  <div className="w-full h-48 bg-white border rounded shadow p-4 mb-4">
    <textarea
        className="w-full h-full p-2 border rounded text-gray-800 font-mono"
        placeholder="Enter your code here..."
        value={code}
        onChange={(e) => onCodeChange(e.target.value)}
    />
  </div>
);

export default CodeEditor;
