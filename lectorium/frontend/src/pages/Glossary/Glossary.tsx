import React, { useState } from "react";
import List from "../../components/UI/List/List";
import { ConceptItem } from "../../components/UI/Concept/ConceptItem";

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
        items={conc}
        renderItem={(item) => <ConceptItem props={item} key={item.id} />}
      />
    </div>
  );
};
