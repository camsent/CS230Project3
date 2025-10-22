import { useState, useEffect } from 'react';

function LoginForm({ onChange }) {
    const [data, setData] = useState({ username: "", password: "" });

    useEffect(() => {
        onChange(data);
    }, [data, onChange]);

    return (
        <form>
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