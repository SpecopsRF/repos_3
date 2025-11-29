terraform {
  required_version = ">= 1.0.0"
}

variable "app_name" {
  description = "Имя приложения"
  type        = string
  default     = "devsecops-demo"
}

variable "environment" {
  description = "Окружение"
  type        = string
  default     = "development"
}

variable "replicas" {
  description = "Количество реплик"
  type        = number
  default     = 2
}

output "app_name" {
  value = var.app_name
}

output "environment" {
  value = var.environment
}

output "replicas" {
  value = var.replicas
}

output "deployment_command" {
  value = "kubectl scale deployment ${var.app_name} --replicas=${var.replicas}"
}
