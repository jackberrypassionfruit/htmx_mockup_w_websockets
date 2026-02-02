
CREATE PROCEDURE [dbo].[MoveSerializeTransact] 
	@job_number NVARCHAR(20),
	@page NVARCHAR(20),
	@sub_process NVARCHAR(20),
	@eng_toggle BIT,
	@mrb_toggle BIT,
	@css_toggle BIT,
	@current_user NVARCHAR(100)
AS


SET XACT_ABORT ON
SET NOCOUNT ON

DECLARE 
	@next_sequential_sub_routing NVARCHAR(20),
	@next_initial_sub_routing NVARCHAR(20),
	@next_process_step NVARCHAR(20),
	@current_site_location NVARCHAR(20),
	@hold_location NVARCHAR(20),
	@next_process_step_hold NVARCHAR(20),
	@this_process_tablename NVARCHAR(100),
	@next_process_tablename NVARCHAR(100)


/*
TESTING

SET		@job_number = '6168339';
SET		@page = 'serialize';
SET		@sub_process = '';
SET		@eng_toggle = 0;
SET		@mrb_toggle = 0;
SET		@css_toggle = 0;
SET		@current_user = 'jack.pashayan@poly6.com';
*/

DROP TABLE IF EXISTS #process_tablename_mappings;
CREATE TABLE #process_tablename_mappings (
    [process_step_name] NVARCHAR(100) NULL,
    [db_table] NVARCHAR(100) NULL,
    [db_details_table] NVARCHAR(100) NULL
);

INSERT INTO #process_tablename_mappings
VALUES
( 'Injection',            'Cores2.Injection.Master' ,       'Cores2.Injection.Details' ),
( 'Cure',                 'Cores2.Cure.Master' ,            'Cores2.Cure.Details' ),
( 'Dissolution & Dry',    'Cores2.Dissolution.Master' ,     'Cores2.Dissolution.Details' ),
( 'Serialize',            'Cores2.Serialize.Master' ,       'Cores2.Serialize.Details' ),
( 'CT Scan',              'Cores2.Dimensional.Master' ,     'Cores2.Dimensional.Details' ),
( 'Low Fire Cycle',       'Cores2.Fire.Master' ,            'Cores2.Fire.Details' ),
( 'High Fire Cycle',      'Cores2.Fire.Master' ,            'Cores2.Fire.Details' ),
( 'Fire Cycle',           'Cores2.Fire.Master' ,            'Cores2.Fire.Details' ),
( 'Visual Inspection',    'Cores2.Inspection.Master' ,      'Cores2.Inspection.Details' ),
( 'Sort',                 'Cores2.Inspection.Master' ,      'Cores2.Inspection.Details' ),
( 'Patch',                'Cores2.Patch.Master' ,           'Cores2.Patch.Details' ),
( 'Low Fire Patch',       'Cores2.Patch.Master' ,           'Cores2.Patch.Details' ),
( 'High Fire Patch',      'Cores2.Patch.Master' ,           'Cores2.Patch.Details' ),
( 'CMM',                  'Cores2.CMM.Master' ,             'Cores2.CMM.Details' )

--SELECT * FROM #process_tablename_mappings

--DROP TABLE IF EXISTS #routings_this_job;
--CREATE TABLE #routings_this_job (
--    [process_step_name] NVARCHAR(20) NULL,
--    [process_step_num] SMALLINT NULL,
--	[process_state] NVARCHAR(20),
--	[part_number] NVARCHAR(20)
--);


--INSERT INTO #routings_this_job
--SELECT
--	[process_step_name],
--	[process_step_num],
--	[process_state],
--	[part_number]
--FROM [VW.Configuration.Routings_Max_Revision] AS a
--WHERE EXISTS (
--	SELECT * FROM [Cores2.Master.Details] AS x
--	WHERE	a.configuration_id = x.configuration_id
--	AND		x.job_number = @job_number
--)

DROP TABLE IF EXISTS #current_process;
CREATE TABLE #current_process (
    [configuration_id] SMALLINT,
	[process_step_name] NVARCHAR(20) NULL,
    [process_step_num] SMALLINT NULL,
	[process_state] NVARCHAR(20),
	[part_number] NVARCHAR(20)
);

