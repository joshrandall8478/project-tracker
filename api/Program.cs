using api.Data;
using Microsoft.EntityFrameworkCore;

var builder = WebApplication.CreateBuilder(args);

// Add services to the container.
// Learn more about configuring OpenAPI at https://aka.ms/aspnet/openapi





builder.Services.AddControllers();
builder.Services.AddEndpointsApiExplorer();


// Allow vite within CORS
// builder.Services.AddCors(options =>
// {
//     options.AddPolicy("AllowVite",
//         policy =>
//         {
//             policy.WithOrigins("http://localhost:5173")
//                   .AllowAnyHeader()
//                   .AllowAnyMethod();
//         });
// });
builder.Services.AddDbContext<ApplicationDBContext>(options =>
{
   options.UseMySql(
    builder.Configuration.GetConnectionString("DefaultConnection"),
    ServerVersion.AutoDetect(builder.Configuration.GetConnectionString("DefaultConnection"))
   ); 
});

var app = builder.Build();

// Configure the HTTP request pipeline.
if (app.Environment.IsDevelopment())
{
    app.MapOpenApi();
}

// app.UseHttpsRedirection();

// app.UseCors("AllowVite");


app.Run();

