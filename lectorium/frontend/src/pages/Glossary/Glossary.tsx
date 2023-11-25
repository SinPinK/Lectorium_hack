import React, { useState } from "react";
import List from "../../components/UI/List/List";
import { ConceptItem } from "../../components/UI/Concept/ConceptItem";
import { ListVariant } from "../../components/UI/List/List";

export const Glossary: React.FC = () => {

  const [conc, setConc] = useState([
    {
      id: 0,
      title: 'Машина',
      body: 'это что ваще такое'
  }
])
 
  return (
    <div>
      <List
       variant={ListVariant.card}
        items={conc}
        renderItem={(item) => <ConceptItem props={item} key={item.id} />}
      />
    </div>
  );
};