INSERT INTO #current_process
SELECT
	[configuration_id],
	[process_step_name],
	[process_step_num],
	[process_state],
	[part_number]
FROM [VW.Configuration.Routings_Max_Revision] AS a
WHERE EXISTS (
	SELECT * FROM [Cores2.Master.Details] AS x
	WHERE	a.configuration_id = x.configuration_id
	AND		a.process_step_num = x.process_step_num
	AND		x.job_number = @job_number
	AND		x.location <> 'Scrap'
)

DROP TABLE IF EXISTS #next_process;
CREATE TABLE #next_process (
    [configuration_id] SMALLINT,
    [process_step_name] NVARCHAR(20) NULL,
    [process_step_num] SMALLINT NULL,
	[process_state] NVARCHAR(20),
	[part_number] NVARCHAR(20)
);

INSERT INTO #next_process
SELECT
	[configuration_id],
	[process_step_name],
	[process_step_num],
	[process_state],
	[part_number]
FROM [VW.Configuration.Routings_Max_Revision] AS a
WHERE EXISTS (
	SELECT * FROM [Cores2.Master.Details] AS x
	WHERE	a.configuration_id = x.configuration_id
	AND		a.process_step_num = x.process_step_num + 1
	AND		x.job_number = @job_number
	AND		x.location <> 'Scrap'
)

--SELECT * FROM #next_process
--ORDER BY process_step_num


SET @next_process_step_hold = 
	COALESCE(
		(
			SELECT TOP(1) [process_step_name]
			FROM [VW.Configuration.Routings_Max_Revision] AS a
			WHERE EXISTS (
				SELECT * FROM [Cores2.Master.Details] AS x
				WHERE	a.configuration_id = x.configuration_id
				AND		a.process_step_num = x.process_step_num + 2
				AND		x.job_number = @job_number
				AND		x.location <> 'Scrap'
			)
		),
		'Scrap'
	)

--PRINT @next_process_step_hold

DROP TABLE IF EXISTS #active_parts;
CREATE TABLE #active_parts (
    [part_id] NVARCHAR(20) NOT NULL,
    [pk_id] INT NULL,
	[configuration_id] SMALLINT,
	[process_step_num] SMALLINT,
	[process_state] NVARCHAR(20),
	[job_number] NVARCHAR(20),
	--[run_number] SMALLINT
	[master_pk_id] INT NOT NULL
);

INSERT INTO #active_parts
SELECT
    a.[part_id],
    a.[pk_id],
	a.[configuration_id],
	a.[process_step_num],
	b.[process_state],
	a.[job_number]
	-- This section and below is not dynamic
	--COALESCE(a.[run_number], 1) AS run_number
	,c.pk_id AS master_pk_id
FROM [Cores2.Serialize.Master] AS a
JOIN #current_process AS b
ON 1=1
JOIN [Cores2.Master.Details] AS c
ON a.part_id = c.part_id
WHERE a.job_number = @job_number
AND a.scrapped IS NULL

--SELECT * FROM #active_parts

