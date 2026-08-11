variable "resource_group_name" {
  description = "Name of the resource group"
  type        = string
}

variable "location" {
  description = "Azure region for the resources"
  type        = string
}
variable "ssh_public_key" {
  description = "SSH public key for the VM"
  type        = string
}