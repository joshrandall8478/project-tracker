using Microsoft.AspNetCore.Mvc;

namespace Backend.Controllers;

[ApiController]
[Route("api/[controller]")]
public class ProjectsController : ControllerBase
{
    private static readonly List<Project> Projects = new()
    {
        new Project { Id = 1, Name = "Sample Project 1", Description = "A sample project", Status = "Active" },
        new Project { Id = 2, Name = "Sample Project 2", Description = "Another sample project", Status = "Completed" }
    };

    [HttpGet]
    public ActionResult<IEnumerable<Project>> GetAll()
    {
        return Ok(Projects);
    }

    [HttpGet("{id}")]
    public ActionResult<Project> GetById(int id)
    {
        var project = Projects.FirstOrDefault(p => p.Id == id);
        if (project == null)
        {
            return NotFound();
        }
        return Ok(project);
    }

    [HttpPost]
    public ActionResult<Project> Create(Project project)
    {
        project.Id = Projects.Max(p => p.Id) + 1;
        Projects.Add(project);
        return CreatedAtAction(nameof(GetById), new { id = project.Id }, project);
    }
}

public class Project
{
    public int Id { get; set; }
    public string Name { get; set; } = string.Empty;
    public string Description { get; set; } = string.Empty;
    public string Status { get; set; } = string.Empty;
}
