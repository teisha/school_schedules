import React from 'react';
import Login from '../components/Login'


export type LoginInputs = {
  email: string
  password: string
}

const LoginPage: React.FC<{}> = ()  => {
    return (
        <Login />
    )
}

export default LoginPage;





//   const handleInputChange = (e: React.ChangeEvent<any>) => {
//     e.persist();
//     setInputs({
//       ...inputs,
//       [e.target.name]: e.target.value,
//     });
//   };