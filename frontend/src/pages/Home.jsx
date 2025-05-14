import React from 'react';
import ComplexityGraph from '../components/ComplexityGraph';
import CodeEditor from '../components/CodeEditor';
import CalculateButton from '../components/CalculateButton';
import PredictionCard from '../components/PredictionCard';
import ExplanationBox from '../components/ExplanationBox';


const Home = () => {
  return (
    <div className="min-h-screen flex flex-col items-center justify-center bg-lime-400 px-2">
      {/* Header */}
      <h1 className="w-full text-5xl font-extrabold text-center mb-8 mt-8">Algorithm Analyzer</h1>

      <div className="w-full max-w-2xl flex flex-col items-center">
        <h2 className="text-xl font-semibold mb-2 text-center">Code: </h2>
        {/* Code Input Section */}
        <div className="w-full flex flex-col mb-12">
          <CodeEditor />
          <CalculateButton />
        </div>

        {/* Analysis Output Section */}
        <div className="w-full flex flex-col gap-6">
          <h2 className="text-xl font-semibold mb-2 text-center">Code Analysis: </h2>
          <PredictionCard />
          <ComplexityGraph />
          <h2 className="text-xl font-semibold mb-2 text-center">Explanation: </h2>
          <ExplanationBox />
        </div>
      </div>
    </div>
  );
};

export default Home;