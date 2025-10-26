import { useState, useEffect } from 'react';

const API_URL = 'http://127.0.0.1:8000';

export async function registerUser(username, password) {
    const response = await fetch(`${API_URL}/register/`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ username, password }),
    });
    
    if (!response.ok) {
        throw new Error ("Registration failed");
    }
    return await response.json();
};

export async function loginUser(username, password) {
    const response = await fetch(`${API_URL}/login/`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ username, password }),
    });
    if (!response.ok) {
        throw new Error ("Login failed");
    }
    return await response.json();
};

function SignUpForm({ onChange }) {

    const [error, setError] = useState(null);
    const [data, setData] = useState({
        username: "",
        password: ""
    })

    useEffect(() => {
        onChange(data);
    }, [data, onChange]);

    const handleSignUp = async (e) => {
        e.preventDefault();
        try {
            const data = await signUpUser(username, password);
            console.log("SignUp successful:", data);
            alert("SignUp successful!");
        } catch (err) {
            setError(err.message);
        }
    }
  
    return (
        <form onSubmit={handleSignUp}>
            <input className='signUpForm'
                type="text"
                placeholder='Username'
                value={data.username}
                onChange={(e) => setData({ ...data, username: e.target.value })}
            />
            <br />
            <input className='signUpForm'
                type="password"
                placeholder='Password'
                value={data.password}
                onChange={(e) => setData({ ...data, password: e.target.value })}
            />
        </form>
    )    
}


export default SignUpForm; 