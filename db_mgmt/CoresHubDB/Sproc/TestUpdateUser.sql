CREATE PROCEDURE [dbo].[TestUpdateUser]
  @job_number nvarchar(20)
AS

SET NOCOUNT ON


DROP TABLE IF EXISTS #return_table;
CREATE TABLE #return_table
(
  pk_id INT NULL,
  [part_id] NVARCHAR(20) NULL,
  [job_number] NVARCHAR(20) NULL,
  [end_operator] NVARCHAR(20) NULL,
  [end_datetime] DATETIME2 NULL
);

UPDATE a
  SET a.end_operator = 'Jack Pashayan'
  -- FROM master.dbo.core_serializemaster AS a
  FROM [Cores2.Serialize.Master] As a
  WHERE a.job_number = @job_number;

INSERT INTO #return_table
SELECT
  cs.pk_id, cs.part_id, cs.job_number, cs.end_operator, cs.end_datetime
-- FROM core_serializemaster cs
FROM [Cores2.Serialize.Master] AS cs
WHERE cs.job_number = @job_number

SELECT *
FROM #return_table
