#!/bin/bash

# Path to your .csproj file
PROJECT_FILE="./ClassLibrary1.csproj"

# Read each line in packages.txt and add the package
while IFS= read -r package
do
  dotnet add "$PROJECT_FILE" package "$package"
done < "packages.txt"

