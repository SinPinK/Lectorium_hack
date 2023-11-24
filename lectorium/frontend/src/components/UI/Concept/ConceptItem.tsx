import React from 'react'
import { IConcept } from '../../../utils/types'
import styles from './ConceptItem.module.scss'

interface ConceptItemProps {
  props: IConcept;
}

export const ConceptItem:React.FC<ConceptItemProps> = ({props}) => {
  return (
    <div className={styles.concept}>
      <h2>{props.id}.{props.title}</h2>
      <p>{props.body}</p>
    </div>
  )
}
