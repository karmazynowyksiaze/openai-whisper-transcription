data "aws_region" "current" {}

resource "aws_vpc" "cluepr_poc_vpc" {
  cidr_block           = "10.0.0.0/16"
  enable_dns_hostnames = true

  tags = {
    Name = "cluepr_poc VPC"
  }
}

resource "aws_internet_gateway" "cluepr_poc_gateway" {
  vpc_id = aws_vpc.cluepr_poc_vpc.id

  tags = {
    Name = "cluepr_poc IGW"
  }
}

resource "aws_subnet" "cluepr_poc_public_subnet" {
  vpc_id            = aws_vpc.cluepr_poc_vpc.id
  cidr_block        = "10.0.0.0/24"
  availability_zone = "eu-north-1a"

  tags = {
    Name = "cluepr_poc Public Subnet"
  }
}

resource "aws_route_table" "cluepr_poc_route_table" {
  vpc_id = aws_vpc.cluepr_poc_vpc.id

  route {
    cidr_block = "0.0.0.0/0"
    gateway_id = aws_internet_gateway.cluepr_poc_gateway.id
  }

  tags = {
    Name = "cluepr_poc Public Route Table"
  }
}
resource "aws_route_table_association" "cluepr_poc_route_table_association" {
  subnet_id      = aws_subnet.cluepr_poc_public_subnet.id
  route_table_id = aws_route_table.cluepr_poc_route_table.id
}

resource "aws_instance" "ec2" {
  count                       = var.instance_count
  ami                         = var.ami
  instance_type               = var.instance_type
  key_name                    = "EC2KeyPair"
  associate_public_ip_address = true
  subnet_id                   = aws_subnet.cluepr_poc_public_subnet.id
  vpc_security_group_ids = [
    aws_security_group.allow_ssh.id,
    aws_security_group.allow_http.id,
    aws_security_group.allow_https.id,
    aws_security_group.allow_flask.id]

  tags = {
    Name = element(var.instance_tags, count.index)
  }
}
