docker build -t veneur:build -f dockerfile.build .
docker run --name veneurbuild veneur:build go
docker cp veneur:build:/build/veneur ./veneur
