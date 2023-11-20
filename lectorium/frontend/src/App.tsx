import axios from "axios";
import React, { useEffect, useState } from "react";
import { BrowserRouter } from "react-router-dom";
import { Navbar } from "./pages/Navbar/Navbar";
import { AppRouter } from "./pages/AppRouter";

function App() {
  const [test, setTest] = useState("Go Hack");

  // useEffect(() => {
  //     axios({
  //         method: 'GET',
  //         url: window.location.origin+'/api/test/',
  //     }).then(response => {
  //         setTest(JSON.parse(response.data))
  //     })
  // })
  return (
    <BrowserRouter>
    <Navbar>
    <AppRouter />
    </Navbar>
     
    </BrowserRouter>
  );
}

export default App;
