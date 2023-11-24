import axios from "axios";
import React, { useEffect, useState } from "react";
import { BrowserRouter } from "react-router-dom";
import { Navbar } from "./pages/Navbar/Navbar";
import { AppRouter } from "./pages/AppRouter";

function App() {
  const [test, setTest] = useState("Go Hack");
  const [content, setContent] = useState({'test': "Go hack"})

  useEffect(() => {
      axios({
          method: 'GET',
          url: window.location.origin+'/api/test/',
      }).then(response => {
          setContent(JSON.parse(response.data))
          console.log('from useEffect: ', JSON.parse(response.data).body)
      })
  })
  return (
    <BrowserRouter>
    <Navbar>
    <h1>{content['test']}</h1>
    <AppRouter />
    </Navbar>
     
    </BrowserRouter>
  );
}

export default App;
