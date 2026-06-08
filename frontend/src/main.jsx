import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import './assets/index.css'
import SimpleLanding from './pages/SimpleLanding'

createRoot(document.getElementById('root')).render(
  <StrictMode>
    <SimpleLanding />
  </StrictMode>,
)
