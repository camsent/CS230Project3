import { useState, useEffect } from 'react';



function LoginForm({ onChange }) {
    const [data, setData] = useState({ username: "", password: "" });
    const [error, setError] = useState(null);

    useEffect(() => {
        onChange(data);
    }, [data, onChange]);

    const handleLogin = async (e) => {
        e.preventDefault();
        try {
            const data = await loginUser(username, password);
            console.log("Login successful:", data);
            localStorage.setItem('session_id', data.session_id);
            alert("Login successful!");
        } catch (err) {
            setError(err.message);
        }
    }

    return (
        <form onSubmit={handleLogin}>
            <input className='loginForm'
                type="text"
                placeholder='Username'
                value={data.username}
                onChange={(e) => setData({ ...data, username: e.target.value })}
            />
            <br />
            <input className='loginForm'
                type="password"
                placeholder='Password'
                value={data.password}
                onChange={(e) => setData({ ...data, password: e.target.value })}
            />
        </form>    
    )
}

export default LoginForm; 