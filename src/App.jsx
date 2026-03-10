import "./index.css";

function App() {
  return (
    <div className="min-h-screen bg-gray-100">

      {/* Navbar */}
      <nav className="flex justify-between items-center p-6 bg-white shadow">
        <h1 className="text-2xl font-bold text-indigo-600">
          ResumeAI
        </h1>

        <button className="bg-indigo-600 text-white px-4 py-2 rounded-lg">
          Upload Resume
        </button>
      </nav>

      {/* Hero Section */}
      <div className="text-center mt-32">

        <h1 className="text-5xl font-bold text-gray-800">
          AI Resume Analyzer
        </h1>

        <p className="mt-4 text-gray-600 text-lg">
          Improve your resume and prepare for interviews using AI
        </p>

        <button className="mt-8 bg-indigo-600 text-white px-8 py-3 rounded-xl hover:bg-indigo-700">
          Get Started
        </button>

      </div>

    </div>
  );
}

export default App;