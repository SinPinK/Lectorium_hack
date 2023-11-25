export interface IParagraph {
  part1: string,
  part2: string,
  part3: string,
  part4: string;
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

