CREATE TABLE [dbo].[Login](
	[id] [int] IDENTITY(1,1) NOT NULL,
	[nombre] [varchar](50) NULL,
	[usuario] [varchar](50) NULL,
	[password] [varchar](50) NULL,
 CONSTRAINT [PK_Login] PRIMARY KEY CLUSTERED 
(
	[id] ASC
)


insert into (nombre, usuario, password) values ('Darwin', 'dr@gmai', '1234')