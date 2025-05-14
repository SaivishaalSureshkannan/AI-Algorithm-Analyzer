import React from 'react';

const CodeEditor = () => (
  <div className="w-full h-48 bg-white border rounded shadow p-4 mb-4 flex items-center justify-center text-gray-50">
    <textarea
        className="w-full h-full p-2 border rounded text-gray-50"
        placeholder="Enter your code here..."
    />
  </div>
);

export default CodeEditor;
