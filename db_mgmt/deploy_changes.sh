docker run --rm -v $(pwd)/CoresHubDB:/project mcr.microsoft.com/dotnet/sdk:8.0 \
    bash -c "cd /project && dotnet build CoresHubDB.sqlproj"

docker run --rm \
    -v "$(pwd)/CoresHubDB/bin/Debug:/dacpac" \
    mcr.microsoft.com/dotnet/sdk:8.0 \
    bash -c "dotnet tool install -g microsoft.sqlpackage && \
    /root/.dotnet/tools/sqlpackage \
    /Action:Publish \
    /SourceFile:/dacpac/CoresHubDB.dacpac \
    /TargetServerName:cpp-poly6-dev.database.usgovcloudapi.net,1433 \
    /TargetDatabaseName:DCAP \
    /TargetUser:cppazureuser \
    /TargetPassword:'VeryMuchSecure14!' \
    /TargetTrustServerCertificate:True"