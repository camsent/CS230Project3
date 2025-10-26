import { useState } from 'react';
import './App.css';
import LoginForm from './assets/components/LoginForm.jsx';
import SignUpForm from './assets/components/SignUpForm.jsx';

function App() {
  const [page, setPage] = useState('login');
  const [formData, setFormData] = useState({});

  function handleChange(data) {
    setFormData(data);
  }

  async function handleSubmit() {
    const url =
      page === 'login'
        ? 'http://127.0.0.1:8000/login'      // FastAPI login route
        : 'http://127.0.0.1:8000/register';  // FastAPI signup route

    try {
      const response = await fetch(url, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(formData),
      });

      console.log('Raw response:', response);

      // If the response is not JSON (e.g., 500 HTML error), catch it
      let data = {};
      try {
        data = await response.json();
      } catch (jsonErr) {
        console.warn('Response is not JSON:', jsonErr);
      }

      if (!response.ok) {
        console.error('Backend error:', data);
        alert(`Error: ${data.detail || response.status}`);
      } else {
        console.log('Success data:', data);
        alert(page === 'login' ? 'Login successful!' : 'Sign up successful!');
      }
    } catch (err) {
      console.error('Fetch failed:', err);
      alert('Failed to connect to the server. Check console for details.');
    }
  }

  return (
    <div style={{ width: '300px', margin: '50px auto', textAlign: 'center' }}>
      <div className="card">
        <div className="card-info">
          <h2>{page === 'login' ? 'Login' : 'Sign Up'}</h2>

          {page === 'login' ? (
            <LoginForm onChange={handleChange} />
          ) : (
            <SignUpForm onChange={handleChange} />
          )}

          <div style={{ marginTop: '20px' }}>
            <button id="topButton" onClick={handleSubmit}>
              {page === 'login' ? 'Login' : 'Sign Up'}
            </button>

            <button
              id="bottomButton"
              style={{ marginLeft: '10px' }}
              onClick={() => setPage(page === 'login' ? 'signup' : 'login')}
            >
              Switch to {page === 'login' ? 'Sign Up' : 'Login'}
            </button>
          </div>
        </div>
      </div>
    </div>
  );
}

export default App;
