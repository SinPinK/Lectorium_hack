import React from 'react'
import styles from './Button.module.scss'

export enum ButtonVariant {
  primary = 'primary',
  secondary = 'secondary'
}

type ButtonProps = {
  title: string,
  type?: 'button' | 'submit' | 'reset' | undefined,
  variant: ButtonVariant;
  disabled?: boolean;
  onClick?: (e: React.MouseEvent) => void
}



export const Button:React.FC<ButtonProps> = ({title, type, disabled, variant, onClick}) => {
  return (
    <button onClick={onClick} type={type} disabled={disabled} className={variant === ButtonVariant.primary ? styles.primary : styles.secondary}>
      {title}
    </button>
  )
}
