import axios, { AxiosRequestConfig } from "axios";
import React, { useEffect, useState } from "react";
import { BrowserRouter } from "react-router-dom";
import { Navbar } from "./pages/Navbar/Navbar";
import { AppRouter } from "./pages/AppRouter";
import { ITranscribedText } from "./utils/types";
import List from "./components/UI/List/List";
import { TextBlock } from "./components/TextBlock";

function App() {
  
  return (
    <BrowserRouter>
    
    <Navbar>
  
    <AppRouter />
    </Navbar>
     
    </BrowserRouter>
  );
}

export default App;
