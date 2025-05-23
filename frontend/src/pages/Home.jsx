import React, { useState } from 'react';
import ComplexityGraph from '../components/ComplexityGraph';
import CodeEditor from '../components/CodeEditor';
import CalculateButton from '../components/CalculateButton';
import PredictionCard from '../components/PredictionCard';
import ExplanationBox from '../components/ExplanationBox';
import { analyzeCode } from '../services/api';

const Home = () => {
  const [code, setCode] = useState('');
  const [analysis, setAnalysis] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const handleAnalyze = async () => {
    if (!code.trim()) {
      setError('Please enter some code to analyze');
      return;
    }

    setLoading(true);
    setError(null);

    try {
      const result = await analyzeCode(code);
      setAnalysis(result);
    } catch (err) {
      setError('Failed to analyze code. Please try again.');
      console.error(err);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="min-h-screen flex flex-col items-center justify-center bg-lime-400 px-2">
      {/* Header */}
      <h1 className="w-full text-5xl font-extrabold text-center mb-8 mt-8">Algorithm Analyzer</h1>

      <div className="w-full max-w-2xl flex flex-col items-center">
        <h2 className="text-xl font-semibold mb-2 text-center">Code: </h2>
        {/* Code Input Section */}
        <div className="w-full flex flex-col mb-12">
          <CodeEditor code={code} onCodeChange={setCode} />
          <CalculateButton onClick={handleAnalyze} loading={loading} />
          {error && <div className="text-red-500 text-center mt-2">{error}</div>}
        </div>

        {/* Analysis Output Section */}
        <div className="w-full flex flex-col gap-6">
          <h2 className="text-xl font-semibold mb-2 text-center">Code Analysis: </h2>          <PredictionCard analysis={analysis} />
          <ComplexityGraph complexity={analysis?.mlPrediction?.complexity || analysis?.complexity} />
          <h2 className="text-xl font-semibold mb-2 text-center">Explanation: </h2>
          <ExplanationBox analysis={analysis} />
        </div>
      </div>
    </div>
  );
};

export default Home;