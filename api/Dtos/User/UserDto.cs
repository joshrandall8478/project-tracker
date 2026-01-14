using Microsoft.EntityFrameworkCore.Query;

namespace api.Dtos.UserDto;
public class UserDto
{
    // Properties of tables
    public int Id { get; set; }
    public string Username { get; set; }
    
    
    // Navigation Properties
    // public ICollection<Project> Projects { get; set; } = new List<Project>();

}