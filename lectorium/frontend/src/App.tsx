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
  const [content, setContent] = useState<ITranscribedText[]>([])
  const [par, setPar] = useState<ITranscribedText[]>([{
    id: 0,
    body:{
      part1:'lol',
      part2:'lol2',
      part3:'lol3',
      part4:'lol4',
      part5:'lol2',
      part6:'lol2',
      part7:'lol2',
      part8:'lol2',
      part9:'lol2',
      part10:'lol2',
      part11:'lol2'

    }
  }])

  const [isLoading, setIsLoading] = useState(false)



  useEffect(() => {
    fetchPosts()
  }, [])

  async function fetchPosts() {
    try {
      setIsLoading(true)
      const response = await axios.get<ITranscribedText[]>(window.location.origin+'/api/test/')
      setContent(response.data)
      console.log(content);
      setIsLoading(false)
    }catch(e) {
      console.log(e);
    }
  }

  console.log(content)

//   useEffect(() => {
//     axios({
//         method: 'GET',
//         url: window.location.origin+'/api/test/',
//     }).then(response => {
//         setContent(JSON.parse(response.data))
//         console.log('from useEffect: ', JSON.parse(response.data).body)
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
