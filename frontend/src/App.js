import React, { useState } from 'react';
import './App.css';

function App() {
  const [report, setReport] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const runScan = async () => {
    setLoading(true);
    setError(null);
    try {
      const response = await fetch('http://127.0.0.1:8000/scan/full', {
        method: 'POST',
      });
      const data = await response.json();
      setReport(data.report);
    } catch (err) {
      setError('Backend connect karanna bari — API running da check karanna!');
    }
    setLoading(false);
  };

  const getRiskColor = (score) => {
    if (score >= 80) return '#00ff88';
    if (score >= 50) return '#ffaa00';
    return '#ff4444';
  };

  return (
    <div style={styles.container}>
      <div style={styles.header}>
        <h1 style={styles.title}>🛡️ DevSecOps Shield</h1>
        <p style={styles.subtitle}>AI-Powered Security Pipeline</p>
      </div>

      <button
        style={styles.button}
        onClick={runScan}
        disabled={loading}
      >
        {loading ? '⏳ Scanning...' : '🚀 Run Security Scan'}
      </button>

      {error && (
        <div style={styles.errorBox}>
          ❌ {error}
        </div>
      )}

      {report && (
        <div style={styles.reportContainer}>
          <div style={styles.scoreBox}>
            <h2 style={{ color: getRiskColor(report.risk_score) }}>
              🤖 AI Risk Score: {report.risk_score}/100
            </h2>
            <h3 style={{ color: getRiskColor(report.risk_score) }}>
              {report.verdict}
            </h3>
          </div>

          <div style={styles.grid}>
            <div style={styles.card}>
              <h3>🔐 Secrets</h3>
              <p style={styles.count}>{report.secrets?.count || 0}</p>
              <p>{report.secrets?.count === 0 ? '✅ Clean' : '❌ Found'}</p>
            </div>

            <div style={styles.card}>
              <h3>🧪 Code Issues</h3>
              <p style={styles.count}>{report.bandit?.count || 0}</p>
              <p>{report.bandit?.count === 0 ? '✅ Clean' : '⚠️ Issues Found'}</p>
            </div>

            <div style={styles.card}>
              <h3>📦 Dependencies</h3>
              <p style={styles.count}>{report.dependencies?.count || 0}</p>
              <p>{report.dependencies?.count === 0 ? '✅ Clean' : '❌ Vulnerable'}</p>
            </div>

            <div style={styles.card}>
              <h3>🐳 Container</h3>
              <p style={styles.count}>{report.container?.critical || 0}</p>
              <p>Critical Vulnerabilities</p>
            </div>
          </div>
        </div>
      )}
    </div>
  );
}

const styles = {
  container: {
    minHeight: '100vh',
    backgroundColor: '#0a0e1a',
    color: '#ffffff',
    fontFamily: 'Arial, sans-serif',
    padding: '40px 20px',
  },
  header: {
    textAlign: 'center',
    marginBottom: '40px',
  },
  title: {
    fontSize: '2.5rem',
    color: '#00ff88',
    margin: 0,
  },
  subtitle: {
    color: '#888',
    fontSize: '1.1rem',
  },
  button: {
    display: 'block',
    margin: '0 auto 40px',
    padding: '15px 40px',
    fontSize: '1.1rem',
    backgroundColor: '#00ff88',
    color: '#0a0e1a',
    border: 'none',
    borderRadius: '8px',
    cursor: 'pointer',
    fontWeight: 'bold',
  },
  errorBox: {
    backgroundColor: '#ff444422',
    border: '1px solid #ff4444',
    borderRadius: '8px',
    padding: '15px',
    margin: '0 auto 20px',
    maxWidth: '600px',
    textAlign: 'center',
  },
  reportContainer: {
    maxWidth: '900px',
    margin: '0 auto',
  },
  scoreBox: {
    textAlign: 'center',
    backgroundColor: '#111827',
    borderRadius: '12px',
    padding: '30px',
    marginBottom: '30px',
  },
  grid: {
    display: 'grid',
    gridTemplateColumns: 'repeat(2, 1fr)',
    gap: '20px',
  },
  card: {
    backgroundColor: '#111827',
    borderRadius: '12px',
    padding: '25px',
    textAlign: 'center',
    border: '1px solid #1f2937',
  },
  count: {
    fontSize: '2.5rem',
    fontWeight: 'bold',
    color: '#00ff88',
    margin: '10px 0',
  },
};

export default App;