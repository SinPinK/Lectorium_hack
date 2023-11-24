import React from 'react'

type ListProps<T> = {
  items: T[],
  renderItem: (item: T) => React.ReactNode
}

export default function List<T>(props:ListProps<T>) {
  return(
    <div className='bg-white rounded-20 overflow-y-auto w-full max-h-card'>
      {props.items.map(props.renderItem)}
    </div>
  )
  
}
