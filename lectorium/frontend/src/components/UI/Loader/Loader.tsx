import React from 'react'
import styles from './Loader.module.scss'
import loader from '../../../assets/icons/loader.svg'

export const Loader:React.FC = () => {
  return (
    
    <div>
      <img className={styles.loader} src={loader} alt="" />
    </div>
      

    
    
  )
}
