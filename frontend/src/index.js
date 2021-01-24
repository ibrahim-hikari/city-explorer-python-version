import React from 'react'
import ReactDOM from 'react-dom'

import App from './components/app'

function Main(props) {
    return (
        <App />
    )
}

const root = document.getElementById('root')
ReactDOM.render(<Main/>, root)