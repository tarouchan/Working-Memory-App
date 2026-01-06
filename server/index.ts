import { spawn } from "child_process";

console.log("Starting Streamlit app...");

const streamlit = spawn("python3", ["-m", "streamlit", "run", "app.py", "--server.port", "5000", "--server.address", "0.0.0.0"], {
  stdio: "inherit",
  shell: true
});

streamlit.on('error', (err) => {
  console.error('Failed to start streamlit:', err);
});

streamlit.on('close', (code) => {
  console.log(`Streamlit process exited with code ${code}`);
  process.exit(code || 0);
});
