import React, { useState } from "react";
import List from "../../components/UI/List/List";
import { IConcept } from "../../utils/types";
import { ConceptItem } from "../../components/UI/Concept/ConceptItem";

export const Glossary: React.FC = () => {
  const [concepts, setConcepts] = useState<IConcept[]>([
    {
      id: 1,
      title: "Машина",
      body: "Механизм, совершающий какую-н. полезную работу с преобразованием одного вида энергии в другой.",
    },
    { id: 2, title: "Велосипед", body: "Двухколесная, реже трёхколёсная машина для езды, приводимая в движение ногами ездока." },
  ]);
  return (
    <div>
      <List
        items={concepts}
        renderItem={(item) => <ConceptItem props={item} key={item.id} />}
      />
    </div>
  );
};
