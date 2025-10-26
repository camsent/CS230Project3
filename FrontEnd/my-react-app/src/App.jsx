import { useState } from 'react'
import './App.css'
import LoginForm from './assets/components/LoginForm.jsx'
import SignUpForm from './assets/components/SignUpForm.jsx'
import CalendarApp from './assets/components/Calendar.jsx'

function App() {
  const [page, setPage] = useState('login');
  const [formData, setFormData] = useState({});

  function handleChange(data) {
    setFormData(data);
  }

  // 🟢 Handles login/signup submission
  function handleSubmit() {
    if (page === 'login') {
      console.log("Logging in:", formData);
      // Example: check if user entered something before switching
      if (formData.username && formData.password) {
        setPage('calendar'); // ✅ Switch to the calendar after login
      } else {
        alert('Please enter username and password');
      }
    } else {
      // Handle signup
      console.log("Signing up:", formData);
      setPage('login'); // Go back to login after signup
    }
  }

  // 🟢 Show Calendar if user is logged in
  if (page === 'calendar') {
    return <CalendarApp />;
  }

  return (
    <div style={{ width: '300px', margin: '50px auto', textAlign: 'center' }}>
      <div className="card">
        <div className="card-info">
          <h2 id="Login">{page === "login" ? "Login" : "Sign Up"}</h2>

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
  )
}

export default App