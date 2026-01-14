# DB Migrations
Run EF Core migrations to create the database schema:
```
cd api
dotnet ef migrations add InitialCreate
dotnet ef database update
```