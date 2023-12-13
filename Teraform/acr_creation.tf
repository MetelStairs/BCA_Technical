# main.tf

provider "azurerm" {
  features = {}
}

# Define variables
variable "resource_group_name" {
  description = "The name of the Azure Resource Group"
  default     = "BCA_Dev_Hailstone"
}

variable "location" {
  description = "The Azure region where resources will be created"
  default     = "South UK"
}

variable "acr_name" {
  description = "The name of the Azure Container Registry"
  default     = "bca_acr_dev"
}

# Create a resource group
resource "azurerm_resource_group" "rg" {
  name     = var.resource_group_name
  location = var.location
}

# Create Azure Container Registry
resource "azurerm_container_registry" "acr" {
  name                = var.acr_name
  resource_group_name = azurerm_resource_group.rg.name
  location            = azurerm_resource_group.rg.location
  sku                 = "Standard"  # You can change this to "Basic" or "Premium" as needed
}