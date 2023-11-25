import axios, { AxiosRequestConfig } from "axios";
import React, { useEffect, useState } from "react";
import { BrowserRouter } from "react-router-dom";
import { Navbar } from "./pages/Navbar/Navbar";
import { AppRouter } from "./pages/AppRouter";
import { ITranscribedText } from "./utils/types";
import List from "./components/UI/List/List";
import { TextBlock } from "./components/TextBlock";

function App() {
  const [test, setTest] = useState();
  const [content, setContent] = useState<ITranscribedText[]>([]);
  const [par, setPar] = useState<ITranscribedText[]>([
    {
      id: 0,
      body: {
        part1: "lol",
        part2: "lol2",
        part3: "lol3",
        part4: "lol4",
      },
    },
  ]);

  return (
    <BrowserRouter>
      <Navbar>
        <AppRouter />
      </Navbar>
    </BrowserRouter>
  );
}

export default App;
