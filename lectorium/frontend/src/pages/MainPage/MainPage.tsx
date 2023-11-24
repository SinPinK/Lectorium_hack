import React, { useState, useEffect } from "react";
import { DropCard } from "../../components/UI/DropCard";
import { TextBlock } from "../../components/TextBlock";
import List from "../../components/UI/List/List";
import { IConcept, ITranscribedText } from "../../utils/types";
import { ConceptItem } from "../../components/UI/Concept/ConceptItem";
import axios from "axios";

export const MainPage: React.FC = () => {
  const [text, setText] = useState({
    body: "Lorem ipsum dolor sit amet consectetur, adipisicing elit. Eum fugit cumque distinctio cum hic harum nostrum voluptatem, rem dolorum esse optio tenetur in rerum. In, recusandae expedita! Enim, reprehenderit. Officia!Lorem ipsum dolor sit amet consectetur, adipisicing elit. Eum fugit cumque distinctio cum hic harum nostrum voluptatem, rem dolorum esse optio tenetur in rerum. In, recusandae expedita! Enim, reprehenderit. Officia!Lorem ipsum dolor sit amet consectetur, adipisicing elit. Eum fugit cumque distinctio cum hic harum nostrum voluptatem, rem dolorum esse optio tenetur in rerum. In, recusandae expedita! Enim, reprehenderit. Officia!Lorem ipsum dolor sit amet consectetur, adipisicing elit. Eum fugit cumque distinctio cum hic harum nostrum voluptatem, rem dolorum esse optio tenetur in rerum. In, recusandae expedita! Enim, reprehenderit. Officia!",
  });

  const [conc, setConc] = useState([
    {
      id: 0,
      title: "Машина",
      body: "это что ваще такое",
    },
  ]);

  const [content, setContent] = useState<ITranscribedText[]>([]);
  const [isLoading, setIsLoading] = useState(false)

  const [par, setPar] = useState<ITranscribedText[]>([{
    id: 0,
    body:{
      part1:'part1',
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


  useEffect(() => {
    fetchPosts();
  }, []);

  async function fetchPosts() {
    try {
      setIsLoading(true);
      const response = await axios.get(
        window.location.origin + "/api/test/"
      );
      setContent(response.data);
      console.log(content);
      setIsLoading(false);
    } catch (e) {
      console.log(e);
    }
  }

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
    <div className="flex flex-col gap-8">
      <div className="flex gap-8 flex-row">
        <DropCard />
        <List
          items={conc}
          renderItem={(item) => <ConceptItem props={item} key={item.id} />}
        />
      </div>

      <List
        items={par}
        renderItem={(item) => <TextBlock props={item} key={item.id} />}
      />
    </div>
  );
};
