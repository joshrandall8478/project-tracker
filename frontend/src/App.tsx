import { useState, useEffect } from 'react'
import './App.css'
import { projectService, type Project } from './services/api'

function App() {
  const [projects, setProjects] = useState<Project[]>([])
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState<string | null>(null)

  useEffect(() => {
    loadProjects()
  }, [])

  const loadProjects = async () => {
    try {
      setLoading(true)
      setError(null)
      const data = await projectService.getAll()
      setProjects(data)
    } catch (err) {
      setError(err instanceof Error ? err.message : 'Failed to load projects')
    } finally {
      setLoading(false)
    }
  }

  return (
    <>
      <h1>Project Tracker</h1>
      <div className="card">
        {loading && <p>Loading projects...</p>}
        {error && <p style={{ color: 'red' }}>Error: {error}</p>}
        {!loading && !error && (
          <div>
            <h2>Projects</h2>
            {projects.length === 0 ? (
              <p>No projects found.</p>
            ) : (
              <ul style={{ textAlign: 'left', maxWidth: '600px', margin: '0 auto' }}>
                {projects.map((project) => (
                  <li key={project.id} style={{ marginBottom: '1em' }}>
                    <strong>{project.name}</strong> - {project.status}
                    <br />
                    <small>{project.description}</small>
                  </li>
                ))}
              </ul>
            )}
          </div>
        )}
      </div>
      <p className="read-the-docs">
        C# Web API Backend + TypeScript React Frontend
      </p>
    </>
  )
}

export default App
