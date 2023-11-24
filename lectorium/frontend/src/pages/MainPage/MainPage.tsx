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

    <div>

    </div>
  );
};
