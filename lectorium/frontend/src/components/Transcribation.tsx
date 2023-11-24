import React from 'react'
import { ITransribedText } from '../utils/types'
import styles from './Transcribation.module.scss'
import { Button, ButtonVariant } from './UI/Button/Button';

interface TextBlockProps {
  props: ITransribedText;
}

export const TextBlock:React.FC<TextBlockProps> = ({props}) => {
  return (
    <div className={styles.transcribation}>
      <div className={styles.transcribation__text}>
        <p >{props.body}</p>
        <Button title='Скачать' variant={ButtonVariant.primary}/>
      </div>
      
    </div>
  )
}
