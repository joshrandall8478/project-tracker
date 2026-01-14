public enum Progress
{
    NotStarted, // 0
    InProgress, // 1
    Complete // 2
}
public class Task
{
    public int Id { get; set; }
    public string Ittle { get; set; } = string.Empty;

    public Progress Progress { get; set; } = 0;
    public DateTime CreatedAt { get; set; } = DateTime.UtcNow;
    // Foreign key
    public int ProjectId { get; set; }

    // // Navigation property
    // public Project Project { get; set; } = null!; 
}