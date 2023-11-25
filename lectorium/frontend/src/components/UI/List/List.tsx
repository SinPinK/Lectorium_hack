import React from 'react'

type ListProps<T> = {
  items: T[],
  renderItem: (item: T) => React.ReactNode
  variant: ListVariant;
}

export enum ListVariant {
  card = "card",
  list = 'list'
}

export default function List<T>(props:ListProps<T>, variant:ListVariant) {
  return(
    <div className={variant === ListVariant.card ? 'bg-white rounded-20 overflow-y-auto w-full max-h-card'
    :'bg-white rounded-20 w-full '
    }>
      {props.items.map(props.renderItem)}
    </div>
  )
  
}
