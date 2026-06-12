USE [Group_ID_13_DB]
GO

if object_id('date') is null
	CREATE TABLE [Group_ID_13].[date](
		[date_id] [int] NOT NULL,
		[date] [datetime] NOT NULL,
		[day] [int] NOT NULL,
		[month] [int] NOT NULL,
		[year] [int] NOT NULL,
		[quarter] [varchar](10) NOT NULL,
		[day_of_week] [varchar](20) NOT NULL, 
		CONSTRAINT [PK_date] PRIMARY KEY CLUSTERED ([date_id] ASC),
	);

if object_id('participant') is null
	CREATE TABLE [Group_ID_13].[participant](
		[participant_id] [varchar](20) NOT NULL, 
		[participant_age_group] [varchar](30) NOT NULL, 
		[participant_gender] [varchar](20) NOT NULL, 
		[participant_status] [varchar](20) NOT NULL, 
		[participant_type] [varchar](20) NOT NULL, 
		CONSTRAINT [PK_participant] PRIMARY KEY CLUSTERED ([participant_id] ASC),
	);

if object_id('gun') is null
	CREATE TABLE [Group_ID_13].[gun](
		[gun_id] [varchar](20) NOT NULL, 
		[gun_stolen] [varchar](30) NOT NULL, 
		[gun_type] [varchar](30) NOT NULL, 
		CONSTRAINT [PK_gun] PRIMARY KEY CLUSTERED ([gun_id] ASC),
	);

if object_id('incident') is null
	CREATE TABLE [Group_ID_13].[incident](
		[incident_id] [int] NOT NULL,
		CONSTRAINT [PK_incident] PRIMARY KEY CLUSTERED ([incident_id] ASC),
	);

if object_id('geography') is null
	CREATE TABLE [Group_ID_13].[geography](
		[geo_id] [varchar](20) NOT NULL, 
		[latitude] [float] NOT NULL,
		[longitude] [float] NOT NULL,
		[city] [varchar](50) NOT NULL, 
		[state] [varchar](50) NOT NULL, 
		[continent] [varchar](30) NOT NULL, 
		CONSTRAINT [PK_geography] PRIMARY KEY CLUSTERED ([geo_id] ASC),
	);

if object_id('custody') is null
	CREATE TABLE [Group_ID_13].[custody](
		[custody_id] [int] NOT NULL,
		[date_id] [int] NOT NULL,
		[participant_id] [varchar](20) NOT NULL, 
		[geo_id] [varchar](20) NOT NULL, 
		[crime_gravity] [int] NOT NULL,
		[incident_id] [int] NOT NULL,
		[gun_id] [varchar](20) NOT NULL,
		CONSTRAINT [PK_custody] PRIMARY KEY CLUSTERED ([custody_id] ASC),
	
		FOREIGN KEY ([date_id]) REFERENCES [Group_ID_13].[date]([date_id]),
		FOREIGN KEY ([participant_id]) REFERENCES [Group_ID_13].[participant]([participant_id]),
		FOREIGN KEY ([geo_id]) REFERENCES [Group_ID_13].[geography]([geo_id]),
		FOREIGN KEY ([gun_id]) REFERENCES [Group_ID_13].[gun]([gun_id]),
		FOREIGN KEY ([incident_id]) REFERENCES [Group_ID_13].[incident]([incident_id])
	);







