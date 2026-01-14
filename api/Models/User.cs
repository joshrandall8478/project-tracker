using Microsoft.EntityFrameworkCore.Query;

public class User
{
    // Properties of tables
    public int Id { get; set; }
    public string Username { get; set; }
    public string PasswordHash { get; set; }
    
    
    // Navigation Properties
    // public ICollection<Project> Projects { get; set; } = new List<Project>();

}