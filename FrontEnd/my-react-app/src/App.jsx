import { useState } from 'react'
import './App.css'
import LoginForm from './assets/components/LoginForm.jsx'
import SignUpForm from './assets/components/SignUpForm.jsx'

function App() {
  const [page, setPage] = useState('login');
  const [formData, setFormData] = useState({
  });

  function handleChange(data) {
    setFormData(data);
  }
  
  

  return (
    <div style={{ width: '300px', margin: '50px auto', textAlign: 'center'}}>
      {/*<!-- From Uiverse.io by alexruix -->*/} 
      <div class="card">
        <div class="card-info">
        
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

            <button id="bottomButton"
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