import React, { useState, useEffect } from "react";

function App() {
  const [pyodide, setPyodide] = useState(null);
  const [diameter, setDiameter] = useState(150);
  const [vLines, setVLines] = useState(10);
  const [hLines, setHLines] = useState(10);
  const [margin, setMargin] = useState(5);
  const [svgCode, setSvgCode] = useState("");

  // Load Pyodide
  useEffect(() => {
    async function loadPy() {
      const py = await window.loadPyodide({
        indexURL: "./pyodide/"
      });
      const generatorPy = await (await fetch("./generator.py")).text();
      await py.runPythonAsync(generatorPy);
      setPyodide(py);
    }
    loadPy();
  }, []);

  const generate = async () => {
    if (!pyodide) return;

    const code = `
generate_svg(${diameter}, ${vLines}, ${hLines}, ${margin})
    `;

    const svg = await pyodide.runPythonAsync(code);
    setSvgCode(svg);
  };

  return (
    <div style={{ padding: "20px" }}>
      <h1>Wafer Grid Generator</h1>

      <div>
        <label>Wafer diameter (mm): </label>
        <input value={diameter} onChange={(e) => setDiameter(Number(e.target.value))}/>
      </div>

      <div>
        <label>Vertical lines: </label>
        <input value={vLines} onChange={(e) => setVLines(Number(e.target.value))}/>
      </div>

      <div>
        <label>Horizontal lines: </label>
        <input value={hLines} onChange={(e) => setHLines(Number(e.target.value))}/>
      </div>

      <div>
        <label>Margin (mm): </label>
        <input value={margin} onChange={(e) => setMargin(Number(e.target.value))}/>
      </div>

      <button onClick={generate}>Generate SVG</button>

      <h2>Preview:</h2>
      <div dangerouslySetInnerHTML={{ __html: svgCode }} />

      <h2>Download:</h2>
      {svgCode && (
        <a
          href={`data:image/svg+xml;charset=utf-8,${encodeURIComponent(svgCode)}`}
          download="wafer.svg"
        >
          Download SVG
        </a>
      )}
    </div>
  );
}

export default App;
