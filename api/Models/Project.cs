public class Project
{
    public int Id { get; set; }
    public string Name { get; set; } = string.Empty;

    public int UserId { get; set; }

    // // Navigation properties
    // public User User { get; set; } = null!;
    // public ICollection<Task> Tasks { get; set; } = new List<Task>();
}