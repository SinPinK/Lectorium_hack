<<<<<<< HEAD:lectorium/frontend/src/App.js
import logo from './logo.svg';
import './App.css';
import axios from 'axios'
import { useState, useEffect } from 'react'
=======
import React from 'react';


>>>>>>> 2ffab1cd29d8ce62ef6870b0b60cf71a46b1349b:lectorium/frontend/src/App.tsx

function App() {
    const [test, setTest] = useState('Go Hack')
    useEffect(() => {
        axios({
            method: 'GET',
            url: window.location.origin+'/api/test/',
        }).then(response => {
            setTest(JSON.parse(response.data))
        }).catch(error => {
            console.log('error in axios: ', error)
        })
    }, [])

  return (
    <div className="App">
<<<<<<< HEAD:lectorium/frontend/src/App.js
      <h1>{test}</h1>
=======
     
>>>>>>> 2ffab1cd29d8ce62ef6870b0b60cf71a46b1349b:lectorium/frontend/src/App.tsx
    </div>
  );
}

export default App;
