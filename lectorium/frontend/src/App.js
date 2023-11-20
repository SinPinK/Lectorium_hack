import logo from './logo.svg';
import './App.css';
import axios from 'axios'
import { useState, useEffect } from 'react'

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

    </div>
  );
}

export default App;
