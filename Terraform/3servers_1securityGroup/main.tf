###############################################################################
# Terraform describes the way you want your infrastructure and resources to be
#
# This Terraform creates 3 servers under 1 security group
#
###############################################################################

provider "aws" {
  region = "us-east-1"
}

resource "aws_default_vpc" "default" {} # This need to be added since AWS Provider v4.29+ to get VPC id

resource "aws_instance" "my_server_web" {
  ami                    = "ami-007855ac798b5175e"
  instance_type          = "t3.micro"
  vpc_security_group_ids = [aws_security_group.my_webserver.id]

  tags = {
    Name = "Server-Web"
  }
  depends_on = [aws_instance.my_server_db, aws_instance.my_server_app]
}

resource "aws_instance" "my_server_app" {
  ami                    = "ami-007855ac798b5175e"
  instance_type          = "t3.micro"
  vpc_security_group_ids = [aws_security_group.my_webserver.id]

  tags = {
    Name = "Server-Application"
  }

  depends_on = [aws_instance.my_server_db]
}


resource "aws_instance" "my_server_db" {
  ami                    = "ami-007855ac798b5175e"
  instance_type          = "t3.micro"
  vpc_security_group_ids = [aws_security_group.my_webserver.id]

  tags = {
    Name = "Server-Database"
  }
}



resource "aws_security_group" "my_webserver" {
  name   = "My Security Group"
  vpc_id = aws_default_vpc.default.id # This need to be added since AWS Provider v4.29+ to set VPC id


  dynamic "ingress" {
    for_each = ["80", "443", "22"]
    content {
      from_port   = ingress.value
      to_port     = ingress.value
      protocol    = "tcp"
      cidr_blocks = ["0.0.0.0/0"]
    }
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }

  tags = {
    Name = "My SecurityGroup"
  }
}