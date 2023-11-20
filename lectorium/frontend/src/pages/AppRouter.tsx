import React from 'react'
import { Route,  Routes} from "react-router-dom";
import { MainPage } from "../pages/MainPage/MainPage";
import { Help } from "../pages/Help/Help";
import { Archive } from "../pages/Archive/Archive";


export const AppRouter = () => {
  return (
    <Routes>
        <Route path="/main" element={<MainPage/>}/>
        <Route path="/help" element={<Help/>}/>
        <Route path="/archive" element={<Archive/>}/>
      </Routes>
  )
}
