output "api_endpoint" {
  value = "${aws_api_gateway_stage.prod.invoke_url}/generate"
}

output "api_key" {
  value     = aws_api_gateway_api_key.my_key.value
  sensitive = true
}