import React, { useState } from "react";
import { DropCard } from "../../components/UI/DropCard";
import { TextBlock } from "../../components/TextBlock";
import List from "../../components/UI/List/List";
import { IConcept, ITranscribedText } from "../../utils/types";
import { ConceptItem } from "../../components/UI/Concept/ConceptItem";

export const MainPage: React.FC = () => {
  const [text, setText] = useState({
    body: "Lorem ipsum dolor sit amet consectetur, adipisicing elit. Eum fugit cumque distinctio cum hic harum nostrum voluptatem, rem dolorum esse optio tenetur in rerum. In, recusandae expedita! Enim, reprehenderit. Officia!Lorem ipsum dolor sit amet consectetur, adipisicing elit. Eum fugit cumque distinctio cum hic harum nostrum voluptatem, rem dolorum esse optio tenetur in rerum. In, recusandae expedita! Enim, reprehenderit. Officia!Lorem ipsum dolor sit amet consectetur, adipisicing elit. Eum fugit cumque distinctio cum hic harum nostrum voluptatem, rem dolorum esse optio tenetur in rerum. In, recusandae expedita! Enim, reprehenderit. Officia!Lorem ipsum dolor sit amet consectetur, adipisicing elit. Eum fugit cumque distinctio cum hic harum nostrum voluptatem, rem dolorum esse optio tenetur in rerum. In, recusandae expedita! Enim, reprehenderit. Officia!",
  });

  const [conc, setConc] = useState([
    {
      id: 0,
      title: 'Машина',
      body: 'это что ваще такое'
  }
])

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

  

  
 

  return (
    // <div className=" flex gap-8 flex-col">
    //   <div className="flex gap-8 flex-row">
    //   <DropCard />
    //   <List
    //     items={}
    //     renderItem={(item) => <ConceptItem props={item} key={item.id} />}
    //   />
    //   </div>
      
    //   <TextBlock props={text} />
    // </div>

    <div className="flex flex-col gap-8">
      <div className="flex gap-8 flex-row">
      <DropCard />
      <List
        items={conc}
        renderItem={(item) => <ConceptItem props={item} key={item.id} />}
      />
      </div>
      
      <List items={par} renderItem={(item) => <TextBlock props={item} key={item.id} /> } />
    </div>
  );
};