-- These both only implicitely apply for Sort/Inspection
-- Would have to extend logic if reproduced
SET @next_sequential_sub_routing =
(
	SELECT TOP(1) sub_process
	FROM	[VW.Configuration.Ref.Sub_Routings.Max_Rev]
	WHERE	process_state = (SELECT TOP(1) process_state FROM #current_process)
	AND		part_number =	(SELECT TOP(1) part_number	 FROM #current_process)
	AND sequence_number = 
	(
		SELECT TOP(1) sequence_number + 1
		FROM	[VW.Configuration.Ref.Sub_Routings.Max_Rev]
		WHERE	process_state = (SELECT TOP(1) process_state FROM #current_process)
		AND		part_number =	(SELECT TOP(1) part_number   FROM #current_process)
		AND		sub_process = @sub_process
	)
)


SET @next_initial_sub_routing =
(
	SELECT TOP(1) sub_process
	FROM	[VW.Configuration.Ref.Sub_Routings.Max_Rev]
	WHERE	process_state = (SELECT TOP(1) process_state FROM #next_process)
	AND		part_number =	(SELECT TOP(1) part_number	 FROM #next_process)
	AND		sequence_number = 1
	----	This line line is a hack, because Sort is the only step with sub_processes right now
	AND		@next_process_step = 'Sort'
)


-- PRINT @next_sequential_sub_routing
-- PRINT @next_initial_sub_routing

SET @next_process_step = COALESCE(
	( SELECT TOP(1) process_step_name FROM #next_process ),
	'Scrap'
)

--PRINT @next_process_step


DROP TABLE IF EXISTS #selected_parameters;
CREATE TABLE #selected_parameters (
    [process_step_name] NVARCHAR(20) NULL,
	[process_state] NVARCHAR(20),
	[part_number] NVARCHAR(20),
	[attribute] NVARCHAR(100),
	[value] NVARCHAR(MAX)
);

INSERT INTO #selected_parameters
SELECT 
	[process_step_name],
	[process_state],
	[part_number],
	[attribute],
	[value]
FROM [VW.Configuration.Process_Parameters_Max_Revision] AS a
WHERE EXISTS (
	SELECT * FROM #current_process AS x
	WHERE a.configuration_id = x.configuration_id
	AND a.process_step_num = x.process_step_num
)

--SELECT * FROM #selected_parameters
--ORDER BY attribute


SET @current_site_location =
(
	SELECT TOP(1)
		current_location
	FROM [VW.Cores2.Site_Location.Current_By_Job]
	WHERE job_number = @job_number
)

--PRINT @current_site_location

SET @hold_location = 
CASE
	WHEN @eng_toggle = 1 AND @next_sequential_sub_routing IS NULL
		THEN 'Eng Review'
	WHEN @mrb_toggle = 1
		THEN 'MRB'
	WHEN @css_toggle = 1
		THEN 'CSS'
	ELSE NULL
END

--PRINT @hold_location


SET @this_process_tablename = 
(
	SELEcT TOP(1) db_table FROM #process_tablename_mappings
	WHERE process_step_name = ( SELECT TOP(1) process_step_name FROM #current_process )
)

SET @next_process_tablename = 
(
	SELEcT TOP(1) db_table FROM #process_tablename_mappings
	WHERE process_step_name = ( SELECT TOP(1) process_step_name FROM #next_process )
)
/*
	TODO - following UI update
	parts_for_mrb_selected
*/

/*
AND THEN THE PAYLOADS
*/

-- UPDATE current process_table
DROP TABLE IF EXISTS #this_process_move_update_master;
CREATE TABLE #this_process_move_update_master (
    [pk_id] INT NOT NULL,
	[part_id] NVARCHAR(20),
	[start_operator] NVARCHAR(50),
	[start_datetime] DATETIME2(7),
	[end_operator] NVARCHAR(50),
	[end_datetime] DATETIME2(7),
	[scrapped] NVARCHAR(10),
	[modified_by] NVARCHAR(50),
	[modified_datetime] DATETIME2(7)
);

INSERT INTO #this_process_move_update_master
SELECT
	pk_id
	,part_id
	,@current_user AS start_operator
    ,GETDATE() AS start_datetime
    ,@current_user AS end_operator
    ,GETDATE() AS end_datetime
    ,IIF(
		@next_process_step = 'Scrap',
			'Yes',
		'No'
	) AS scrapped 
    ,@current_user AS modified_by
    ,GETDATE() AS modified_datetime
FROM #active_parts

--SELECT * FROM #this_process_move_update_master


-- INSERT [Cores2.Hold.Master]
DROP TABLE IF EXISTS #insert_hold_master;
CREATE TABLE #insert_hold_master (
    [process_pk_id] INT NOT NULL,
	[part_id] NVARCHAR(20),
	[configuration_id] SMALLINT,
	[job_number]  NVARCHAR(20),
	[run_number] SMALLINT,

	[hold_type] NVARCHAR(20),
	[location] NVARCHAR(20),
	[sub_location] NVARCHAR(20) NULL,
	[next_location] NVARCHAR(20),
	-- [next_sub_location] NVARCHAR(20)
	[process_step_num] SMALLINT,

	[scrapped] NVARCHAR(10),
	[created_by] NVARCHAR(50),
	[created_datetime] DATETIME2(7)
);


INSERT INTO #insert_hold_master
SELECT
	pk_id AS process_pk_id
	,part_id
	,configuration_id
	,job_number
	,1 AS run_number
	,@hold_location AS hold_type
	,( SELECT TOP(1) process_step_name FROM #current_process ) AS location
	,NULL AS [sub_location]
	,@next_process_step_hold AS next_location
	,process_step_num
    ,IIF(
		@next_process_step = 'Scrap',
			'Yes',
		'No'
	) AS scrapped 
    ,@current_user AS created_by
    ,GETDATE() AS created_datetime
FROM #active_parts
-- Only provide a payload if HOLD is the next location
WHERE @hold_location IS NOT NULL

--SELECT * FROM #insert_hold_master


-- INSERT [Cores2.Serialize.Details]
DROP TABLE IF EXISTS #this_process_insert_details;
CREATE TABLE #this_process_insert_details (
	[part_id] NVARCHAR(20),
	[process_step_num] SMALLINT,
	[attribute] NVARCHAR(50),
	[value] NVARCHAR(MAX),
	[created_by] NVARCHAR(50),
	[created_datetime] DATETIME2(7)
);


INSERT INTO #this_process_insert_details
SELECT
	part_id
	,process_step_num
    ,'Site Location' AS attribute
	,@current_site_location AS value
    ,@current_user AS created_by
    ,GETDATE() AS created_datetime
FROM #active_parts

--SELECT * FROM #this_process_insert_details


-- INSERT [Cores2.Dimensional.Master] (after adding columns)
DROP TABLE IF EXISTS #next_process_post_master;
CREATE TABLE #next_process_post_master (
	[part_id] NVARCHAR(20),
	[configuration_id] SMALLINT,
	[job_number]  NVARCHAR(20),
	[process_step_num] SMALLINT,
	[created_by] NVARCHAR(50),
	[created_datetime] DATETIME2(7)
);


INSERT INTO #next_process_post_master
SELECT
	part_id
	,configuration_id
	,job_number
	,process_step_num
    ,@current_user AS created_by
    ,GETDATE() AS created_datetime
FROM #active_parts
-- Do not provide a payload if HOLD is the next location
WHERE @hold_location IS NULL AND @next_sequential_sub_routing IS NULL

--SELECT * FROM #next_process_post_master


-- TODO - Add conditional columns if want to make this generalized
-- INSERT [Cores2.Serialize.Master] (if this were  table with sub_processes)
DROP TABLE IF EXISTS #next_sub_process_post_master;
CREATE TABLE #next_sub_process_post_master (
	[part_id] NVARCHAR(20),
	[configuration_id] SMALLINT,
	[job_number]  NVARCHAR(20),
	-- [run_number] SMALLINT,
	-- [process_state] NVARCHAR(50),
	-- [sub_process] NVARCHAR(50),
	[process_step_num] SMALLINT,
	[created_by] NVARCHAR(50),
	[created_datetime] DATETIME2(7)
);


INSERT INTO #next_sub_process_post_master
SELECT
	part_id
	,configuration_id
	,job_number
	-- ,1 AS run_number
	-- ,process_state
	-- ,@sub_process AS sub_process
	,process_step_num
    ,@current_user AS created_by
    ,GETDATE() AS created_datetime
FROM #active_parts
-- Do not provide a payload if HOLD is the next location
WHERE @hold_location IS NULL AND @next_sequential_sub_routing IS NOT NULL

--SELECT * FROM #next_sub_process_post_master


-- UPDATE [Cores2.Master.Details]
DROP TABLE IF EXISTS #update_master_details;
CREATE TABLE #update_master_details (
	[pk_id] INT,
	[part_id] NVARCHAR(20),
	[location] NVARCHAR(20),
	[sub_location] NVARCHAR(20) NULL,
	[process_step_num] SMALLINT,
	[scrap_step] NVARCHAR(20) NULL,
	[scrap_code] NVARCHAR(20) NULL,
	[scrap_operator] NVARCHAR(100) NULL,
	[scrap_notes] NVARCHAR(100) NULL,
	[scrap_time] DATETIME2(7) NULL,
	[modified_by] NVARCHAR(50),
	[modified_datetime] DATETIME2(7)
);

INSERT INTO #update_master_details
SELECT
	[master_pk_id] AS pk_id
	,[part_id]
	,CASE	
		WHEN @next_process_step = 'Scrap'
			THEN 'Scrap'
		WHEN @next_initial_sub_routing IS NOT NULL
			THEN (SELECT TOP(1) process_step_name FROM #current_process)
		ELSE
			IIF(
				@hold_location IS NULL,
					@next_process_step,
				IIF(
					(SELECT TOP(1) process_state FROM #next_process) = 'Final',
						'Visual Inspection',
					'Sort'
				)
			)
	END AS location
	,CASE
		WHEN @next_process_step = 'Scrap'
			THEN NULL
		WHEN @next_initial_sub_routing IS NOT NULL
			THEN @next_initial_sub_routing
		ELSE COALESCE(
				@hold_location,
				IIF(
					(SELECT TOP(1) process_step_name FROM #next_process) LIKE '%Patch',
						'Patch & Finish',
					NULL
				)
			)
	END AS sub_location
	,CASE
		WHEN @next_process_step = 'Scrap' OR @next_initial_sub_routing IS NOT NULL
			THEN process_step_num
		ELSE IIF(
				@hold_location IS NULL OR 
				(SELECT TOP(1) process_step_name FROM #next_process) IN ('Eng Review', 'CSS'),
					(SELECT TOP(1) process_step_num FROM #next_process),
				(SELECT TOP(1) process_step_num FROM #current_process)
			)
	END AS process_step_num
	,IIF(
		@next_process_step = 'Scrap', 
			(SELECT TOP(1) process_step_name FROM #current_process),
		NULL
	) AS scrap_step
	,IIF(
		@next_process_step = 'Scrap', 
			'PLY062',
		NULL
	) AS scrap_code
	,IIF(
		@next_process_step = 'Scrap', 
			@current_user,
		NULL
	) AS scrap_operator
	,IIF(
		@next_process_step = 'Scrap', 
			'Routing completed for Engineering Trial',
		NULL
	) AS scrap_notes
	,IIF(
		@next_process_step = 'Scrap', 
			GETDATE(),
		NULL
	) AS scrap_time

    ,@current_user AS created_by
    ,GETDATE() AS created_datetime
FROM #active_parts


--SELECT * FROM #update_master_details



-- INSERT [Cores2.Master.Changelog]
DROP TABLE IF EXISTS #insert_changelog;
CREATE TABLE #insert_changelog (
	[part_id] NVARCHAR(20),
	[configuration_id] SMALLINT,
	[job_number]  NVARCHAR(20),
	[run_number] SMALLINT,
	[operator] NVARCHAR(50),
	[transaction_type] NVARCHAR(50),
	[transaction_time] DATETIME2(7),
	[from_process_step_num] SMALLINT,
	[to_process_step_num] SMALLINT,
	[from_location] NVARCHAR(50),
	[to_location] NVARCHAR(50),
	[transaction_details] NVARCHAR(500),
	[app_version] NVARCHAR(50),
	[notes] NVARCHAR(500),
	[created_by] NVARCHAR(50),
	[created_datetime] DATETIME2(7)
);


INSERT INTO #insert_changelog
SELECT
	part_id
	,configuration_id
	,job_number
	,1 AS run_number
	,@current_user AS operator
	,'Move' AS [transaction_type]
	,GETDATE() AS transaction_time
	,process_step_num AS from_process_step_num
	,CASE
		WHEN @next_initial_sub_routing IS NOT NULL
			THEN (SELECT TOP(1) process_step_name FROM #current_process)
		WHEN @hold_location IS NULL OR (SELECT TOP(1) process_step_name FROM #next_process) IN ('Eng Review', 'CSS')
			THEN (SELECT TOP(1) process_step_num FROM #next_process)
		ELSE (SELECT TOP(1) process_step_num FROM #current_process)
	END AS to_process_step_num
	,(SELECT TOP(1) process_step_name FROM #current_process) AS from_location
	,IIF(
		@hold_location IS NULL,
			@next_process_step,
		(SELECT TOP(1) process_step_name FROM #current_process)
	) AS to_location
	,IIF(
		@next_initial_sub_routing IS NOT NULL,
			-- got lazy and didn't say from substep, since I am not caching that here
			'Moved to '+@next_initial_sub_routing,
		'Moved from '+(SELECT TOP(1) process_step_name FROM #current_process)
			+' to '+COALESCE(@hold_location, @next_process_step)
	) AS transaction_details
	,'1.0.0' AS app_version
	,'No Notes' AS [notes]
    ,@current_user AS created_by
    ,GETDATE() AS created_datetime
FROM #active_parts

SELECT * FROM #insert_changelog

/*
	TODO - following UI update
	parts_for_selection_inspection
*/

/*
NOW MAKE CHANGES
*/

BEGIN TRANSACTION;

BEGIN TRY

	UPDATE a
	SET
		a.[part_id] = b.[part_id],
		a.[start_operator] = b.[start_operator],
		a.[start_datetime] = b.[start_datetime],
		a.[end_operator] = b.[end_operator],
		a.[end_datetime] = b.[end_datetime],
		a.[scrapped] = b.[scrapped],
		a.[modified_by] = b.[modified_by],
		a.[modified_datetime] = b.[modified_datetime]
	FROM [Cores2.Serialize.Master] AS a
	JOIN #this_process_move_update_master AS b
	ON a.pk_id = b.pk_id


	INSERT INTO [Cores2.Hold.Master]
	(
		[process_pk_id],
		[part_id],
		[configuration_id],
		[job_number],
		[run_number],
		[hold_type],
		[location],
		[sub_location],
		[next_location],
		[process_step_num],
		[scrapped],
		[created_by],
		[created_datetime]
	)
	SELECT * FROM #insert_hold_master


	INSERT INTO [Cores2.Serialize.Details]
	(
		[part_id],
		[process_step_num],
		[attribute],
		[value],
		[created_by],
		[created_datetime] 
	)
	SELECT * FROM #this_process_insert_details


	INSERT [Cores2.Dimensional.Master]
	(
		[part_id],
		[configuration_id],
		[job_number],
		[process_step_num],
		[created_by],
		[created_datetime]
	)
	SELECT * FROM #next_process_post_master


	INSERT [Cores2.Serialize.Master]
	(
		[part_id],
		[configuration_id],
		[job_number],
		--[run_number],
		--[process_state],
		--[sub_process],
		[process_step_num],
		[created_by],
		[created_datetime]
	)
	SELECT * FROM #next_sub_process_post_master


	UPDATE a
	SET
		a.[part_id] = b.[part_id],
		a.[location] = b.[location],
		a.[sub_location] = b.[sub_location],
		a.[process_step_num] = b.[process_step_num], 
		a.[scrap_step] = b.[scrap_step],
		a.[scrap_code] = b.[scrap_code],  
		a.[scrap_operator] = b.[scrap_operator], 
		a.[scrap_notes] = b.[scrap_notes], 
		a.[scrap_time] = b.[scrap_time], 
		a.[modified_by] = b.[modified_by], 
		a.[modified_datetime] = b.[modified_datetime]
	FROM [Cores2.Master.Details] AS a
	JOIN #update_master_details AS b
	ON a.pk_id = b.pk_id


	INSERT [Cores2.Master.Changelog]
	(
		[part_id],
		[configuration_id],
		[job_number],
		[run_number],
		[operator],
		[transaction_type],
		[transaction_time],
		[from_process_step_num],
		[to_process_step_num],
		[from_location],
		[to_location],
		[transaction_details],
		[app_version],
		[notes],
		[created_by],
		[created_datetime]
	)
	SELECT * FROM #insert_changelog

	/*
		TODO - following UI update
		"Poly6.Part_Selection_Ref"
	*/

	
	COMMIT;
	

END TRY
	BEGIN CATCH;
		IF @@trancount > 0
			ROLLBACK;
		THROW;
	END CATCH;