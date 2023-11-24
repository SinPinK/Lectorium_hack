import React from 'react'
import { ITranscribedText } from '../utils/types'
import styles from './Transcribation.module.scss'
import { Button, ButtonVariant } from './UI/Button/Button';

interface TextBlockProps {
  props: ITranscribedText;
}

export const TextBlock:React.FC<TextBlockProps> = ({props}) => {
  return (
    <div className={styles.transcribation}>
      <div className={styles.transcribation__text}>
        <p >{props.body.part1}</p>
        <Button title='Скачать' variant={ButtonVariant.primary}/>
      </div>
      
    </div>
  )
}
