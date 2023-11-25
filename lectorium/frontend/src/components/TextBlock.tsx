import React from 'react'
import { ITranscribedText } from '../utils/types'
import styles from './Transcribation.module.scss'
import { Button, ButtonVariant } from './UI/Button/Button';

interface TextBlockProps {
  props: ITranscribedText;
}



const transcribeText = (e:React.MouseEvent) => {
  e.preventDefault()

}
export const TextBlock:React.FC<TextBlockProps> = ({props}) => {
  return (
    <div className={styles.transcribation}>
      <div className={styles.transcribation__text}>
        {props.body.part1 
        ?<div className={styles.transcribation__wrapper}>
          <p className={styles.transcribation__p1}>{props.body.part1}</p>
          <p className={styles.transcribation__p2}>{props.body.part2}</p>
          <p className={styles.transcribation__p3}>{props.body.part3}</p>
          <p className={styles.transcribation__p4}>{props.body.part4}</p>
        </div>
        : <p className={styles.transcribation__desc}>Здесь появится ваша транскрипция</p>
        }
        
        <Button onClick={transcribeText} title='Скачать термины' variant={ButtonVariant.primary} />
      </div>
      
    </div>
  )
}
