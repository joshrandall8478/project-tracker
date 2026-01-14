using Microsoft.AspNetCore.Identity;
using api.Dtos.UserDto;
namespace api.Mappers
{
    public static class UserMappers
    {
        public static UserDto ToUserDto(this User userModel)
        {
            return new UserDto
            {
              Id = userModel.Id,
              Username = userModel.Username,
            //   PasswordHash = userModel.PasswordHash 
            };
        }
    }
}