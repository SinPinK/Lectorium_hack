export interface IParagraph {
  part1: string,
  part2: string,
  part3: string,
  part4: string,
  part5: string,
  part6: string,
  part7: string,
  part8: string,
  part9: string,
  part10: string,
  part11: string;
}

export interface ITranscribedText {
  body: IParagraph;
  id?: number;
}

export interface IConcept {
  id: number;
  title: string;
  body: string;
}

