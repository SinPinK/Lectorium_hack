import React, { useState } from "react";
import { DropCard } from "../../components/UI/DropCard";
import { TextBlock } from "../../components/Transcribation";

export const MainPage: React.FC = () => {
  const [text, setText] = useState({
    body: "Lorem ipsum dolor sit amet consectetur, adipisicing elit. Eum fugit cumque distinctio cum hic harum nostrum voluptatem, rem dolorum esse optio tenetur in rerum. In, recusandae expedita! Enim, reprehenderit. Officia!Lorem ipsum dolor sit amet consectetur, adipisicing elit. Eum fugit cumque distinctio cum hic harum nostrum voluptatem, rem dolorum esse optio tenetur in rerum. In, recusandae expedita! Enim, reprehenderit. Officia!Lorem ipsum dolor sit amet consectetur, adipisicing elit. Eum fugit cumque distinctio cum hic harum nostrum voluptatem, rem dolorum esse optio tenetur in rerum. In, recusandae expedita! Enim, reprehenderit. Officia!Lorem ipsum dolor sit amet consectetur, adipisicing elit. Eum fugit cumque distinctio cum hic harum nostrum voluptatem, rem dolorum esse optio tenetur in rerum. In, recusandae expedita! Enim, reprehenderit. Officia!",
  });

  return (
    <div className=" flex gap-8 flex-col">
      <DropCard />
      <TextBlock props={text} />
    </div>
  );
};
