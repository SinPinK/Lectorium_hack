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

  const [isLoading, setIsLoading] = useState(false)



  useEffect(() => {
    fetchPosts()
  }, [])

  async function fetchPosts() {
    try {
      setIsLoading(false)
      const response = await axios.get<ITranscribedText[]>(window.location.origin+'/api/test/')
      setContent(response.data)
      console.log(content);
      setIsLoading(true)
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
    {/* <List items={content} renderItem={(item) => <TextBlock props={item.body} key={item.id} /> } /> */}
    <Navbar>
      {/* {isLoading ? <p>`${}` </p>
                : <p>lol</p>
      }
     */}
    <AppRouter />
    </Navbar>
     
    </BrowserRouter>
  );
}

export default App;
