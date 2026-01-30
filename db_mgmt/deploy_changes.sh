docker run --rm -v $(pwd)/CoresHubDB:/project mcr.microsoft.com/dotnet/sdk:8.0 \
    bash -c "cd /project && dotnet build CoresHubDB.sqlproj"

~/sqlpackage/sqlpackage /Action:Publish \
    /SourceFile:CoresHubDB/bin/Debug/CoresHubDB.dacpac \
    /TargetServerName:192.168.2.108,1433 \
    /TargetDatabaseName:master \
    /TargetUser:sa \
    /TargetPassword:VeryMuchSecure14\! \
    /TargetTrustServerCertificate:True