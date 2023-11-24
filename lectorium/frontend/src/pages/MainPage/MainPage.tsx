import React, { useState } from "react";
import { DropCard } from "../../components/UI/DropCard";
import { TextBlock } from "../../components/Transcribation";
import List from "../../components/UI/List/List";
import { IConcept } from "../../utils/types";
import { ConceptItem } from "../../components/UI/Concept/ConceptItem";

export const MainPage: React.FC = () => {
  const [text, setText] = useState({
    body: "Lorem ipsum dolor sit amet consectetur, adipisicing elit. Eum fugit cumque distinctio cum hic harum nostrum voluptatem, rem dolorum esse optio tenetur in rerum. In, recusandae expedita! Enim, reprehenderit. Officia!Lorem ipsum dolor sit amet consectetur, adipisicing elit. Eum fugit cumque distinctio cum hic harum nostrum voluptatem, rem dolorum esse optio tenetur in rerum. In, recusandae expedita! Enim, reprehenderit. Officia!Lorem ipsum dolor sit amet consectetur, adipisicing elit. Eum fugit cumque distinctio cum hic harum nostrum voluptatem, rem dolorum esse optio tenetur in rerum. In, recusandae expedita! Enim, reprehenderit. Officia!Lorem ipsum dolor sit amet consectetur, adipisicing elit. Eum fugit cumque distinctio cum hic harum nostrum voluptatem, rem dolorum esse optio tenetur in rerum. In, recusandae expedita! Enim, reprehenderit. Officia!",
  });
  const [concepts, setConcepts] = useState<IConcept[]>([
    {
      id: 1,
      title: "Машина",
      body: "Механизм, совершающий какую-н. полезную работу с преобразованием одного вида энергии в другой.",
    },
    { id: 2, title: "Велосипед", body: "Двухколесная, реже трёхколёсная машина для езды, приводимая в движение ногами ездока." },
    { id: 3, title: "Велосипед", body: "Двухколесная, реже трёхколёсная машина для езды, приводимая в движение ногами ездока." },
    { id: 4, title: "Велосипед", body: "Двухколесная, реже трёхколёсная машина для езды, приводимая в движение ногами ездока." },
    { id: 5, title: "Велосипед", body: "Двухколесная, реже трёхколёсная машина для езды, приводимая в движение ногами ездока." },
    { id: 6, title: "Велосипед", body: "Двухколесная, реже трёхколёсная машина для езды, приводимая в движение ногами ездока." },
    { id: 7, title: "Велосипед", body: "Двухколесная, реже трёхколёсная машина для езды, приводимая в движение ногами ездока." },
    { id: 8, title: "Велосипед", body: "Двухколесная, реже трёхколёсная машина для езды, приводимая в движение ногами ездока." },
  ]);

  return (
    <div className=" flex gap-8 flex-col">
      <div className="flex gap-8 flex-row">
      <DropCard />
      <List
        items={concepts}
        renderItem={(item) => <ConceptItem props={item} key={item.id} />}
      />
      </div>
      
      <TextBlock props={text} />
    </div>
  );
};
