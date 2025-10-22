import { useState, useEffect } from 'react';

function SignUpForm({ onChange}) {

    const [data, setData] = useState({
        username: "",
        password: ""
    })

    useEffect(() => {
        onChange(data);
    }, [data, onChange]);

    return (
        <form>
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