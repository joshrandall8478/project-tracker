# project-tracker
Simple Task &amp; Project Tracker

## Tech Stack

- **Backend**: C# Web API (.NET 10.0)
- **Frontend**: TypeScript React with Vite

## Project Structure

```
project-tracker/
├── Backend/           # C# Web API backend
│   ├── Controllers/   # API controllers
│   ├── Program.cs     # Application entry point
│   └── appsettings.json
└── frontend/          # React TypeScript frontend
    ├── src/
    │   ├── services/  # API service layer
    │   └── App.tsx    # Main application component
    └── vite.config.ts
```

## Getting Started

### Prerequisites

- .NET 10.0 SDK or later
- Node.js 20.x or later
- npm 10.x or later

### Running the Backend

1. Navigate to the Backend directory:
   ```bash
   cd Backend
   ```

2. Restore dependencies (if needed):
   ```bash
   dotnet restore
   ```

3. Run the API:
   ```bash
   dotnet run
   ```

The API will be available at `http://localhost:5000`

### Running the Frontend

1. Navigate to the frontend directory:
   ```bash
   cd frontend
   ```

2. Install dependencies (if needed):
   ```bash
   npm install
   ```

3. Run the development server:
   ```bash
   npm run dev
   ```

The frontend will be available at `http://localhost:5173`

### Building for Production

**Backend:**
```bash
cd Backend
dotnet build -c Release
```

**Frontend:**
```bash
cd frontend
npm run build
```

## API Endpoints

### Projects

- `GET /api/projects` - Get all projects
- `GET /api/projects/{id}` - Get a project by ID
- `POST /api/projects` - Create a new project

### Weather Forecast (Sample)

- `GET /weatherforecast` - Get weather forecast data

## Features

- RESTful API with C# Web API
- CORS enabled for frontend-backend communication
- TypeScript for type-safe frontend code
- Modern React with hooks
- Vite for fast development and builds
- Sample project CRUD operations
