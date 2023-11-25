import React, { useState, useEffect } from "react";
import { DropCard } from "../../components/UI/DropCard";
import { TextBlock } from "../../components/TextBlock";
import List, { ListVariant } from "../../components/UI/List/List";
import { IConcept, ITranscribedText } from "../../utils/types";
import { ConceptItem } from "../../components/UI/Concept/ConceptItem";
import axios from "axios";

export const MainPage: React.FC = () => {
  const [conc, setConc] = useState([
    {
      id: 0,
      title: "Машина",
      body: "это что ваще такое",
    },
  ]);


  const [par, setPar] = useState<ITranscribedText[]>([
    {
      id: 3,
      body: {
        part1: '',
        part2: "",
        part3: "",
        part4: "",
      },
    },
  ]);
  
  const createText = (newPost:ITranscribedText) => {
    setPar([newPost])
  }

  return (
    <div className="flex flex-col gap-8">
      <div className="flex gap-8 flex-row">
        <DropCard createText={createText} />
        <List
         variant={ListVariant.card}
          items={conc}
          renderItem={(item) => <ConceptItem props={item} key={item.id + 1} />}
        />
      </div>

      <List
      variant={ListVariant.list}
        items={par}
        renderItem={(item) => <TextBlock props={item} key={item.id} />}
      />
    </div>
  );
};
