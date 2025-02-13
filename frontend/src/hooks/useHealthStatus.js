// Cache the promise to avoid creating a new one on every render
let healthPromise = null

export function useHealthStatus() {
  if (!healthPromise) {
    healthPromise = fetchHealthStatus()
  }
  return healthPromise
}

async function fetchHealthStatus() {
  try {
    const response = await fetch(`${import.meta.env.VITE_API_URL}/api/health`)
    if (!response.ok) throw new Error('Health check failed')
    const data = await response.json()
    return data
  } catch (error) {
    console.error('Fetch error:', error)
    throw error
  }
}
