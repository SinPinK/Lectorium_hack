import axios from 'axios';
import React, { useEffect, useState } from 'react';


function App() {
    const [test, setTest] = useState('Go Hack')

    useEffect(() => {
        axios({
            method: 'GET',
            url: window.location.origin+'/api/test/',
        }).then(response => {
            setTest(JSON.parse(response.data))
        })
    })
  return (
    <div className="App">
        <h1>{test}</h1>
    </div>
  );
}

export default App;